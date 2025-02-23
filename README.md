# Image Encryption Tool

## 🔒 About
This is a GUI-based **Image Encryption Tool** built using **Python** and **Tkinter**. It allows users to securely encrypt images using **AES-256 encryption** with a password. The tool features:

✅ **Drag and Drop Support** for easy file selection.  
✅ **Image Preview** before encryption.  
✅ **Dark Mode UI** for a modern look.  
✅ **AES-256 Encryption** for strong security.  

---

## 📜 Features
- Encrypts images using **AES (256-bit)** encryption.
- Uses **password-based encryption** for security.
- Supports **multiple image formats** (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`).
- Provides **image preview** before encryption.
- Allows **drag and drop** to select images.

---

## 🖥️ Installation & Usage

### 🔹 Prerequisites
Ensure you have Python installed. You can check by running:
```bash
python3 --version
```
If not installed, download Python from [here](https://www.python.org/downloads/).

### 🔹 Install Dependencies
Run the following command to install required libraries:
```bash
pip install -r requirements.txt
```
**OR** install manually:
```bash
pip install tkinterdnd2 pycryptodome pillow
```

### 🔹 Run the Tool
To start the application, run:
```bash
python3 image_encryption.py
```

---

## 🛠️ How to Use
1. **Enter a password** for encryption.
2. **Select an image** using the "Select Image" button **OR** drag and drop an image into the application.
3. The **image preview** will be shown.
4. Click the **"Encrypt"** button to encrypt the image.
5. The encrypted image will be saved as `image.enc` in the same location.

---

## 🏗️ Convert to Executable (.exe or Linux Binary)
You can create a standalone **executable file** using PyInstaller:
```bash
pyinstaller --onefile --windowed image_encryption.py
```
For **Linux Executable**:
```bash
pyinstaller --onefile image_encryption.py
```

---

## 🛡️ Security Note
- **Remember your password!** The tool does not store or recover passwords.
- Encrypted images cannot be decrypted without the correct password.

---


## 🖥️ Screenshots
![Screenshot_2025-02-23_01_29_29](https://github.com/user-attachments/assets/84b6fb7b-949d-4c03-822b-4578fedae8c6)


---

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Commit your changes: `git commit -m "Added new feature"`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a Pull Request.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📩 Contact
For issues or suggestions, create an issue on [GitHub](https://github.com/your-username/Image-Encryption-Tool).

Happy Encrypting! 🔐

