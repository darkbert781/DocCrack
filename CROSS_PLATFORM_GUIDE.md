# 🌐 Cross-Platform Usage Guide

Your Document Security Tool now works on **Windows, Linux, and macOS**!

---

## 📦 Package Contents

```
Operating system security/
├── doc_security_tool.py        ← Python source code (cross-platform)
├── requirements.txt            ← Dependencies
│
├── Linux:
│   ├── launch.sh               ← Linux launcher
│   └── dist/
│       └── DocumentSecurityTool  ← Linux executable (compiled)
│
├── Windows:
│   ├── run_windows.bat         ← Windows launcher
│   ├── setup_windows.bat       ← Windows setup
│   └── compile_windows.bat     ← Create Windows .exe
│
├── Test Files:
│   ├── sample_protected.pdf
│   └── sample_wordlist.txt
│
└── Documentation:
    ├── START_HERE.txt
    └── README.md
```

---

## 🪟 Windows Usage

### Option 1: Run Python Script (Recommended)

1. **First Time Setup**:
   - Double-click `setup_windows.bat`
   - Wait for dependencies to install

2. **Launch the Tool**:
   - Double-click `run_windows.bat`
   - GUI will open!

### Option 2: Create Windows Executable

If you want a standalone .exe file:

1. Double-click `compile_windows.bat`
2. Wait for compilation (~2 minutes)
3. Find your .exe at: `dist\DocumentSecurityTool.exe`
4. Run it anytime - no Python needed!

### Manual Commands (PowerShell/CMD)
```cmd
REM Install dependencies
python -m pip install pikepdf msoffcrypto-tool PyPDF2

REM Run the tool
python doc_security_tool.py

REM Or compile to .exe
python -m pip install pyinstaller
python -m PyInstaller --onefile --windowed doc_security_tool.py
```

---

## 🐧 Linux Usage

### Option 1: Use Pre-compiled Executable
```bash
# Already compiled and ready!
./launch.sh
```

### Option 2: Run Python Script
```bash
# Install dependencies (if not using executable)
pip3 install pikepdf msoffcrypto-tool PyPDF2

# Run the tool
python3 doc_security_tool.py
```

---

## 🍎 macOS Usage

### Setup
```bash
# Install Python (if not installed)
brew install python3

# Install dependencies
pip3 install pikepdf msoffcrypto-tool PyPDF2

# Run the tool
python3 doc_security_tool.py
```

### Create macOS App (Optional)
```bash
# Install PyInstaller
pip3 install pyinstaller

# Compile
pyinstaller --onefile --windowed --name "DocumentSecurityTool" doc_security_tool.py

# Run
open dist/DocumentSecurityTool.app
```

---

## 🎯 Quick Start by Platform

| Platform | Quick Command |
|----------|---------------|
| **Windows** | Double-click `run_windows.bat` |
| **Linux** | Run `./launch.sh` |
| **macOS** | Run `python3 doc_security_tool.py` |

---

## 📋 Requirements

### All Platforms Need:
- **Python 3.7+** (except if using compiled executables)
- **tkinter** (usually included with Python)
- **pip** (Python package manager)

### Python Libraries:
- `pikepdf` - PDF handling
- `msoffcrypto-tool` - Office documents
- `PyPDF2` - PDF support

---

## 🔧 Installation Methods Comparison

### Method 1: Python Script (Universal)
**Pros:**
- ✅ Works on all platforms
- ✅ Small file size (~24 KB)
- ✅ Easy to update
- ✅ One codebase

**Cons:**
- ⚠️ Requires Python installed
- ⚠️ Requires dependencies

**Best for:** Developers, technical users, cross-platform sharing

---

### Method 2: Compiled Executable (Platform-Specific)
**Pros:**
- ✅ No Python needed
- ✅ No dependencies to install
- ✅ Professional distribution
- ✅ Faster startup

**Cons:**
- ⚠️ Large file (~35 MB)
- ⚠️ Must compile per platform
- ⚠️ Harder to update

**Best for:** End users, professional distribution

---

## 🚀 Distribution Options

### For End Users (Non-Technical)
Provide compiled executables:
```
DocumentSecurityTool-v1.0/
├── Windows/
│   └── DocumentSecurityTool.exe
├── Linux/
│   └── DocumentSecurityTool
├── macOS/
│   └── DocumentSecurityTool.app
└── README.txt
```

### For Technical Users
Provide Python script:
```
DocumentSecurityTool-v1.0/
├── doc_security_tool.py
├── requirements.txt
├── run_windows.bat
├── launch.sh (Linux)
└── README.md
```

---

## 💡 Recommended Setup

### Windows Users:
1. Run `setup_windows.bat` (one-time)
2. Use `run_windows.bat` to launch
3. Optional: Compile to .exe for standalone use

### Linux Users:
1. Use pre-compiled executable: `./launch.sh`
2. Or install Python deps and run script

### macOS Users:
1. Install dependencies: `pip3 install -r requirements.txt`
2. Run: `python3 doc_security_tool.py`

---

## 🧪 Testing on Each Platform

### Test on Windows:
```cmd
python doc_security_tool.py
```
Open `sample_protected.pdf`, password: `password`

### Test on Linux:
```bash
./launch.sh
```
Or:
```bash
python3 doc_security_tool.py
```

### Test on macOS:
```bash
python3 doc_security_tool.py
```

---

## 🐛 Troubleshooting

### Windows Issues

**"Python is not recognized"**
- Install Python from python.org
- Check "Add Python to PATH" during install
- Restart terminal

**"tkinter not found"**
- Usually comes with Python
- Try reinstalling Python with tkinter option

**"DLL load failed"**
- Install Visual C++ Redistributable
- Download from Microsoft website

### Linux Issues

**"tkinter not available"**
```bash
sudo apt-get install python3-tk
```

**"Permission denied"**
```bash
chmod +x launch.sh doc_security_tool.py
```

### macOS Issues

**"Python not found"**
```bash
brew install python3
```

**"Application can't be opened"**
- Right-click → Open (first time)
- Or: System Preferences → Security & Privacy

---

## 📊 Platform Comparison

| Feature | Windows | Linux | macOS |
|---------|---------|-------|-------|
| **Pre-compiled available** | ❌ No | ✅ Yes | ❌ No |
| **Python script works** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Setup difficulty** | Easy | Easiest | Medium |
| **Compilation supported** | ✅ Yes | ✅ Yes | ✅ Yes |

---

## ✅ Summary

**Easiest Method for Each Platform:**

- 🪟 **Windows**: Run `setup_windows.bat`, then `run_windows.bat`
- 🐧 **Linux**: Run `./launch.sh` (already compiled)
- 🍎 **macOS**: `pip3 install -r requirements.txt` then `python3 doc_security_tool.py`

**For Professional Distribution:**
Compile separately on each platform using PyInstaller.

---

**Your tool is now truly cross-platform!** 🌍
