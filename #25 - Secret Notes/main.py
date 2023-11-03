from tkinter import *
from tkinter import messagebox
import base64


# Functions
def encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    encoded_string = base64.urlsafe_b64encode(encoded_string.encode()).decode()
    return encoded_string


def decode(key, string):
    decoded_chars = []
    string = base64.urlsafe_b64decode(string).decode()
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(abs(ord(string[i]) - ord(key_c) % 256))
        decoded_chars.append(encoded_c)
    decoded_string = "".join(decoded_chars)
    return decoded_string


def save_and_encrypt_notes():
    # Get the data
    title = title_entry.get()
    note = note_text.get("1.0", END)
    master_secret = master_secret_entry.get()

    if len(title) == 0 or len(note) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error", message="Please fill in all the fields")
    else:
        # Encrypt the data
        encrypted_note = encode(master_secret, note)

        # Save the data
        try:
            with open("data.txt", mode="a") as file:
                file.write(f"{title} | {encrypted_note}\n")
        except FileNotFoundError:
            with open("data.txt", mode="w") as file:
                file.write(f"{title} | {encrypted_note}\n")

        # Clear the fields
        title_entry.delete(0, END)
        note_text.delete("1.0", END)
        master_secret_entry.delete(0, END)

        messagebox.showinfo(title="Success", message="Your data has been saved")


def decrypt_notes():
    # Get the data
    note = note_text.get("1.0", END)
    master_secret = master_secret_entry.get()

    if len(note) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error", message="Please fill in all the fields")
    else:
        try:
            # Decrypt the data
            decrypted_note = decode(master_secret, note)

            # Clear the fields and insert the decrypted note
            note_text.delete("1.0", END)
            note_text.insert(END, decrypted_note)
        except:
            messagebox.showinfo(title="Error", message="Please enter encrypted data")


# UI
# Window
FONT = ("Verdana", 15, "normal")
window = Tk()
window.title("Secret Notes")
window.geometry("500x700")

# Image
photo = PhotoImage(file="topsecret.png")
# photo_label = Label(image=photo)
# photo_label.pack()

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo)
canvas.pack()

# Label
title_info_label = Label(text="Enter your title", font=FONT)
title_info_label.pack()

# Entry
title_entry = Entry(width=50)
title_entry.pack()

# Label
note_info_label = Label(text="Enter your secret", font=FONT)
note_info_label.pack()

# Text
note_text = Text(height=10, width=50)
note_text.pack()

# Label
master_secret_label = Label(text="Enter your master key", font=FONT)
master_secret_label.pack()

# Entry
master_secret_entry = Entry(width=50)
master_secret_entry.pack()

# Button
save_button = Button(text="Save & Encrypt", width=15, font=FONT, command=save_and_encrypt_notes)
save_button.pack()

# Button
decrypt_button = Button(text="Decrypt", width=15, font=FONT, command=decrypt_notes)
decrypt_button.pack()

window.mainloop()
