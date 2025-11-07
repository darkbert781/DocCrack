# 🔐 Document Security Tool - Professional Edition

A comprehensive all-in-one tool for document protection and password recovery supporting Word, PDF, Excel, PowerPoint, and other office formats.

## ✨ Features

### Document Protection
- **Password Protection**: Secure your documents with strong passwords
- **AES-256 Encryption**: Industry-standard encryption for PDFs
- **Multi-Format Support**: 
  - PDF (`.pdf`)
  - Microsoft Word (`.docx`, `.doc`)
  - Microsoft Excel (`.xlsx`, `.xls`)
  - Microsoft PowerPoint (`.pptx`, `.ppt`)

### Password Recovery
- **Multiple Attack Methods**:
  - **Common Passwords**: Try most commonly used passwords
  - **Dictionary Attack**: Use custom wordlist files
  - **Brute Force**: Systematic password generation (configurable length)
- **Real-time Progress**: See attempts and status in live log
- **Stop Anytime**: Cancel operation at any point
- **Success Rate**: Works on standard password-protected documents

### Professional GUI
- Modern, clean interface
- Intuitive workflow
- Real-time activity logging
- Progress indicators
- Professional styling with color-coded actions

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Quick Setup (Recommended)

**For systems with externally-managed Python (Kali, Ubuntu 23.04+):**

```bash
# Run the setup script (creates virtual environment automatically)
./setup_venv.sh

# Launch the application
./run.sh
```

### Manual Installation

**Option 1: Virtual Environment (Recommended)**

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python doc_security_tool.py
```

**Option 2: System-wide (if allowed)**

```bash
# Install dependencies
pip install pikepdf msoffcrypto-tool PyPDF2

# Run the application
python3 doc_security_tool.py
```

**Option 3: Use pipx**

```bash
# Coming soon - standalone app installation
```

## 📖 Usage Guide

### Protecting a Document

1. Select **"Protect Document (Add Password)"** mode
2. Click **"Browse..."** to select your document
3. Enter your desired password
4. Confirm the password
5. Click **"🔒 Protect Document"**
6. The protected file will be saved with `_protected` suffix

### Recovering/Cracking a Password

1. Select **"Crack Password (Recover/Remove)"** mode
2. Click **"Browse..."** to select the protected document
3. Choose an attack method:
   - **Common Passwords**: Quick check of popular passwords
   - **Dictionary**: Upload a wordlist file (one password per line)
   - **Brute Force**: Try all combinations up to specified length
4. Configure settings based on chosen method
5. Click **"🔓 Crack Password"**
6. Monitor progress in the activity log
7. Password will be displayed when found

## 💡 Tips & Best Practices

### For Protection:
- Use strong, unique passwords (mix of letters, numbers, symbols)
- Store passwords securely (password manager recommended)
- Keep backups of unprotected originals in secure location
- Test opening protected file to verify password works

### For Recovery:
- Start with **Common Passwords** - fastest method
- Use targeted wordlists for dictionary attacks
- Brute force is time-intensive - start with length 4-5
- Consider what you know about the password (length, patterns)
- Larger wordlists increase success chance but take longer

## 📋 Wordlist Resources

For dictionary attacks, you can use wordlists such as:
- **SecLists**: https://github.com/danielmiessler/SecLists
- **RockYou**: Popular leaked password database
- **Custom lists**: Create based on known patterns

Create simple wordlist:
```bash
echo -e "password\n123456\nadmin\nwelcome" > wordlist.txt
```

## ⚙️ Technical Details

### Supported Formats
| Format | Protection | Recovery | Encryption |
|--------|-----------|----------|------------|
| PDF | ✅ | ✅ | AES-256 |
| DOCX | ✅ | ✅ | AES-128/256 |
| XLSX | ✅ | ✅ | AES-128/256 |
| PPTX | ✅ | ✅ | AES-128/256 |

### Dependencies
- **pikepdf**: PDF manipulation and encryption
- **msoffcrypto-tool**: Office document encryption/decryption
- **PyPDF2**: Alternative PDF handling
- **tkinter**: GUI framework (included with Python)

### Performance
- Common passwords: ~1000 tries/second
- Dictionary attack: Depends on wordlist size and disk I/O
- Brute force: ~500-1000 tries/second (varies by system)

## 🔒 Security & Legal Notice

### Important Notes:
⚠️ **Legal Use Only**: This tool is for:
- Recovering YOUR OWN forgotten passwords
- Security research and testing on authorized documents
- Educational purposes

❌ **DO NOT**:
- Attempt to crack passwords on documents you don't own
- Use on copyrighted/proprietary materials without authorization
- Violate computer fraud or privacy laws in your jurisdiction

### Disclaimer:
This software is provided for legitimate security purposes only. Users are responsible for ensuring their use complies with applicable laws. The authors assume no liability for misuse.

## 🐛 Troubleshooting

### "Library not installed" errors
```bash
pip install --upgrade pikepdf msoffcrypto-tool PyPDF2
```

### GUI doesn't appear
Ensure tkinter is installed:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# macOS (usually pre-installed)
```

### "File format not supported"
- Ensure file extension is correct
- Try converting to newer format (e.g., .doc → .docx)
- Some legacy formats may not be supported

### Password recovery is slow
- Start with shorter passwords for brute force (length 3-4)
- Use dictionary attacks with targeted wordlists
- Consider password complexity when estimating time

## 🔄 Updates & Roadmap

### Current Version: 1.0.0

### Planned Features:
- [ ] ZIP/RAR archive support
- [ ] GPU acceleration for faster cracking
- [ ] Password strength meter
- [ ] Batch processing multiple files
- [ ] Export cracked passwords list
- [ ] Custom character sets for brute force
- [ ] Mask attacks (known password patterns)
- [ ] Hybrid attacks (dictionary + brute force)

## 📝 License

This project is provided as-is for educational and legitimate security purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the documentation
3. Create an issue with detailed information

---

**Made with ❤️ for document security**

⭐ If you find this tool useful, please star the repository!
