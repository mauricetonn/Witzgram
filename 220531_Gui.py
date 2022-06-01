"""
Gui to interakt with the User

    author: Simon Klingler
    date: 31.05.2022
    version: 0.0.1
    license: free
"""

from cgitb import text
import tkinter as tk
from turtle import width
import JokeAPI 

def button_interaction(variant=""):
    if variant == "":
        print("btn_clicked")
    elif variant == "disliked":
        print("disliked clicked")
    elif variant == "liked":
        print("liked clicked")
    elif variant == "newJoke":
        my_witz.configure(text= JokeAPI.get_joke(clicked.get())[0])
    elif variant == "myownJoke":
        print("myownJoke clicked")

def show():
    label.config( text = clicked.get())
  

# gui setup
main_window = tk.Tk()
main_window.title("Witzgram")
main_window.geometry("800x400")

main_window.minsize(800, 400)
main_window.maxsize(800, 400)

my_frame = tk.Frame(main_window)
my_frame.grid()

# Dropdown menu options
options = [
    "Any", "Misc", "Programming", "Dark", "Pun", "Spooky", "Christmas"
]
  
# datatype of menu text
clicked = tk.StringVar()
  
# initial menu text
clicked.set( "Any" )

# Create Dropdown menu
drop = tk.OptionMenu(my_frame , clicked , *options )
drop.grid(row=0, column=0, pady = 10)

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

# images (Müssen noch heruntergeladen werden, am besten ist ein Ordner in diesem Projekt der images heißt oder so)

#background_image_kategory = tk.PhotoImage(file=path_to_image) # beliebiger Pfad zu einem Bild !!! PFAD NOCH NICHT EINGEFÜGT !!!
#background_label = tk.Label(my_frame, image=background_image_kategory)

   # oder man kann für jede Kategory ein Hintergrund erstellen:
# background_image_any = tk.PhotoImage(file=path_to_image)
# background_image_Misc = tk.PhotoImage(file=path_to_image)
# background_image_Programming = tk.PhotoImage(file=path_to_image)
# background_image_Dark = tk.PhotoImage(file=path_to_image)
# background_image_Pun = tk.PhotoImage(file=path_to_image)
# background_image_Spooky = tk.PhotoImage(file=path_to_image)
# background_image_Christmas = tk.PhotoImage(file=path_to_image)

# und dan für jedes Image ein Label erstellen:
# background_label = tk.Label(my_frame, image=background_image_any)
# background_label = tk.Label(my_frame, image=background_image_Misc)
# background_label = tk.Label(my_frame, image=background_image_Programming)
# background_label = tk.Label(my_frame, image=background_image_Dark)
# background_label = tk.Label(my_frame, image=background_image_Pun)
# background_label = tk.Label(my_frame, image=background_image_Spooky)
# background_label = tk.Label(my_frame, image=background_image_Christmas)


# positioning
# my_witz.grid(row=1, column=2, columnspan=2)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)  # bild als Hintergrund eifügen !!! NOCH NICHT GETEStET!!!
my_witz.grid(row=0, column=2, pady=20)
my_btn_1.grid(row=1, column=1, pady=10)
my_btn_2.grid(row=1, column=3, pady=10)
my_btn_3.grid(row=2, column=2, pady=10)
my_label.grid(row=3, column=1, pady=10)
input.grid(row=3,column=2)
my_btn_4.grid(row=4, column=2)
drop.grid(row=0, column=1, pady = 10)

my_btn_5.grid(row=10, column=2)



main_window.update()
main_window.mainloop()