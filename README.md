<p align="center">
  <img src="https://github.com/Joel-Shine/ilovetreminal/blob/main/iloveterminal.svg" alt="iloveterminal logo" height="100">
</p>

<h1 align="center">📄 Blip — A Lightweight CLI Text Editor</h1>

---

## ✨ Features

- 🔤 **Syntax highlighting** (auto-detects language by file extension)
- 💾 **Save** files with `Ctrl+S` — includes autocomplete file naming
- 📂 **Open** files with `Ctrl+O` — type with live autocomplete
- ⌨️ **Keyboard driven** editing experience
- 🧠 Intelligent indentation and structure-aware lexer
- 🖱️ **Mouse support** for scrolling and navigation
- 🧱 Simple layout with status bar and file info

---

## 🛠️ Installation

```bash
pip install prompt_toolkit pygments
```

---

## 🚀 Usage

```bash
python blip.py               # Start editing a new file
python blip.py myfile.py     # Open an existing file
```

---

## 🧭 Keyboard Shortcuts

| Shortcut     | Action                      |
|--------------|-----------------------------|
| `Ctrl+S`     | Save file                   |
| `Ctrl+L`     | Change Language (for lexer) |
| `Ctrl+O`     | Open file                   |
| `Ctrl+Q`     | Quit the editor             |
| `Enter`      | Confirm file open/save      |

---

## 💡 Why Blip?

Blip is ideal for:
- Quick edits without opening a bloated GUI
- Scripting environments
- Terminal-focused devs
- Retro charm with modern behavior

---

## 🧠 Tech Stack

- [`prompt_toolkit`](https://github.com/prompt-toolkit/python-prompt-toolkit)
- [`pygments`](https://pygments.org/) for syntax lexing

---

## 🧪 Screenshot

```
+----------------------------------------------------------+
| def hello():                                             |
|     print("Hello from Blip!")                            |
|                                                          |
|                                                          |
+----------------------------------------------------------+
[File saved to hello.py ✅]
```