# 🔐 DocCrack

**Professional all-in-one document security tool** for password protection and recovery.

[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-blue)]()
[![Python](https://img.shields.io/badge/python-3.7+-green)]()
[![License](https://img.shields.io/badge/license-MIT-orange)]()

## ✨ Features

### 🔒 Document Protection
- Password-protect PDF, Word, Excel, PowerPoint files
- AES-256 encryption (industry standard)
- Original files never modified
- Creates secure `_protected` versions

### 🔓 Password Recovery
- **Common Passwords**: Test popular passwords (~40 common ones)
- **Dictionary Attack**: Use custom wordlist files
- **Brute Force**: Try all combinations (configurable length)
- Real-time progress monitoring
- Stop/resume capability

### 🎨 Professional GUI
- Modern, intuitive interface
- Cross-platform (Windows, Linux, macOS)
- Real-time activity logging
- Color-coded actions
- No command-line required!

## 📸 Screenshots

![DocCrack GUI](docs/screenshot.png)

## 🚀 Quick Start

### Windows
```cmd
# One-time setup
setup_windows.bat

# Launch the tool
run_windows.bat
```

### Linux
```bash
# Use pre-compiled executable
./launch.sh

# Or run from source
pip3 install -r requirements.txt
python3 doc_security_tool.py
```

### macOS
```bash
pip3 install -r requirements.txt
python3 doc_security_tool.py
```

## 📦 Installation

### Download
**[⬇️ Download Latest Release](https://github.com/yourusername/DocCrack/releases)**

Or clone:
```bash
git clone https://github.com/yourusername/DocCrack.git
cd DocCrack
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run
```bash
python doc_security_tool.py
```

## 🎯 Supported Formats

| Format | Extension | Protection | Recovery |
|--------|-----------|-----------|----------|
| PDF | `.pdf` | ✅ | ✅ |
| Word | `.docx` | ✅ | ✅ |
| Excel | `.xlsx` | ✅ | ✅ |
| PowerPoint | `.pptx` | ✅ | ✅ |

## 💡 Usage Examples

### Protect a Document
1. Select **"Protect Document"** mode
2. Browse for your file
3. Enter password (twice)
4. Click **"🔒 Protect Document"**
5. Done! Protected file saved with `_protected` suffix

### Recover a Password
1. Select **"Crack Password"** mode
2. Browse for protected document
3. Choose attack method:
   - **Common Passwords** (fastest)
   - **Dictionary** (needs wordlist)
   - **Brute Force** (for short passwords)
4. Click **"🔓 Crack Password"**
5. Password displayed when found!

## 📊 Performance

| Attack Method | Speed | Best For |
|--------------|-------|----------|
| Common Passwords | ~1000/sec | Quick test |
| Dictionary | Variable | Known patterns |
| Brute Force (4 chars) | ~1 minute | Very short |
| Brute Force (5 chars) | ~30 minutes | Short |

## 🛠️ Development

### Build from Source
```bash
# Clone repository
git clone https://github.com/yourusername/DocCrack.git
cd DocCrack

# Install dependencies
pip install -r requirements.txt

# Run
python doc_security_tool.py
```

### Create Executable
**Windows:**
```cmd
compile_windows.bat
```

**Linux:**
```bash
pyinstaller --onefile --name "DocCrack" doc_security_tool.py
```

## 🔒 Security & Legal

### ⚠️ Legal Use Only
This tool is for:
- ✅ Recovering YOUR OWN forgotten passwords
- ✅ Authorized security testing
- ✅ Educational purposes
- ✅ Penetration testing with permission

### ❌ DO NOT:
- Attempt to crack passwords on documents you don't own
- Use on copyrighted/proprietary materials without authorization
- Violate computer fraud or privacy laws

**You are responsible for legal compliance!**

## 📝 Requirements

- Python 3.7 or higher
- tkinter (usually included with Python)
- See `requirements.txt` for Python packages

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **pikepdf** - PDF encryption/decryption
- **msoffcrypto-tool** - Office document handling
- **PyPDF2** - PDF support

## 📧 Support

- 📖 [Full Documentation](docs/)
- 🐛 [Report Issues](https://github.com/yourusername/DocCrack/issues)
- 💬 [Discussions](https://github.com/yourusername/DocCrack/discussions)

## ⭐ Star History

If you find this tool useful, please consider giving it a star!

---

**Made with ❤️ for document security**

*Educational and legitimate security research purposes only*
