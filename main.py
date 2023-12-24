from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# PASSWORD GENERATOR
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = ([random.choice(letters) for _ in range(5)] + [random.choice(numbers) for _ in range(4)] +
                [random.choice(symbols) for _ in range(4)])

    final_password = ''.join(random.sample(password, len(password)))
    entry_pass.delete(0, END)
    entry_pass.insert(0, final_password)
    pyperclip.copy(final_password)


# SAVE PASSWORD
def save_pass():
    web = entry_web.get().title()
    user = entry_user.get()
    password = entry_pass.get()
    new_dict = {
        web: {
            'Email/User': user,
            'Password': password
        }
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title='Warning!', message='Please fill empty fields.')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_dict, data_file, indent=4)
        else:
            data.update(new_dict)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_web.delete(0, END)
            entry_pass.delete(0, END)
            entry_web.focus()


# Search function
def search():
    web = entry_web.get().title()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Warning!', message='Data file not found.')
    else:
        try:
            messagebox.showinfo(title=web, message=f'Email/user: {data[web]["Email/User"]}\n'
                                                   f'Password: {data[web]["Password"]}')
        except KeyError:
            messagebox.showinfo(title='Warning!', message=f'Details not found for {web}\nPlease save one.')


# UI SETUP
windows = Tk()
windows.title('Password Manager')
windows.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
image_logo = PhotoImage(file='logo.png')
canvas.create_image(63, 90, image=image_logo)
canvas.grid(column=1, row=0)

# Label & Entry website
label_web = Label(text='Website:')
label_web.grid(column=0, row=1)

entry_web = Entry(width=35)
entry_web.focus()
entry_web.grid(column=1, row=1, columnspan=2)

# Label Email/username
label_user = Label(text='Email/Username:')
label_user.grid(column=0, row=3)

entry_user = Entry(width=35)
entry_user.insert(END, 'testing@gmail.com')
entry_user.grid(column=1, row=3, columnspan=2)

# Label Password
label_pass = Label(text='Password:')
label_pass.grid(column=0, row=4)

entry_pass = Entry(width=35)
entry_pass.grid(column=1, row=4, columnspan=2, padx=5, pady=5)

# Add Button
add_button = Button(text='Add', width=30, command=save_pass)
add_button.grid(column=1, row=6, padx=5, pady=5)

# Search Button
search_button = Button(text='Search', width=30, command=search)
search_button.grid(column=1, row=2, pady=5, padx=5)

# Generate password button
pass_button = Button(text='Generate Password', width=30, command=pass_gen)
pass_button.grid(column=1, row=5)

windows.mainloop()
