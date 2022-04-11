f3rom tkinter import colorchooser
from tkinter import filedialog
from login import *  # imports the login python program
import tempfile
import subprocess
import os
from tkinter import messagebox


class main():
    def __init__(self, master):  # sets up a class for variables to be used throughout the program
        self.change_bgpic = PhotoImage(file="change_bg.png")  # This sets the button to the image imported
        self.clearpic = PhotoImage(file="clear_button.png")
        self.change_brushpic = PhotoImage(file="change_brush.png")
        self.eraserpic = PhotoImage(file="eraser_button.png")
        self.window = master
        self.pen_colour = "black"
        self.eraser_colour = "white"
        self.eraser_select = False
        self.background_colour = "white"
        self.penwidth = 5
        self.message_box_count = 0
        self.color = None
        self.current_x = None
        self.current_y = None  # sets the variables of the x and y coordinates
        self.tools()
        self.canvas.bind('<Button-1>',
                         self.find_xy)  # calls the find xy function when the left mouse button is clicked on the canvas
        self.canvas.bind("<B1-Motion>",
                         self.draw)  # calls the draw function when the mouse is moved with button 1 being held down(Drawing)

    def find_xy(self, event):
        self.current_x, self.current_y = event.x, event.y  # sets the current x and y coordinates

    def draw(self, event):
        self.canvas.create_line(self.current_x, self.current_y, event.x, event.y, width=self.penwidth,
                                fill=self.pen_colour, capstyle=ROUND, smooth=True)  # CREATES A LINE
        self.current_x, self.current_y = event.x, event.y

    def changeW(self, event):
        self.penwidth = event  # this sets the brush width to the same as that on the slider

    def changePC(self, color):
        self.pen_colour = color  # sets the brush colour to the same as that on the button clicked
        self.eraser_select = False

    def changebg(self):
        self.color = colorchooser.askcolor()  # opens the colour chooser menu
        if self.color[1] is None:  # if the user closes or cancels the colour chooser menu, the commands don't go ahead
            print("")
        else:
            self.clearmessage_box()  # calls the message box to confirm with the user they want to clear the canvas

    def verified_changebg(self):
        self.canvas.delete(
            'all')  # deletes everything on the canvas and sets the background and eraser colour to the user's chosen colour
        self.background_colour = self.color[1]
        self.canvas.create_rectangle(0, 0, 1300, 800, fill=self.background_colour, outline="")
        self.eraser_colour = self.background_colour
        self.message_box.destroy()
        self.message_box_count = 0
        if self.eraser_select == True:
            self.eraser()

    def clearmessage_box(self):
        if self.message_box_count == 0: # Only opens another message box if no others are already opened
            self.message_box_count = 1
            self.message_box = Toplevel(self.window)  # creates a window to act as a message box
            self.message_box.title("Warning")
            self.message_box.config(bg="#c4c4c4")
            self.message_box.geometry("400x150+100+100")
            self.message_box.resizable(width=False, height=False)
            Label(self.message_box, text="This will delete the contents of the canvas", bg="#c4c4c4",
                  font=("Calibri", 15)).pack(pady=5, side=TOP)
            Button(self.message_box, text="Okay", height="1", width="12", bg="#868EA5", border=1, relief=SOLID,
                   font=("Calibri", 13), command=lambda: self.choice(self.var.get())).pack()
            # gets the information on which button the user pressed and opens the choice function
            Button(self.message_box, text="Cancel", height="1", width="12", bg="#868EA5", border=1, relief=SOLID,
                   font=("Calibri", 13), command=self.destroy_messagebox).pack(pady=5)
            Frame(self.message_box, width=400, height=25, bg="#499292").pack(side=BOTTOM)
        else:
            self.destroy_messagebox()  # if there is a message box already open, destroy it to avoid an overload of message boxes

    def destroy_messagebox(self):
        self.message_box.destroy()
        self.message_box_count = 0

    def clear(self):
        self.canvas.delete('all')  # clears the canvas of any drawings
        self.canvas.create_rectangle(0, 0, 1300, 800, fill=self.background_colour,
                                     outline="")  # recreates the background
        self.message_box.destroy()  # destroys the message box window
        self.message_box_count = 0

    def choice(self, chosen_button):
        if chosen_button == "clear":  # depending on whether the user presses the clear or change background function, the correct function is called for the choice.
            self.clear()
        elif chosen_button == "background":
            self.verified_changebg()

    def changeb(self):
        color = colorchooser.askcolor()
        self.pen_colour = color[1]  # sets the pen colour as the colour chosen
        self.eraser_select = False

    def eraser(self):
        self.pen_colour = self.eraser_colour  # sets the pen colour to the eraser colour to put the user in eraser mode
        self.eraser_select = True

    def sign_out(self):
        answer = messagebox.askquestion("Sign out","Are you sure you want to sign out? This will end your current session.")
        if answer == "yes":  # Signs the user out if they choose to do so and sends them back to the main login screen
            self.window.destroy()
            loginmain()
            window = Tk()  # Recreates the main window
            window.title("program")  
            window.geometry('1550x800+100+50')
            window.config(bg="#c4c4c4")  
            window.resizable(width=False, height=False)
            main(window)

    def help(self):
        self.help_box = Toplevel(self.window)  # Help window
        self.help_box.title("Help")
        self.help_box.config(bg="#c4c4c4", border=1)
        self.help_box.geometry("600x700+700+150")
        self.help_box.resizable(width=False, height=False)
        Label(self.help_box, text="Help", bg="#c4c4c4", font=("Calibri", 45)).pack(side=TOP, pady=20)
        info_box = Frame(self.help_box, width=500, height=600, bg="#499292", border=1)
        info_box.pack()
        Label(info_box,
              text="- Click on a coloured button to change your brush colour \n\n - Use the slider on the left hand side of the window to      \n"
                   "adjust the size of your brush\n\n - Click the brush colour button to open up a wider variety\n of colours to use. Here you can also set custom colours \nin case you want to easily "
                   "reuse the same colour at a \nlater point.\n\n - Select the background colour button to open the colour \n chooser window and select your colour, this will change\n the colour of the entire canvas."
                   " It is recommended that \nthis is done before you start drawing as changing the \nbackground colour removes any drawing already on the\n canvas. \n\n Email our support team: Funimate.support@gmail.com"
                   "\nfor any more enquiries you may have. ",

              bg="#499292", width=50, font=("Calibri", 15)).pack(padx=10)

        Button(self.help_box, text="Close", height="2", width="25", bg="#868EA5", border=0, relief=SOLID,
               font=("Calibri", 13), command=self.help_box.destroy).pack(side=BOTTOM, pady=15)

    def tools(self):
        slider = Scale(self.window, from_=100, to=1, command=self.changeW, orient=VERTICAL, length=425, relief=GROOVE,
                       bd=3, activebackground="red")
        # creates a scale widget to change the size of the brush. The command goes to the function changeW()
        slider.set(self.penwidth)  # sets the penwidth to the scale of that of the slider
        slider.place(x=20, y=167)

        black_button = Button(self.window, background="black", command=lambda: self.changePC("black"), width=12,
                              height=4)  # creates a button that when pressed sets the brush colour to the same as the buttons
        black_button.place(x=93, y=400)  # places the button at these coordinates in the window

        blue_button = Button(self.window, background="#1261A0", command=lambda: self.changePC("#1261A0"), width=12,
                             height=4)
        blue_button.place(x=233, y=400)

        red_button = Button(self.window, background="#DC1C13", command=lambda: self.changePC("#DC1C13"), width=12,
                            height=4)
        red_button.place(x=373, y=400)

        green_button = Button(self.window, background="#149414", command=lambda: self.changePC("#149414"), width=12,
                              height=4)
        green_button.place(x=93, y=530)

        pink_button = Button(self.window, background="#fe3fb3", command=lambda: self.changePC("#fe3fb3"), width=12,
                             height=4)
        pink_button.place(x=233, y=530)

        white_button = Button(self.window, background="white", command=lambda: self.changePC("white"), width=12,
                              height=4, border=1)
        white_button.place(x=373, y=530)

        self.var = StringVar(self.window)
        self.var.set(None)
        change_bg_button = Radiobutton(self.window, image=self.change_bgpic, value="background", variable=self.var,
                                       command=self.changebg, indicatoron=0, width=200, height=120,
                                       border=0)  # When the button is pressed, it calls the change background function
        change_bg_button.place(x=25, y=650)
        # The button shares the same variable as the clear button, contains the value "background"
        
        clear_button = Radiobutton(self.window, image=self.clearpic, value="clear", variable=self.var,
                                   command=self.clearmessage_box, indicatoron=0, width=174, height=74,
                                   border=0)
        clear_button.place(x=93, y=267)

        change_brush_button = Button(self.window, image=self.change_brushpic, command=self.changeb, width=200,
                                     height=120, border=0)
        change_brush_button.place(x=260, y=650)

        eraser_button = Button(self.window, image=self.eraserpic, command=self.eraser, width=178, height=78,
                               border=0)
        eraser_button.place(x=93, y=167)

        save_button = Button(self.window, text="Save Canvas", height="7", width="16", bg="#868EA5", border=1,
                             relief=SOLID, font=("Calibri", 15), command=self.save_canvas)
        save_button.place(x=300, y=167)

        logout_button = Button(self.window, text="Sign out", height="3", width="16", bg="#499292", border=1,
                               relief=SOLID, font=("Calibri", 15), command=self.sign_out)
        logout_button.place(x=25, y=50)

        help_button = Button(self.window, text="help", height="3", width="16", bg="#499292", border=1,
                             relief=SOLID, font=("Calibri", 15), command=self.help)
        help_button.place(x=300, y=50)

        self.canvas = Canvas(self.window, width=1050, height=750, bg="white")  # creates the canvas
        self.canvas.pack(expand=True)  # canvas fills the entire window and expands to fill any space
        self.canvas.place(relx=1.0, rely=1.0, anchor=SE)

    def save_canvas(self):
        tempFilePath = os.path.join(tempfile.gettempdir(), "test.ps")
        FilePath = filedialog.asksaveasfile(title='Please select data directory', mode="w", defaultextension=".png",
                                            filetypes=(("png file", "*.png"), (
                                                "All Files",
                                                "*.*")))  # Asks the user where they want their picture saved
        self.canvas.postscript(file=tempFilePath,
                               colormode="color")  # Converts the canvas to post script to be converted to a png.file
        args = "\"C:\Ghostscript\gswin32c.exe\" -dSAFER -dBATCH -dNOPAUSE -dUseCropBox -sDEVICE=png16m -dGraphicsAlphaBits=4 -dEPSFitPage -sOutputFile=\"{0}\" \"{1}\"".format(
            FilePath.name, tempFilePath)  # calls ghostscript
        subprocess.Popen(args, shell=True)
        #S:\A Level Computer Science Resources\CodeEnv\Ghostscript\gswin32c.exe

loginmain()  # calls the main function in the login python file
window = Tk()  # This creates the main window in which my program will be situated
window.title("program")  # Names the window and configures the settings of it
window.geometry('1550x800+100+50')
# This sets the dimensions of the window and the position that it opens up on the display
window.config(bg="#c4c4c4")  # sets background of window to black
window.resizable(width=False, height=False)
main(window)
conn.commit()
window.mainloop()  # loops the program
conn.close()
