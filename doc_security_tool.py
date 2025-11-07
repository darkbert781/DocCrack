#!/usr/bin/env python3
"""
Document Security Tool - All-in-One Protection & Password Recovery
Supports Word, PDF, Excel, PowerPoint and more
Cross-platform: Windows, Linux, macOS

Author: ALinaswe Simfukwe
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
import sys
from pathlib import Path
import itertools
import string
from datetime import datetime

# Document handling imports
try:
    import pikepdf
except ImportError:
    pikepdf = None

try:
    import msoffcrypto
except ImportError:
    msoffcrypto = None

try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    PdfReader = PdfWriter = None


class DocumentSecurityTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Security Tool - Professional Edition")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Variables
        self.current_file = tk.StringVar()
        self.operation_mode = tk.StringVar(value="protect")
        self.password_var = tk.StringVar()
        self.is_running = False
        self.stop_flag = False
        
        # Style configuration
        self.setup_styles()
        
        # Create GUI
        self.create_gui()
        
    def setup_styles(self):
        """Setup professional styling"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        bg_color = '#f0f0f0'
        primary_color = '#2c3e50'
        accent_color = '#3498db'
        success_color = '#27ae60'
        danger_color = '#e74c3c'
        
        self.root.configure(bg=bg_color)
        
        # Button styles
        style.configure('Primary.TButton',
                       background=accent_color,
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       padding=10)
        
        style.configure('Success.TButton',
                       background=success_color,
                       foreground='white',
                       borderwidth=0,
                       padding=10)
        
        style.configure('Danger.TButton',
                       background=danger_color,
                       foreground='white',
                       borderwidth=0,
                       padding=10)
        
        # Frame styles
        style.configure('Card.TFrame',
                       background='white',
                       relief='raised',
                       borderwidth=1)
        
        style.configure('TLabel',
                       background='white',
                       foreground=primary_color)
        
        style.configure('Title.TLabel',
                       font=('Helvetica', 16, 'bold'),
                       background='white',
                       foreground=primary_color)
        
    def create_gui(self):
        """Create the main GUI interface"""
        # Main container
        main_container = ttk.Frame(self.root, padding="20")
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, weight=1)
        
        # Header
        header_frame = ttk.Frame(main_container, style='Card.TFrame', padding="20")
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        header_frame.columnconfigure(0, weight=1)
        
        title_label = ttk.Label(header_frame,
                               text="🔐 Document Security Tool",
                               style='Title.TLabel')
        title_label.grid(row=0, column=0, sticky=tk.W)
        
        subtitle_label = ttk.Label(header_frame,
                                  text="Protect & Recover Passwords for Word, PDF, Excel & More",
                                  font=('Helvetica', 10))
        subtitle_label.grid(row=1, column=0, sticky=tk.W, pady=(5, 0))
        
        # Mode Selection
        mode_frame = ttk.Frame(main_container, style='Card.TFrame', padding="20")
        mode_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        mode_frame.columnconfigure(1, weight=1)
        
        ttk.Label(mode_frame, text="Operation Mode:", font=('Helvetica', 11, 'bold')).grid(
            row=0, column=0, sticky=tk.W, pady=(0, 10), columnspan=2)
        
        protect_radio = ttk.Radiobutton(mode_frame,
                                       text="🔒 Protect Document (Add Password)",
                                       variable=self.operation_mode,
                                       value="protect",
                                       command=self.mode_changed)
        protect_radio.grid(row=1, column=0, sticky=tk.W, padx=(20, 0), pady=5)
        
        crack_radio = ttk.Radiobutton(mode_frame,
                                     text="🔓 Crack Password (Recover/Remove)",
                                     variable=self.operation_mode,
                                     value="crack",
                                     command=self.mode_changed)
        crack_radio.grid(row=2, column=0, sticky=tk.W, padx=(20, 0), pady=5)
        
        # File Selection
        file_frame = ttk.Frame(main_container, style='Card.TFrame', padding="20")
        file_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        file_frame.columnconfigure(1, weight=1)
        
        ttk.Label(file_frame, text="Select Document:", font=('Helvetica', 11, 'bold')).grid(
            row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        file_entry = ttk.Entry(file_frame, textvariable=self.current_file, state='readonly')
        file_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        
        browse_btn = ttk.Button(file_frame, text="Browse...",
                               command=self.browse_file,
                               style='Primary.TButton')
        browse_btn.grid(row=1, column=1, sticky=tk.E)
        
        # Password/Attack Settings
        self.settings_frame = ttk.Frame(main_container, style='Card.TFrame', padding="20")
        self.settings_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        self.settings_frame.columnconfigure(1, weight=1)
        
        # This will be populated based on mode
        self.create_protect_settings()
        
        # Action Buttons
        action_frame = ttk.Frame(main_container, style='Card.TFrame', padding="20")
        action_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        action_frame.columnconfigure(0, weight=1)
        
        self.action_btn = ttk.Button(action_frame,
                                     text="🔒 Protect Document",
                                     command=self.execute_action,
                                     style='Success.TButton')
        self.action_btn.grid(row=0, column=0, pady=(0, 10), sticky=(tk.W, tk.E))
        
        self.stop_btn = ttk.Button(action_frame,
                                   text="⏹ Stop",
                                   command=self.stop_operation,
                                   style='Danger.TButton',
                                   state='disabled')
        self.stop_btn.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Output/Log Area
        log_frame = ttk.Frame(main_container, style='Card.TFrame', padding="20")
        log_frame.grid(row=5, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 0))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(1, weight=1)
        main_container.rowconfigure(5, weight=1)
        
        ttk.Label(log_frame, text="Activity Log:", font=('Helvetica', 11, 'bold')).grid(
            row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        self.log_text = scrolledtext.ScrolledText(log_frame,
                                                  height=10,
                                                  wrap=tk.WORD,
                                                  font=('Courier', 9))
        self.log_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Progress bar
        self.progress = ttk.Progressbar(log_frame, mode='indeterminate')
        self.progress.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
    def create_protect_settings(self):
        """Create settings for protection mode"""
        # Clear existing widgets
        for widget in self.settings_frame.winfo_children():
            widget.destroy()
        
        ttk.Label(self.settings_frame,
                 text="Protection Settings:",
                 font=('Helvetica', 11, 'bold')).grid(
            row=0, column=0, sticky=tk.W, pady=(0, 10), columnspan=2)
        
        ttk.Label(self.settings_frame, text="Password:").grid(
            row=1, column=0, sticky=tk.W, pady=5)
        
        password_entry = ttk.Entry(self.settings_frame,
                                   textvariable=self.password_var,
                                   show='*',
                                   width=30)
        password_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(self.settings_frame, text="Confirm Password:").grid(
            row=2, column=0, sticky=tk.W, pady=5)
        
        self.confirm_password_var = tk.StringVar()
        confirm_entry = ttk.Entry(self.settings_frame,
                                 textvariable=self.confirm_password_var,
                                 show='*',
                                 width=30)
        confirm_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        
    def create_crack_settings(self):
        """Create settings for cracking mode"""
        # Clear existing widgets
        for widget in self.settings_frame.winfo_children():
            widget.destroy()
        
        ttk.Label(self.settings_frame,
                 text="Password Recovery Settings:",
                 font=('Helvetica', 11, 'bold')).grid(
            row=0, column=0, sticky=tk.W, pady=(0, 10), columnspan=2)
        
        # Attack method
        ttk.Label(self.settings_frame, text="Attack Method:").grid(
            row=1, column=0, sticky=tk.W, pady=5)
        
        self.attack_method = tk.StringVar(value="dictionary")
        attack_combo = ttk.Combobox(self.settings_frame,
                                    textvariable=self.attack_method,
                                    values=["Dictionary", "Brute Force", "Common Passwords"],
                                    state='readonly',
                                    width=28)
        attack_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        attack_combo.current(0)
        
        # Wordlist file (for dictionary attack)
        ttk.Label(self.settings_frame, text="Wordlist File:").grid(
            row=2, column=0, sticky=tk.W, pady=5)
        
        self.wordlist_var = tk.StringVar()
        wordlist_entry = ttk.Entry(self.settings_frame,
                                   textvariable=self.wordlist_var,
                                   state='readonly')
        wordlist_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(0, 10))
        
        wordlist_btn = ttk.Button(self.settings_frame,
                                 text="Browse...",
                                 command=self.browse_wordlist)
        wordlist_btn.grid(row=2, column=2, sticky=tk.E, pady=5)
        
        # Brute force settings
        ttk.Label(self.settings_frame, text="Max Length (Brute):").grid(
            row=3, column=0, sticky=tk.W, pady=5)
        
        self.max_length_var = tk.IntVar(value=4)
        length_spin = ttk.Spinbox(self.settings_frame,
                                 from_=1,
                                 to=8,
                                 textvariable=self.max_length_var,
                                 width=28)
        length_spin.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        
    def mode_changed(self):
        """Handle mode change"""
        mode = self.operation_mode.get()
        if mode == "protect":
            self.create_protect_settings()
            self.action_btn.configure(text="🔒 Protect Document")
        else:
            self.create_crack_settings()
            self.action_btn.configure(text="🔓 Crack Password")
        
    def browse_file(self):
        """Browse for document file"""
        filetypes = [
            ("All Supported", "*.pdf *.docx *.xlsx *.pptx *.doc *.xls *.ppt"),
            ("PDF Files", "*.pdf"),
            ("Word Documents", "*.docx *.doc"),
            ("Excel Files", "*.xlsx *.xls"),
            ("PowerPoint", "*.pptx *.ppt"),
            ("All Files", "*.*")
        ]
        
        filename = filedialog.askopenfilename(
            title="Select Document",
            filetypes=filetypes
        )
        
        if filename:
            self.current_file.set(filename)
            self.log(f"Selected file: {os.path.basename(filename)}")
    
    def browse_wordlist(self):
        """Browse for wordlist file"""
        filename = filedialog.askopenfilename(
            title="Select Wordlist",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        
        if filename:
            self.wordlist_var.set(filename)
            self.log(f"Selected wordlist: {os.path.basename(filename)}")
    
    def log(self, message):
        """Add message to log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def execute_action(self):
        """Execute the selected action"""
        if not self.current_file.get():
            messagebox.showerror("Error", "Please select a document file first!")
            return
        
        if self.operation_mode.get() == "protect":
            self.protect_document()
        else:
            self.crack_password()
    
    def protect_document(self):
        """Protect document with password"""
        password = self.password_var.get()
        confirm = self.confirm_password_var.get()
        
        if not password:
            messagebox.showerror("Error", "Please enter a password!")
            return
        
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        self.action_btn.configure(state='disabled')
        self.progress.start()
        
        thread = threading.Thread(target=self._protect_document_thread, args=(password,))
        thread.daemon = True
        thread.start()
    
    def _protect_document_thread(self, password):
        """Thread worker for document protection"""
        try:
            filepath = self.current_file.get()
            file_ext = os.path.splitext(filepath)[1].lower()
            
            self.log(f"Starting protection for {os.path.basename(filepath)}...")
            
            if file_ext == '.pdf':
                self._protect_pdf(filepath, password)
            elif file_ext in ['.docx', '.xlsx', '.pptx']:
                self._protect_office(filepath, password)
            else:
                self.log(f"❌ Unsupported file format: {file_ext}")
                messagebox.showerror("Error", f"File format {file_ext} not supported yet!")
                
        except Exception as e:
            self.log(f"❌ Error: {str(e)}")
            messagebox.showerror("Error", f"Failed to protect document:\n{str(e)}")
        finally:
            self.root.after(0, self._finish_operation)
    
    def _protect_pdf(self, filepath, password):
        """Protect PDF file"""
        if not pikepdf:
            self.log("❌ pikepdf library not installed. Install with: pip install pikepdf")
            return
        
        try:
            output_path = filepath.replace('.pdf', '_protected.pdf')
            
            with pikepdf.open(filepath) as pdf:
                pdf.save(output_path, encryption=pikepdf.Encryption(
                    owner=password,
                    user=password,
                    R=6  # AES-256 encryption
                ))
            
            self.log(f"✅ PDF protected successfully!")
            self.log(f"Saved as: {os.path.basename(output_path)}")
            messagebox.showinfo("Success", f"Document protected!\nSaved as:\n{output_path}")
            
        except Exception as e:
            raise Exception(f"PDF protection failed: {str(e)}")
    
    def _protect_office(self, filepath, password):
        """Protect Office document"""
        if not msoffcrypto:
            self.log("❌ msoffcrypto-tool library not installed.")
            self.log("Install with: pip install msoffcrypto-tool")
            return
        
        try:
            file_ext = os.path.splitext(filepath)[1]
            output_path = filepath.replace(file_ext, f'_protected{file_ext}')
            
            with open(filepath, 'rb') as infile:
                office_file = msoffcrypto.OfficeFile(infile)
                office_file.load_key(password=password)
                
                with open(output_path, 'wb') as outfile:
                    office_file.encrypt(password, outfile)
            
            self.log(f"✅ Office document protected successfully!")
            self.log(f"Saved as: {os.path.basename(output_path)}")
            messagebox.showinfo("Success", f"Document protected!\nSaved as:\n{output_path}")
            
        except Exception as e:
            raise Exception(f"Office protection failed: {str(e)}")
    
    def crack_password(self):
        """Start password cracking"""
        self.action_btn.configure(state='disabled')
        self.stop_btn.configure(state='normal')
        self.progress.start()
        self.stop_flag = False
        
        thread = threading.Thread(target=self._crack_password_thread)
        thread.daemon = True
        thread.start()
    
    def _crack_password_thread(self):
        """Thread worker for password cracking"""
        try:
            filepath = self.current_file.get()
            file_ext = os.path.splitext(filepath)[1].lower()
            attack = self.attack_method.get().lower()
            
            self.log(f"Starting password recovery for {os.path.basename(filepath)}...")
            self.log(f"Attack method: {attack}")
            
            if attack == "common passwords":
                passwords = self._get_common_passwords()
            elif attack == "dictionary":
                if not self.wordlist_var.get():
                    self.log("❌ Please select a wordlist file!")
                    return
                passwords = self._read_wordlist(self.wordlist_var.get())
            else:  # brute force
                passwords = self._generate_bruteforce(self.max_length_var.get())
            
            found = False
            attempts = 0
            
            for password in passwords:
                if self.stop_flag:
                    self.log("⏹ Operation stopped by user")
                    break
                
                attempts += 1
                if attempts % 100 == 0:
                    self.log(f"Tried {attempts} passwords...")
                
                if self._test_password(filepath, password, file_ext):
                    self.log(f"✅ PASSWORD FOUND: {password}")
                    self.log(f"Attempts: {attempts}")
                    messagebox.showinfo("Success!", 
                                      f"Password found!\n\nPassword: {password}\nAttempts: {attempts}")
                    found = True
                    break
            
            if not found and not self.stop_flag:
                self.log(f"❌ Password not found after {attempts} attempts")
                messagebox.showwarning("Not Found", 
                                      f"Password not found after {attempts} attempts.\nTry a different attack method.")
                
        except Exception as e:
            self.log(f"❌ Error: {str(e)}")
            messagebox.showerror("Error", f"Password recovery failed:\n{str(e)}")
        finally:
            self.root.after(0, self._finish_operation)
    
    def _test_password(self, filepath, password, file_ext):
        """Test if password is correct"""
        try:
            if file_ext == '.pdf':
                return self._test_pdf_password(filepath, password)
            elif file_ext in ['.docx', '.xlsx', '.pptx']:
                return self._test_office_password(filepath, password)
            return False
        except:
            return False
    
    def _test_pdf_password(self, filepath, password):
        """Test PDF password"""
        if pikepdf:
            try:
                with pikepdf.open(filepath, password=password):
                    return True
            except:
                return False
        return False
    
    def _test_office_password(self, filepath, password):
        """Test Office document password"""
        if not msoffcrypto:
            return False
        
        try:
            with open(filepath, 'rb') as file:
                office_file = msoffcrypto.OfficeFile(file)
                office_file.load_key(password=password)
                # Try to decrypt to verify
                import io
                output = io.BytesIO()
                office_file.decrypt(output)
                return True
        except:
            return False
    
    def _get_common_passwords(self):
        """Get list of common passwords"""
        return [
            'password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', 
            '1234567', 'letmein', 'trustno1', 'dragon', 'baseball', 'iloveyou',
            'master', 'sunshine', 'ashley', 'bailey', 'passw0rd', 'shadow',
            '123123', '654321', 'superman', 'qazwsx', 'michael', 'football',
            'password1', 'password123', 'admin', 'root', 'user', 'test',
            '12345', '1234', '123', 'welcome', 'login', 'pass', 'Password1'
        ]
    
    def _read_wordlist(self, filepath):
        """Read passwords from wordlist file"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    password = line.strip()
                    if password:
                        yield password
        except Exception as e:
            self.log(f"Error reading wordlist: {str(e)}")
            return []
    
    def _generate_bruteforce(self, max_length):
        """Generate brute force passwords"""
        chars = string.ascii_lowercase + string.digits
        for length in range(1, max_length + 1):
            for combo in itertools.product(chars, repeat=length):
                if self.stop_flag:
                    break
                yield ''.join(combo)
    
    def stop_operation(self):
        """Stop current operation"""
        self.stop_flag = True
        self.log("Stopping operation...")
        self.stop_btn.configure(state='disabled')
    
    def _finish_operation(self):
        """Finish operation and reset UI"""
        self.progress.stop()
        self.action_btn.configure(state='normal')
        self.stop_btn.configure(state='disabled')
        self.is_running = False


def main():
    """Main entry point"""
    root = tk.Tk()
    app = DocumentSecurityTool(root)
    
    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    main()
