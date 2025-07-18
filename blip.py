import sys
import os
import asyncio
from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea, Label
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.python import PythonLexer
from prompt_toolkit.styles import Style

# 🎨 Styling
style = Style.from_dict({
    "": "bg:#002240 #ffffff",
    "status": "bg:#004466 #ffffff",
    "pygments.keyword": "bold #ff9d00",
    "pygments.name": "#c0ffff",
    "pygments.name.function": "bold #ffffff",
    "pygments.name.class": "bold #ffff00",
    "pygments.name.namespace": "#ffffff",
    "pygments.string": "#3ad900",
    "pygments.number": "#ff628c",
    "pygments.operator": "#ff9d00",
    "pygments.comment": "italic #0088ff",
})

# State & globals
state = {
    "filename": None,
    "mode": "edit",  # edit / save / open
}

# Load file from CLI
if len(sys.argv) > 1:
    state["filename"] = sys.argv[1]
    if os.path.exists(state["filename"]):
        with open(state["filename"], 'r') as f:
            content = f.read()
    else:
        content = ""
else:
    content = ""

# Text areas
editor = TextArea(
    text=content,
    multiline=True,
    scrollbar=True,
    line_numbers=True,
    lexer=PygmentsLexer(PythonLexer),
)

status = Label(text="💾 Ctrl+S | 📂 Ctrl+O | 🌐 Ctrl+L | ❌ Ctrl+Q", style="class:status")
input_bar = TextArea(height=1, prompt=">>> ", multiline=False)

# Async status update
async def set_status(msg, timeout=2.5):
    status.text = msg
    app.invalidate()
    await asyncio.sleep(timeout)
    status.text = "💾 Ctrl+S | 📂 Ctrl+O | 🌐 Ctrl+L | ❌ Ctrl+Q"
    app.invalidate()

# Key bindings
kb = KeyBindings()

@kb.add('c-q')
def _(e): e.app.exit()

@kb.add('(')
def _(e): e.app.current_buffer.insert_text('()'); e.app.current_buffer.cursor_left()
@kb.add('[')
def _(e): e.app.current_buffer.insert_text('[]'); e.app.current_buffer.cursor_left()
@kb.add('{')
def _(e): e.app.current_buffer.insert_text('{}'); e.app.current_buffer.cursor_left()
@kb.add('"')
def _(e): e.app.current_buffer.insert_text('""'); e.app.current_buffer.cursor_left()
@kb.add("'")
def _(e): e.app.current_buffer.insert_text("''"); e.app.current_buffer.cursor_left()

@kb.add('c-z')
def _(e):  # Undo
    e.app.current_buffer.undo()

@kb.add('c-y')
def _(e):  # Redo
    e.app.current_buffer.redo()

@kb.add('tab')
def _(e):  # Tab = 4 spaces
    e.app.current_buffer.insert_text('    ')

@kb.add('c-l')
def _(e):
    state["mode"] = "lang"
    input_bar.text = ""
    asyncio.create_task(set_status("🌐 Input language name (e.g., python, html, java), above 󱞿"))
    app.layout.focus(input_bar)

@kb.add('enter')
def _(e):
    mode = state["mode"]
    fname = input_bar.text.strip()
    if mode == "save":
        if fname:
            try:
                with open(fname, 'w') as f:
                    f.write(editor.text)
                state["filename"] = fname
                asyncio.create_task(set_status(f"✅ Saved to {fname}"))
            except Exception as err:
                asyncio.create_task(set_status(f"❌ Error saving: {err}"))
        else:
            asyncio.create_task(set_status("⚠️ Save cancelled."))
        input_bar.text = ""
        state["mode"] = "edit"
        app.layout.focus(editor)

    elif state["mode"] == "lang":
            from pygments.lexers import get_lexer_by_name
            try:
                editor.lexer = PygmentsLexer(get_lexer_by_name(fname).__class__)
                asyncio.create_task(set_status(f"🌐 Language set to {fname}"))
            except:
                asyncio.create_task(set_status(f"❌ Unknown language: {fname}"))

            state["mode"] = "edit"
            input_bar.text = ""
            app.layout.focus(editor)

    elif mode == "open":
        if fname and os.path.exists(fname):
            try:
                with open(fname, 'r') as f:
                    editor.text = f.read()
                state["filename"] = fname
                asyncio.create_task(set_status(f"📂 Opened {fname}"))
            except Exception as err:
                asyncio.create_task(set_status(f"❌ Error opening: {err}"))
        else:
            asyncio.create_task(set_status("❌ File not found."))
        input_bar.text = ""
        state["mode"] = "edit"
        app.layout.focus(editor)

    elif mode == "edit":
        # normal editing
        line = e.app.current_buffer.document.current_line_before_cursor
        if line.strip().endswith(':'):
            indent = len(line) - len(line.lstrip()) + 4
            e.app.current_buffer.insert_text('\n' + ' ' * indent)
        else:
            e.app.current_buffer.insert_text('\n')

@kb.add('c-s')
def _(e):
    if state["filename"]:
        try:
            with open(state["filename"], 'w') as f:
                f.write(editor.text)
            asyncio.create_task(set_status(f"✅ Saved to {state['filename']}"))
        except Exception as err:
            asyncio.create_task(set_status(f"❌ Error saving: {err}"))
        app.layout.focus(editor)
    else:
        state["mode"] = "save"
        asyncio.create_task(set_status("Input name of file to save, above 󱞿 "))
        app.layout.focus(input_bar)

@kb.add('c-o')
def _(e):
    state["mode"] = "open"
    asyncio.create_task(set_status("Input name of file to open, above 󱞿 "))
    app.layout.focus(input_bar)

# Layout
layout = Layout(HSplit([
    editor,
    input_bar,
    status
]))

app = Application(
    layout=layout,
    key_bindings=kb,
    style=style,
    full_screen=True,
    refresh_interval=0.1
)

if __name__ == "__main__":
    app.run()