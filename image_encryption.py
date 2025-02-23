import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256
from Cryptodome import Random
from PIL import Image, ImageTk

# Dark mode colors
BG_COLOR = "#2E2E2E"
FG_COLOR = "#FFFFFF"

selected_file = None  # Ensure global availability

def encrypt_image():
    global selected_file
    if not selected_file:
        messagebox.showerror("Error", "No image selected")
        return
    
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password")
        return
    
    try:
        with open(selected_file, "rb") as f:
            image_data = f.read()
        
        key = SHA256.new(password.encode()).digest()
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=8)
        encrypted_data = iv + cipher.encrypt(image_data)
        
        encrypted_path = selected_file + ".enc"
        with open(encrypted_path, "wb") as f:
            f.write(encrypted_data)
        
        messagebox.showinfo("Success", f"Image encrypted and saved as: {encrypted_path}")
    except Exception as e:
        messagebox.showerror("Encryption Error", f"An error occurred: {str(e)}")

def select_file():
    global selected_file
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        update_selected_file(file_path)

def drop_file(event):
    global selected_file
    file_path = event.data.strip().replace('{', '').replace('}', '')  # Clean up file path
    update_selected_file(file_path)

def update_selected_file(file_path):
    global selected_file
    selected_file = file_path
    show_preview(file_path)
    status_label.config(text="Image selected successfully", fg="#00FF00")
    encrypt_button.config(state=tk.NORMAL)

def show_preview(image_path):
    try:
        img = Image.open(image_path)
        img.thumbnail((150, 150))  # Resize while maintaining aspect ratio
        img = ImageTk.PhotoImage(img)
        preview_label.config(image=img)
        preview_label.image = img
    except Exception as e:
        messagebox.showerror("Preview Error", f"Cannot load image preview: {str(e)}")

# GUI Setup
root = TkinterDnD.Tk()  # Use TkinterDnD for drag-and-drop support
root.title("Image Encryption Tool")
root.geometry("450x400")
root.configure(bg=BG_COLOR)

tk.Label(root, text="Enter Encryption Password:", fg=FG_COLOR, bg=BG_COLOR).pack(pady=5)
password_entry = ttk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

preview_label = tk.Label(root, bg=BG_COLOR)
preview_label.pack(pady=5)

status_label = tk.Label(root, text="Drag and drop an image here", fg=FG_COLOR, bg=BG_COLOR)
status_label.pack(pady=5)

drop_area = tk.Label(root, text="Drop Image Here", bg="#444444", fg=FG_COLOR, width=40, height=4)
drop_area.pack(pady=10)
drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind("<<Drop>>", drop_file)

select_button = ttk.Button(root, text="Select Image", command=select_file)
select_button.pack(pady=5)

encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt_image, state=tk.DISABLED)
encrypt_button.pack(pady=5)

root.mainloop()
