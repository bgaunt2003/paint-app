from tkinter import *
import sys
import os
from DatabaseSQL import* # imports the SQL database to store user logins

sqlite3.connect("database.db")

def loginmain():
    
    global Lwindow # global variable is created so the variable can be used throughout the program in any function
    Lwindow = Tk()  # Creates a window and configures it
    Lwindow.title("Log in")
    Lwindow.config(bg="#c4c4c4")
    Lwindow.geometry("1100x700+350+150")
    Lwindow.resizable(width=False, height=False)  # The user is unable to resize the window so the widgets don't get moved around
    # global variables for the username and password variables creates as it's useful to use these throughout the program
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    Lwindow.protocol("WM_DELETE_WINDOW", close_window)  # if the window is closed, calls function, the program ends
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
    register_link.bind("<Button-1>", lambda e: registerwindow()) # Makes the text a hyperlink so when pressed it acts as a button

    Lwindow.mainloop()

def close_window():
    sys.exit("User closed program")  # closes the window with the message

def delete2(message):
    if message == "Login Success":
        message_box.destroy()
        Lwindow.destroy()  # Destroys the message box and the login window if its successful so that the main program can run
    else:
        message_box.destroy()  # only gets rid of the message box if the login is unsuccessful
        
def message_window(message):
    global message_box
    message_box = Toplevel(Lwindow)  # creates a window to act as a message box
    message_box.title("Validation Error")
    message_box.config(bg="#c4c4c4")
    message_box.geometry("400x170")
    message_box.resizable(width=False, height=False)
    Label(message_box, text=message, bg="#c4c4c4", font=("Calibri", 20)).pack(pady=5, side=TOP)  # displays the message depending on the result
    if message == "Password has not been recognised":
        Label(message_box, text="Reminder: passwords are case sensitive", bg="#c4c4c4", font=("Calibri", 10)).pack(side=TOP) # displays an extra message if the password has not been recognised
    if message == "Login Success":
       message_box.overrideredirect(1)  # The user is not allowed to close the successful login message box as this will create confusion for the program
    Button(message_box, text="Okay", height="1", width="12", bg="#868EA5", border=1, relief=SOLID, font=("Calibri", 13), command=lambda: delete2(message)).pack()
    Frame(message_box, width=400, height=25, bg="#499292").pack(side=BOTTOM)
    if message == "Login Success":
        Lwindow.withdraw()  # Hides the main login window so the user can no longer enter any information if they have successfully logged in
    else:
        message_box.after(9000, message_box.destroy)  
        # The message box's are destroyed after a certain time if the user hasn't closed them themselves to avoid an overload of messageboxes


def login_user():
    username1 = username_verify.get().lower()  # Sets the variable as the text in the username entry box after the login button is pressed
    password1 = password_verify.get()
    c.execute("SELECT * FROM user_logins") # extracts everything from database
    d = c.fetchall()  # stores database contents in variable d
#    if len(d) == 0:
    for i in range(len(d)):  # checks all the items in the login database to see if the username exists
        if username1 == d[i][0]:  # if the username and password are in the logins database then login success
            if password1 == d[i][1]: 
                message = "Login Success"
                message_window(message)  # calls the message window function with the message variable that differs depending on result
                return
            else:  
                message = "Password has not been recognised"
                password_entry1.delete(0, END)
                message_window(message)
                return
    message = "User not found"  # The user is not found once all the credentials in the database have been checked
    username_entry1.delete(0, END)  # Deletes the contents of the entry boxes
    password_entry1.delete(0, END)
    message_window(message)  
    return

def registerwindow():
    #sets global variables
    global window1
    global username
    global password
    global cpassword
    global username_entry
    global password_entry
    global confirmpassword_entry
    window1 = Toplevel(Lwindow)
    window1.title("Register")
    window1.config(bg="#c4c4c4")
    window1.geometry("530x650+250+200")
    window1.resizable(width=False, height=False)

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
    c.execute("SELECT * FROM user_logins")
    d = c.fetchall()
    print(d)
    p = (username_info, password_info)
     
    for i in range(len(d)):
        if username_info == d[i][0]:  # checks to see if an account with the username has already been created
            Label(window1, text="This username has already been taken   ", fg="Red", bg="#c4c4c4", font=("calibri", 13)).place(x=126, y=600)
            return
    # error handling // Checks what entry boxes have information in when the button is clicked and display a message depending on the result
    if len(password_info) == 0 and len(username_info) == 0:
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
        c.execute("INSERT INTO user_logins VALUES (?,?)", p)  # adds the entered username and password to the database
        username_entry.delete(0, END)  # deletes the entry boxes
        password_entry.delete(0, END)
        confirmpassword_entry.delete(0, END)
        Label(window1, text="                  Registration successful                       ", fg="green", bg="#c4c4c4", font=("calibri", 13)).place(x=113, y=600)
    c.execute("SELECT * FROM user_logins")
    conn.commit() # Makes sure contents pusehed to database