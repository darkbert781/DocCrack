# 🚀 How to Upload DocCrack to GitHub

## Step 1: Prepare Files

✅ **Already done!** Your files are ready:
- `README_GITHUB.md` - Will become your main README
- `.gitignore` - Git ignore file
- `LICENSE` - MIT License
- All source code and scripts

---

## Step 2: Initialize Git Repository

Run these commands in your terminal:

```bash
cd "/home/darkbert/Desktop/Operating system security"

# Rename README for GitHub
mv README.md README_OLD.md
mv README_GITHUB.md README.md

# Initialize git
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit: DocCrack - Document Security Tool"
```

---

## Step 3: Create GitHub Repository

1. Go to **https://github.com**
2. Click **"New repository"** (green button)
3. Repository name: **`DocCrack`**
4. Description: **"Professional document protection & password recovery tool"**
5. Choose **Public** (or Private)
6. **DON'T** initialize with README (we already have one)
7. Click **"Create repository"**

---

## Step 4: Push to GitHub

GitHub will show you commands. Use these:

```bash
# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/DocCrack.git

# Set branch name
git branch -M main

# Push to GitHub
git push -u origin main
```

**Or with SSH** (if you have SSH key set up):
```bash
git remote add origin git@github.com:YOUR_USERNAME/DocCrack.git
git branch -M main
git push -u origin main
```

---

## Step 5: Add Topics/Tags on GitHub

On your repository page, click **"Add topics"** and add:
- `python`
- `security`
- `password-recovery`
- `pdf`
- `document-protection`
- `password-cracker`
- `tkinter`
- `cross-platform`

---

## Step 6: Create First Release (Optional)

1. On GitHub, click **"Releases"** → **"Create a new release"**
2. Tag version: **`v1.0.0`**
3. Release title: **"DocCrack v1.0.0 - Initial Release"**
4. Description:
   ```
   🎉 First stable release of DocCrack!
   
   Features:
   - Password protection for PDF, Word, Excel, PowerPoint
   - Password recovery with 3 attack methods
   - Cross-platform support (Windows, Linux, macOS)
   - Professional GUI
   
   Download and follow the README for installation instructions.
   ```
5. **Attach files** (optional):
   - Upload `dist/DocumentSecurityTool` (Linux executable)
6. Click **"Publish release"**

---

## Quick Command Summary

```bash
# Navigate to folder
cd "/home/darkbert/Desktop/Operating system security"

# Rename README
mv README.md README_OLD.md
mv README_GITHUB.md README.md

# Initialize git
git init
git add .
git commit -m "Initial commit: DocCrack - Document Security Tool"

# Add remote (CHANGE YOUR_USERNAME!)
git remote add origin https://github.com/YOUR_USERNAME/DocCrack.git

# Push
git branch -M main
git push -u origin main
```

---

## 📝 Before Pushing - Review These Files

Make sure to update in **README.md**:
- Replace `yourusername` with your actual GitHub username
- Add screenshot (optional): Create `docs/screenshot.png`
- Update any personal info

---

## 🎯 After Upload

Your repository will be at:
```
https://github.com/YOUR_USERNAME/DocCrack
```

Share it! 🚀

### Optional Enhancements:
1. **Add screenshot** - Take a screenshot of the GUI and add to repo
2. **GitHub Actions** - Auto-build Windows .exe on push
3. **Wiki** - Add detailed documentation
4. **Issues templates** - For bug reports
5. **Contribution guidelines** - `CONTRIBUTING.md`

---

## 🔒 Security Note

The `dist/DocumentSecurityTool` Linux executable is **34 MB**.
GitHub allows files up to 100 MB, so it's fine.

If you want to exclude it from git:
```bash
echo "dist/" >> .gitignore
git rm --cached dist/DocumentSecurityTool
git commit -m "Remove compiled executable from git"
```

Then provide it as a Release attachment instead.

---

**Ready to upload? Run the commands above!** 🚀
