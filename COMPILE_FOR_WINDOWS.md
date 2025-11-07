# 🪟 How to Compile for Windows

The current executable is for **Linux only**. To create a Windows version, you need to compile on a Windows machine.

---

## 📥 Download Python Source

The Python source code is embedded in the Linux executable but was removed from this package. You have two options:

### Option 1: Extract from Git/Backup
If you have the original source code, use that.

### Option 2: Use the Embedded Code
The executable contains the source. To make a Windows version, you'll need to recreate it or use a different approach.

---

## 🪟 Compile on Windows

### Prerequisites (Windows)
1. **Python 3.7+** - Download from [python.org](https://www.python.org/downloads/)
2. **Git Bash** or **PowerShell**

### Steps

#### 1. Install Python Dependencies
```powershell
pip install pikepdf msoffcrypto-tool PyPDF2 pyinstaller
```

#### 2. Get the Source Code
You'll need `doc_security_tool.py` - the Python script that was compiled.

#### 3. Compile for Windows
```powershell
pyinstaller --onefile --windowed --name "DocumentSecurityTool" doc_security_tool.py
```

#### 4. Find Your Executable
```
dist\DocumentSecurityTool.exe
```

---

## 🌐 Alternative: Cross-Platform Python Script

Instead of a compiled executable, you can run the Python script directly on any platform:

### On Windows:
```powershell
python doc_security_tool.py
```

### On Linux:
```bash
python3 doc_security_tool.py
```

### On macOS:
```bash
python3 doc_security_tool.py
```

---

## 📦 Best Solution: Provide Multiple Builds

For cross-platform distribution, create separate builds:

```
DocumentSecurityTool/
├── linux-x64/
│   └── DocumentSecurityTool
├── windows-x64/
│   └── DocumentSecurityTool.exe
├── macos-x64/
│   └── DocumentSecurityTool
└── README.md
```

Each platform needs to be compiled on its native OS.

---

## 🔧 Quick Windows Compilation Script

Save this as `compile_windows.bat`:

```batch
@echo off
echo Installing dependencies...
pip install pikepdf msoffcrypto-tool PyPDF2 pyinstaller

echo Compiling for Windows...
pyinstaller --onefile --windowed --name "DocumentSecurityTool" doc_security_tool.py

echo Done! Executable is in dist\DocumentSecurityTool.exe
pause
```

---

## 🐍 Universal Python Solution

If you want true cross-platform support without multiple executables, distribute as a Python package:

### Create `run.bat` (Windows):
```batch
@echo off
python doc_security_tool.py
```

### Keep `launch.sh` (Linux/Mac):
```bash
#!/bin/bash
python3 doc_security_tool.py
```

### Create `requirements.txt`:
```
pikepdf>=8.0.0
msoffcrypto-tool>=5.0.0
PyPDF2>=3.0.0
```

Users install once:
```
pip install -r requirements.txt
```

Then run on any platform!

---

## ⚡ Need the Source Code?

The source code `doc_security_tool.py` was removed from this package to keep it minimal. 

To get it back:
1. Check your version control (Git)
2. Restore from backup
3. Or I can regenerate it for you

---

## 🎯 Recommended Approach

**For Maximum Compatibility:**

1. **Keep the Python script** (`doc_security_tool.py`)
2. **Provide simple launchers** for each platform
3. **Users install Python once** (one-time setup)
4. **Script runs everywhere** (Windows, Linux, macOS)

This avoids maintaining multiple compiled versions!

---

## 📊 Comparison

| Method | Pros | Cons |
|--------|------|------|
| **Compiled (Current)** | No Python needed | Platform-specific, large file |
| **Python Script** | Cross-platform, small | Requires Python installed |
| **Multiple Builds** | Best of both | Must compile 3 times |

---

## 💡 My Recommendation

Since you want Windows support, I suggest:

1. **I recreate the source code** (`doc_security_tool.py`)
2. **Add simple launchers** for Windows and Linux
3. **Include setup scripts** for Python dependencies
4. **One codebase, all platforms** work

This is simpler than maintaining multiple compiled executables!

---

Would you like me to:
- ✅ Recreate the Python source code?
- ✅ Add Windows launcher scripts?
- ✅ Make it truly cross-platform?

Let me know!
