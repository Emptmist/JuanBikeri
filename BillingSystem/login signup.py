from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


#===========================================FIRST PAGE PROFILE FOR LOG IN AND SIGN UP======================================================
# Create main window
window = Tk()
window.title('Login and Sign Up')
window.geometry('800x500')
window.configure(bg="#744c24")

Logo = Image.open("Bikeri.png")
resized = Logo.resize((250, 250))
logo = ImageTk.PhotoImage(resized)
image_label = Label(window, image=logo, bg="#744c24")
image_label.place(x=550, y=20)

def on_entry_click(event, entry, placeholder_text, placeholder_color):
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)  # Remove the placeholder text when clicked
        entry.config(foreground='black')  # Set the text color to black

def on_focus_out(event, entry, placeholder_text, placeholder_color):
    if entry.get() == '':
        entry.delete(0, tk.END)  # Remove the input text if empty
        entry.insert(0, placeholder_text)  # Insert the placeholder text if no input provided
        entry.config(foreground=placeholder_color)  # Set the text color to gray

def on_password_input(event, entry, placeholder_text):
    if entry.get() == placeholder_text:  # Check if the input matches the placeholder
        entry.config(show="")  # Set show option to display the actual characters
    else:
        entry.config(show="*")  # Set show option to display asterisks for password input

# Store user credentials in a dictionary
user_credentials = {}

# Function to handle sign-up window
def open_signup_window():
    signup_window = Toplevel()
    signup_window.title('Sign Up')
    signup_window.geometry('500x650')
    signup_window.configure(bg="#744c24")

    # Function to handle sign-up button click
    def sign_up():
        username = entry2.get()
        password = entry4.get()

        # Check if username already exists
        if username in user_credentials:
            messagebox.showerror('Sign Up Error', 'Username already exists!')
        else:
            # Add new user to the dictionary
            user_credentials[username] = password
            messagebox.showinfo('Sign Up Successful', 'You have successfully signed up!')
            signup_window.destroy()

    # Create labels and entry fields for sign-up window
    email_label = Label(signup_window, text='Email:', bg="#744c24", fg="white", font=("times new roman", 12, "bold"))
    email_label.place(x=45, y=220)
    placeholder_text1 = 'Enter your email'
    entry1 = tk.Entry(signup_window, foreground='gray', relief=SUNKEN, bg="#744c24", width=22)
    entry1.insert(0, placeholder_text1)
    entry1.bind('<FocusIn>', lambda event: on_entry_click(event, entry1, placeholder_text1, 'black'))
    entry1.bind('<FocusOut>', lambda event: on_focus_out(event, entry1, placeholder_text1, 'gray'))
    entry1.place(x=141, y=223)

    username_label = Label(signup_window, text='Username:', bg="#744c24", fg="white", font=("times new roman", 12, "bold"))
    username_label.place(x=45, y=250)
    placeholder_text2 = 'Enter your Username'
    entry2 = tk.Entry(signup_window, foreground='gray', relief=SUNKEN, bg="#744c24", width=22)
    entry2.insert(0, placeholder_text2)
    entry2.bind('<FocusIn>', lambda event: on_entry_click(event, entry2, placeholder_text2, 'black'))
    entry2.bind('<FocusOut>', lambda event: on_focus_out(event, entry2, placeholder_text2, 'gray'))
    entry2.place(x=141, y=253)

    password_label = Label(signup_window, text='Password:', bg="#744c24", fg="white", font=("times new roman", 12, "bold"))
    password_label.place(x=45, y=280)
    placeholder_text3 = 'Enter your password'
    entry3 = tk.Entry(signup_window, foreground='gray', relief=tk.SUNKEN, bg="#744c24", width=22, show="")
    entry3.insert(0, placeholder_text3)
    entry3.bind('<FocusIn>', lambda event: on_entry_click(event, entry3, placeholder_text3, 'black'))
    entry3.bind('<FocusOut>', lambda event: on_focus_out(event, entry3, placeholder_text3, 'gray'))
    entry3.bind('<Key>', lambda event: on_password_input(event, entry3, placeholder_text3))  # Bind key event to password input
    entry3.place(x=141, y=283)

    re_password_label = Label(signup_window, text='Re-Password:', bg="#744c24", fg="white", font=("times new roman", 12, "bold"))
    re_password_label.place(x=45, y=310)
    placeholder_text4 = 'Re-enter your password'
    entry4 = tk.Entry(signup_window, foreground='gray', relief=tk.SUNKEN, bg="#744c24", width=22, show="")
    entry4.insert(0, placeholder_text4)
    entry4.bind('<FocusIn>', lambda event: on_entry_click(event, entry4, placeholder_text4, 'black'))
    entry4.bind('<FocusOut>', lambda event: on_focus_out(event, entry4, placeholder_text4, 'gray'))
    entry4.bind('<Key>', lambda event: on_password_input(event, entry4, placeholder_text4))  # Bind key event to password input
    entry4.place(x=141, y=313)

    btn = tk.Button(signup_window, text='Sign-Up', bg="#744c24", relief=GROOVE, command=sign_up)
    btn.place(x=141, y=343)

def log_in():
    username = entry2.get()
    password = entry3.get()

    # Check if username and password match
    if username in user_credentials and user_credentials[username] == password:
        messagebox.showinfo('Login Successful', 'You have successfully logged in!')
    else:
        messagebox.showerror('Login Error', 'Invalid username or password!')

# Create labels and entry fields for login window
entry_username = Label(window, text='Username:', bg="#744c24", fg="white", font=("times new roman", 12, "bold"))
entry_username.place(x=45, y=220)
placeholder_text2 = 'Enter your Username'
entry2 = tk.Entry(window, foreground='gray', relief=SUNKEN, bg="#744c24", width=22)
entry2.insert(0, placeholder_text2)
entry2.bind('<FocusIn>', lambda event: on_entry_click(event, entry2, placeholder_text2, 'black'))
entry2.bind('<FocusOut>', lambda event: on_focus_out(event, entry2, placeholder_text2, 'gray'))
entry2.place(x=125, y=223)

entry_password = Label(window, text='Password:', bg="#744c24", fg="white", font=("times new roman", 12, "bold"))
entry_password.place(x=45, y=250)
placeholder_text3 = 'Enter your password'
entry3 = tk.Entry(window, foreground='gray', relief=SUNKEN, bg="#744c24", width=22, show="")
entry3.insert(0, placeholder_text3)
entry3.bind('<FocusIn>', lambda event: on_entry_click(event, entry3, placeholder_text3, 'black'))
entry3.bind('<FocusOut>', lambda event: on_focus_out(event, entry3, placeholder_text3, 'gray'))
entry3.bind('<Key>', lambda event: on_password_input(event, entry3, placeholder_text3))  # Bind key event to password input
entry3.place(x=125, y=253)

# Create buttons for sign up and login
btn = Button(window, text='SIGN UP', bg="#744c24", relief=GROOVE, command=open_signup_window)
btn.place(x=170, y=280)
btn = Button(window, text='LOG IN', bg="#744c24", relief=GROOVE, command=log_in)
btn.place(x=110, y=280)

window.mainloop()
