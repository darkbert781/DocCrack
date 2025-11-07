# DocCrack

Document security tool for password protection and recovery of PDF, Word, Excel, and PowerPoint files.

## Features

**Protection**
- Add passwords to documents (PDF, Word, Excel, PowerPoint)
- AES-256 encryption for PDFs
- Originals never modified

**Recovery**
- Common password checking
- Dictionary attacks
- Brute force (configurable)
- GUI with real-time progress

## Installation

```bash
git clone https://github.com/darkbert781/DocCrack.git
cd DocCrack
pip install -r requirements.txt
python doc_security_tool.py
```

### Windows
Run `setup_windows.bat` then `run_windows.bat`

### Linux  
Pre-compiled executable included: `./launch.sh`

### macOS
```bash
pip3 install -r requirements.txt
python3 doc_security_tool.py
```

## Usage

**Protect a document:**
1. Select "Protect Document" mode
2. Choose file
3. Enter password
4. Click Protect

**Crack a password:**
1. Select "Crack Password" mode
2. Choose protected file
3. Pick attack method (Common/Dictionary/Brute Force)
4. Click Crack

## Supported Formats

- PDF (.pdf)
- Word (.docx)
- Excel (.xlsx)
- PowerPoint (.pptx)

## Performance

- Common passwords: ~1000/sec
- Dictionary: depends on wordlist
- Brute force (4 chars): ~1 min
- Brute force (5 chars): ~30 min

## Building

Create standalone executable:

**Windows:** `compile_windows.bat`  
**Linux:** `pyinstaller --onefile --name DocCrack doc_security_tool.py`

## Legal Notice

This tool is for:
- Recovering your own forgotten passwords
- Authorized security testing
- Educational purposes

Do not use on documents you don't own or without permission.

## Requirements

- Python 3.7+
- pikepdf
- msoffcrypto-tool
- PyPDF2

## Author

Created by **ALinaswe Simfukwe**

## License

MIT License - see LICENSE file
