from tkinter import colorchooser
from login import * # imports the login python program
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename
from login import *  # imports the login python program
import tempfile
import subprocess
import os

class main():
    def __init__(self, master):  # sets up a class for variables to be used throughout the program
        self.window = master
        self.pen_colour = "black"
        self.eraser_colour = "white"
        self.background_colour = "white"
        self.penwidth = 5
        self.current_x = None
        self.current_y = None  # sets the variables of the x and y coordinates
        self.tools()
        self.canvas.bind('<Button-1>',
                         self.find_xy)  # calls the find xy function when the left mouse button is clicked on the canvas # move to class
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

    def changebg(self):
        color = colorchooser.askcolor()  # opens the colour chooser and sets the background colour and eraser colour to this
        if color[1] == None:
            print("s")
        else:
            self.canvas.delete('all')
            self.background_colour = color[1]
            self.canvas.create_rectangle(0, 0, 1300, 800, fill=self.background_colour, outline="")
            self.eraser_colour = self.background_colour
            
    def changeb(self):
        color = colorchooser.askcolor()
        self.pen_colour = color[1]  # sets the pen colour as the colour chosen

    def clear(self):
        self.canvas.delete('all')  # clears the canvas of any drawings
        self.canvas.create_rectangle(0, 0, 1300, 800, fill=self.background_colour, outline="")

    def eraser(self):
        self.pen_colour = self.eraser_colour  # sets the pen colour to the eraser colour to put the user in eraser mode

    def tools(self):
        self.window.geometry(
            '250x200+250+200')  # This sets the dimensions of the window so that widgets can be positioned more easily and precisely

        slider = Scale(self.window, from_=100, to=1, command=self.changeW, orient=VERTICAL, length=500, relief=GROOVE,
                       bd=3,
                       activebackground="red")  # creates a scale widget to change the size of the brush. The command goes to the function changeW()
        slider.set(self.penwidth)  # sets the penwidth to the scale of that of the slider
        slider.pack(padx=25, pady=0, side=LEFT)

        black_button = Button(self.window, background="black", command=lambda: self.changePC("black"), width=12,
                              height=4)  # creates a button that when pressed sets the brush colour to the same as the buttons
        black_button.place(x=93, y=500)  # places the button at these coordinates in the window

        blue_button = Button(self.window, background="#1261A0", command=lambda: self.changePC("#1261A0"), width=12,
                             height=4)
        blue_button.place(x=233, y=500)

        red_button = Button(self.window, background="#DC1C13", command=lambda: self.changePC("#DC1C13"), width=12,
                            height=4)
        red_button.place(x=373, y=500)

        green_button = Button(self.window, background="#149414", command=lambda: self.changePC("#149414"), width=12,
                              height=4)
        green_button.place(x=93, y=650)

        pink_button = Button(self.window, background="#fe3fb3", command=lambda: self.changePC("#fe3fb3"), width=12,
                             height=4)
        pink_button.place(x=233, y=650)

        white_button = Button(self.window, background="white", command=lambda: self.changePC("white"), width=12,
                              height=4, border=1)
        white_button.place(x=373, y=650)


        self.change_bgpic = PhotoImage(file="change_bg.png")  # This sets the button to the image imported
        change_bg_button = Button(self.window, image=self.change_bgpic, command=self.changebg, width=200, height=120,
                                  border=0)  # When the button is pressed, it calls the change background function
        change_bg_button.place(x=25, y=800)

        #C:/animation program\
        #H:\Animation project\
        self.change_brushpic = PhotoImage(file="change_brush.png")
        change_brush_button = Button(self.window, image=self.change_brushpic, command=self.changeb, width=200,
                                     height=120, border=0)
        change_brush_button.place(x=260, y=800)

        self.clearpic = PhotoImage(file="clear_button.png")
        clear_button = Button(self.window, image=self.clearpic, command=self.clear, width=180, height=80,
                                     border=0)
        clear_button.place(x=93, y=360)

        self.eraserpic = PhotoImage(file="eraser_button.png")
        eraser_button = Button(self.window, image=self.eraserpic, command=self.eraser, width=180, height=80,
                                     border=0)
        eraser_button.place(x=93, y=260)

        save_button = Button(self.window, text="Save Canvas", height="7", width="16", bg="#868EA5", border=1, relief=SOLID, font=("Calibri", 15), command=self.save_canvas)
        save_button.place(x=300,y=260)

        self.canvas = Canvas(self.window, width=1200, height=750, bg="white")  # creates the canvas 1200 WIDTH
        self.canvas.pack(expand=True)  # canvas fills the entire window and expands to fill any space
        self.canvas.place(relx=1.0, rely=1.0, anchor=SE)

    def save_canvas(self):
        tempFilePath = os.path.join(tempfile.gettempdir(), "test.ps")
        FilePath = filedialog.asksaveasfile(title='Please select data directory',mode="w", defaultextension=".png", filetypes=(("png file", "*.png"),("All Files", "*.*") ))  # Asks the user where they want their picture saved
        self.canvas.postscript(file=tempFilePath, colormode="color")  # Converts the canvas to post script to be converted to a png.file
        args = "\"S:\A Level Computer Science Resources\CodeEnv\Ghostscript\gswin32c.exe\" -dSAFER -dBATCH -dNOPAUSE -dUseCropBox -sDEVICE=png16m -dGraphicsAlphaBits=4 -dEPSFitPage -sOutputFile=\"{0}\" \"{1}\"".format(FilePath.name, tempFilePath) 
         # calls ghostscript 
        subprocess.Popen(args, shell=True) 
        
        



#loginmain() # calls the main function in the login python file
window = Tk()  # This creates the main window in which my program will be situated
window.title("program")  # Names the window and configures the settings of it
window.state("zoomed")  # covers the entire screen in the window
window.config(bg="#c4c4c4")  # sets background of window to black
window.resizable(width=False, height=False)
main(window)
window.mainloop()  # loops the program



# https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/

# https://www.tutorialspoint.com/python/tk_canvas.htm
# https://github.com/nj-AllAboutCode/Python-Tkinter-Projects/blob/master/DrawingApp.py
# https://www.youtube.com/watch?v=-_mYx6SHqT8
