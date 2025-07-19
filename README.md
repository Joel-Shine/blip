<p align="center">
  <img src="https://github.com/Joel-Shine/ilovetreminal/blob/main/iloveterminal.svg" alt="iloveterminal logo" height="100">
</p>

<h1 align="center"><img src="https://github.com/Joel-Shine/blip/blob/main/logo.png" alt="blip logo" height="30"> Blip — A Lightweight CLI Text Editor</h1>

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

## 🛠️ Installation Guide

Blip runs on Windows, macOS, and Linux. Choose the method for your platform below:

---

### Windows (blip.exe)

1. Download the latest [`blip.exe`](https://github.com/Joel-Shine/blip/releases/latest)
2. Run the installer — it will:
   - Copy `blip.exe` to a system-wide location
   - Add it to your system `PATH` automatically
3. Open **Command Prompt** or **PowerShell**, and type:
   ```bash
   blip myfile.extension

### Mac-OS (blip-macos.tar.gz)

1. Download the latest [blip-macos.tar.gz](https://github.com/Joel-Shine/blip/releases/latest)
2. Extract and install it via terminal:
```bash
tar -xvzf blip-macos.tar.gz
chmod +x blip
sudo mv blip /usr/local/bin/
```
3. Open **iTerm2** or **Terminal**, and run globally:
   ```bash
   blip myfile.extension
   ```
   
### Linux/Debian (blip_installer.deb)

1. Download the latest [blip_installer.deb](https://github.com/Joel-Shine/blip/releases/latest)
2. Install it via terminal:
```bash
sudo dpkg -i file_name.deb
```
3. Open **Terminal**, and run globally:
   ```bash
   blip myfile.extension
   ```

### Or run from source
1. Clone this repo
2. Fire up command prompt and install the following requirements (ensure, it's Python 3 environment)
  ```bash
pip install prompt_toolkit pygments
```
3. Navigate to the directory, open up terminal and type:
```bash
python blip.py filename.extension
```

---

## 🚀 Usage

```bash
python blip.py               # Start editing a new file !
python blip.py myfile.py     # Open an existing file, and start editing !
```

---

## 🚀 DEMO

<p align="center">
  <img src="https://github.com/Joel-Shine/blip/blob/main/demo.png" width="1000" alt="DEMO.png">
</p>

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
