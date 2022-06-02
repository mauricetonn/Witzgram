"""
Gui to interakt with the User

    author: Simon Klingler
    date: 31.05.2022
    version: 0.0.1
    license: free
"""

from cgitb import text
import tkinter as tk
from PIL import Image, ImageTk
from turtle import width
import JokeAPI 
import DatabaseAPI

def current():
    joke_array = JokeAPI.get_joke(clicked.get())
    return joke_array
def button_interaction(variant=""):
    if variant == "":
        print("btn_clicked")
    elif variant == "disliked":
        print("disliked clicked")
    elif variant == "liked":
        print("liked clicked")
        DatabaseAPI.add_joke(joke = current()[0], category = current()[1])
    elif variant == "newJoke":
        my_witz.configure(text = current()[0])
        if clicked.get() == "Any":
            img = ImageTk.PhotoImage(background_image_any)
        elif clicked.get() == "Misc":
            img = ImageTk.PhotoImage(background_image_Misc)
        elif clicked.get() == "Programming":
            img = ImageTk.PhotoImage(background_image_Programming)
        elif clicked.get() == "Dark":
            img = ImageTk.PhotoImage(background_image_Dark)
        elif clicked.get() == "Pun":
            img = ImageTk.PhotoImage(background_image_Pun)
        elif clicked.get() == "Spooky":
            img = ImageTk.PhotoImage(background_image_Spooky)
        elif clicked.get() == "Christmas":
            img = ImageTk.PhotoImage(background_image_Christmas)
        panel.configure(image = img)         
        panel.image = img
    elif variant == "myownJoke":
        print("myownJoke clicked")
        


# gui setup
main_window = tk.Tk()
main_window.title("Witzgram")
main_window.geometry("800x400")

main_window.minsize(800, 400)
main_window.maxsize(800, 400)

# images 

#background_image_kategory = tk.PhotoImage(file="C:\DHBW\Theorie Semester 4\Programmieren mit Python B\Projekt\Witzgram\images\Fragezeichen.png") 
#background_label = tk.Label(main_window, image=background_image_kategory)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)  # bild als Hintergrund eifügen 

my_frame = tk.Frame(main_window)
my_frame.place(width=800, height=400)

# Dropdown menu options
options = [
    "Any", "Misc", "Programming", "Dark", "Pun", "Spooky", "Christmas"
]
  
# datatype of menu text
clicked = tk.StringVar()
  
# initial menu text
clicked.set( "Any" )

# Create Dropdown menu
drop = tk.OptionMenu(my_frame , clicked , *options)

# Images
background_image_any = Image.open('images/Fragezeichen.png').resize((800, 400))
background_image_Misc = Image.open('images/misc.png').resize((800, 400))
background_image_Programming = Image.open('images/programming1.jpg').resize((800, 400))
background_image_Dark = Image.open('images/dark.jpg').resize((800, 400))
background_image_Pun = Image.open('images/pun.png').resize((800, 400))
background_image_Spooky = Image.open('images/Spooky.jpg').resize((800, 400))
background_image_Christmas = Image.open('images/Christmas.jpg').resize((800, 400))

# PhotoImage class is used to add image to widgets, icons etc
img = ImageTk.PhotoImage(background_image_any)

# create Background label
panel = tk.Label(my_frame, image = img)

# components

my_witz  = tk.Label(my_frame, text=JokeAPI.get_joke()[0], wraplength=400 )
my_btn_1 = tk.Button(my_frame, text="liked", command=lambda:button_interaction("liked"))
my_btn_2 = tk.Button(my_frame, text="disliked", command=lambda:button_interaction("disliked")) 
my_btn_3 = tk.Button(my_frame, text="neuer Witz", command=lambda:button_interaction("newJoke")) 
my_btn_4 = tk.Button(my_frame, text="Witz erstellen", command=lambda:button_interaction("myownJoke"))
my_btn_5 = tk.Button(my_frame, text="exit", command=main_window.quit)
label = tk.Label( my_frame , text = " ")

my_label = tk.Label(my_frame, text="Gib deinen eigenen Witz ein: ")
input = tk.Entry(my_frame, bd=5, width=40)

 


# und dann für jedes Image ein Label erstellen:
# background_label = tk.Label(my_frame, image=background_image_any)
# background_label = tk.Label(my_frame, image=background_image_Misc)
# background_label = tk.Label(my_frame, image=background_image_Programming)
# background_label = tk.Label(my_frame, image=background_image_Dark)
# background_label = tk.Label(my_frame, image=background_image_Pun)
# background_label = tk.Label(my_frame, image=background_image_Spooky)
# background_label = tk.Label(my_frame, image=background_image_Christmas)


# positioning
# my_witz.grid(row=1, column=2, columnspan=2)
panel.place(x=0, y=0, width=800, height=400)
panel.tkraise()

my_witz.grid(row=0, column=2, pady=20)
my_witz.tkraise()
my_btn_1.grid(row=1, column=1, pady=10)
my_btn_1.tkraise()
my_btn_2.grid(row=1, column=3, pady=10)
my_btn_2.tkraise()
my_btn_3.grid(row=2, column=2, pady=10)
my_btn_3.tkraise()
my_label.grid(row=3, column=1, pady=10)
my_label.tkraise()
input.grid(row=3,column=2)
input.tkraise()
my_btn_4.grid(row=4, column=2)
my_btn_4.tkraise()
drop.grid(row=0, column=1, pady = 10)
drop.tkraise()
my_btn_5.grid(row=10, column=2)
my_btn_5.tkraise()

main_window.update()
main_window.mainloop()