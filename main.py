from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    # Copy password into the clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get().strip()
    email = email_input.get().strip()
    password = password_input.get()
    if not website or not email or not password:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n"
                                                          f"Password: {password} \nIs it ok to save?")
    if is_ok:
        with open("data.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=480, height=380)
window.config(padx=20, pady=20)

logo_img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(130, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

# Website row
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e", padx=20, pady=2)

website_input = Entry(width=42)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

# Email row
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="e", padx=20, pady=2)

email_input = Entry(width=42)
email_input.insert(0, "kamil@email.com")
email_input.grid(column=1, row=2, columnspan=2)

# Password row
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e", padx=20, pady=2)

password_input = Entry(width=22)
password_input.grid(column=1, row=3, sticky="w")

password_button = Button(text="Generate Password", command=generate_password, relief="groove")
password_button.grid(column=2, row=3, sticky="e")

# Add button
add_button = Button(text="Add", command=save_password, width=35, relief="groove")
add_button.grid(column=1, row=4, columnspan=2, pady=2)

window.mainloop()
