from tkinter import *
import sys
import os


def loginmain():
    global window # global variable is created so the variable can be used throughout the program in any function
    window = Tk()  # Creates a window and configures it
    window.geometry('250x200+250+200')
    window.title("Log in")
    window.config(bg="#c4c4c4")
    window.geometry("1100x700")
    window.resizable(width=False, height=False)  # The user is unable to resize the window so the widgets don't get moved around

    global username_verify
    global password_verify

    global username_entry1
    global password_entry1
    window.protocol("WM_DELETE_WINDOW", close_window)  # if the window is closed,calls function, the program ends
    username_verify = StringVar()
    password_verify = StringVar()

    Label(text="Funimate", bg="#c4c4c4", font=("Calibri", 100)).pack()  # creates a label
    Label(text="Username:", bg="#c4c4c4", font=("Calibri", 20)).place(x=340, y=200)
    username_entry1 = Entry(textvariable=username_verify, bg="#499292", border=0, font=("Calibri", 30), width=20)
    username_entry1.place(x=344, y=240)  # creates an entry window where the user can enter their information
    Label(text="Password:", bg="#c4c4c4", font=("Calibri", 20)).place(x=340, y=330)
    password_entry1 = Entry(textvariable=password_verify, bg="#499292", border=0, font=("Calibri", 30), width=20)
    password_entry1.place(x=344, y=370)

    login_button = Button(text="Log in", height="2", width="18", bg="#868EA5", border=1, relief=SOLID, font=("Calibri", 15), command=login_user)
    login_button.pack(pady=160, side=BOTTOM)

    registerlink_text = Label(text="Haven't got an account?                now", bg="#c4c4c4", font=("Calibri", 17))
    registerlink_text.place(x=370, y=590)
    register_link = Label(text="Sign up", bg="#c4c4c4", font=("Calibri", 17), cursor="hand2", fg="blue")
    register_link.place(x=601, y=590)
    register_link.bind("<Button-1>", lambda e: registerwindow()) # Makes the text a hyperlink so when pressed it calls a function like a button

    window.mainloop()


def close_window():
    sys.exit("User closed program")  # closes the window with the message


def login_user():

    username1 = username_verify.get().lower()  # Sets the variable as the text in the username entry box after the login button is pressed
    password1 = password_verify.get()

    files_list = os.listdir()  # Looks for the name of the user in the file directory as this is where the user accounts are stored
    if username1 in files_list:  # if the username is the same name as one of the files then a user has been found
        file1 = open(username1, "r")  # opens the file with the username in and checks for the password
        p_check = file1.read().splitlines()  # if the password is in the file with its corresponding username then login success
        if password1 in p_check:  # If the password
            message = "Login Success"
            message_window(message)  # calls the message window function with the message variable that differs depending on result
        else:
            message = "Password has not been recognised"
            password_entry1.delete(0, END)
            message_window(message)
    else:
        message = "User not found"
        username_entry1.delete(0, END)  # Deletes the contents of the entry boxes
        password_entry1.delete(0, END)
        message_window(message)


def delete2(message):
    if message == "Login Success":
        message_box.destroy()
        window.destroy()  # Destroys the message box and the login window if its successful so that the main program can run
    else:
        message_box.destroy()  # only gets rid of the message box if the login is unsuccessful


def message_window(message):
    global message_box
    message_box = Toplevel(window)  # creates a window to act as a message box
    message_box.title("message window")
    message_box.config(bg="#c4c4c4")
    message_box.geometry("400x170")
    message_box.resizable(width=False, height=False)
    Label(message_box, text=message, bg="#c4c4c4", font=("Calibri", 20)).pack(pady=5, side=TOP)  # displays the message depending on the result
    if message == "Password has not been recognised":
        Label(message_box, text="Reminder: passwords are case sensitive", bg="#c4c4c4", font=("Calibri", 10)).pack(side=TOP) # displays an extra message if the password has not been recognised
    Button(message_box, text="Okay", height="1", width="12", bg="#868EA5", border=1, relief=SOLID, font=("Calibri", 13), command=lambda: delete2(message)).pack()
    Frame(message_box, width=400, height=25, bg="#499292").pack(side=BOTTOM)


def registerwindow():
    global window1
    window1 = Toplevel(window)
    window1.title("Register")
    window1.geometry('250x200+250+200')
    window1.config(bg="#c4c4c4")
    window1.geometry("530x650")
    window1.resizable(width=False, height=False)
    global username
    global password
    global cpassword
    global username_entry
    global password_entry
    global confirmpassword_entry
    username = StringVar()
    password = StringVar()
    cpassword = StringVar()
    Label(window1, text="Create account", bg="#c4c4c4", font=("Calibri", 60)).pack()
    Label(window1, text="Username:", bg="#c4c4c4", font=("Calibri", 20)).place(x=70, y=120)
    username_entry = Entry(window1, textvariable=username, bg="#499292", border=0, font=("Calibri", 30), width=20)
    username_entry.place(x=74, y=160)
    Label(window1, text="Password:", bg="#c4c4c4", font=("Calibri", 20)).place(x=70, y=250)
    password_entry = Entry(window1, textvariable=password, bg="#499292", border=0, font=("Calibri", 30), width=20)
    password_entry.place(x=74, y=290)
    Label(window1, text="Confirm password:", bg="#c4c4c4", font=("Calibri", 20)).place(x=70, y=380)
    confirmpassword_entry = Entry(window1, textvariable=cpassword, bg="#499292", border=0, font=("Calibri", 30), width=20)
    confirmpassword_entry.place(x=74, y=420)
    Button(window1, text="Sign Up", height="2", width="20", bg="#868EA5", border=1, relief=SOLID, font=("Calibri", 15), command=register_user).pack(pady=60, side=BOTTOM)



def register_user():
    username_info = username.get()
    password_info = password.get()
    cpassword_info = cpassword.get()
    files_list = os.listdir()

    if username_info in files_list:  # error handling // Checks what entry boxes have information in when the button is clicked and display a message depending on the result
        Label(window1, text="This username has already been taken   ", fg="Red", bg="#c4c4c4", font=("calibri", 13)).place(x=126, y=600)
    elif len(password_info) == 0 and len(username_info) == 0:
        Label(window1, text="Please enter a Username and password", fg="Red", bg="#c4c4c4", font=("calibri", 13)).place(x=126, y=600)
    elif len(password_info) == 0:
        Label(window1,text="            Please enter a password                      ", fg="Red", bg="#c4c4c4", font=("calibri", 13)).place(x=129, y=600)
    elif len(username_info) == 0:
        Label(window1, text="            Please enter a Username                     ", fg="Red", bg="#c4c4c4", font=("calibri", 13)).place(x=129, y=600)
    elif len(cpassword_info) == 0:
        Label(window1, text="            Please confirm your password                      ", fg="Red", bg="#c4c4c4", font=("calibri", 13)).place(x=107, y=600)
    elif password_info != cpassword_info:
        Label(window1, text="            Passwords don't match                          ", fg="Red", bg="#c4c4c4", font=("calibri", 13)).place(x=129, y=600)
    else:  # if all the entry fields are completed correctly
        file = open(username_info.lower(), "w")  # username and password saved in a file named as the username
        file.write(username_info + "\n")  # separates the username and password in the file by a line
        file.write(password_info)
        file.close()
        username_entry.delete(0, END)  # deletes the entry boxes
        password_entry.delete(0, END)
        confirmpassword_entry.delete(0, END)
        Label(window1, text="                  Registration successful                       ", fg="green", bg="#c4c4c4", font=("calibri", 13)).place(x=113, y=600)
