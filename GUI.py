"""
Gui to interakt with the User

    author: Simon Klingler
    date: 31.05.2022
    version: 0.0.1
    license: free
"""

import tkinter as tk
from PIL import Image, ImageTk
import JokeAPI 
import DatabaseAPI

# variables to handle the acces to same jokes at different places
_current_joke = JokeAPI.get_joke("Any")[0]
_current_category = JokeAPI.get_joke("Any")[1]
_current_likes = 0
_favorites_rank = 0

def set_new_api_current():
    """
    Function to get new Values for _current_joke and _current_category from JokeAPI

    Test:
        1) calling set_new_api_current should change _current_joke and _current_category
    """
    global _current_joke, _current_category
    current = JokeAPI.get_joke(clicked.get())
    _current_joke = current[0]
    _current_category = current[1]

def set_new_db_current(rank):
    """
    Function to get new Values for _current_joke, _current_category, _current_likes from DatabaseAPI

    Args:
        rank (int): list index of joke array
    Test:
        1) rank(0) should set _current_joke, _current_category, _current_likes to the dataset with the highest likes number
        2) rank(-1) should set _current_joke, _current_category, _current_likes to the dataset with the lowest likes number
    """
    global _current_joke, _current_category, _current_likes
    current = DatabaseAPI.get_jokes(rank=rank)
    _current_joke = current[0]
    _current_category = current[1]
    _current_likes = current[2]

def change_background():
    """
    Changes the panel.image to the fitting image for the current category

    Test:
        1) Change Category -> New Joke -> Background should change
    """
    if clicked.get() == "Any":
        img = ImageTk.PhotoImage(background_image_Any)
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
    elif clicked.get() == "Favorites":
        img = ImageTk.PhotoImage(background_image_Favorites)
    else:
        img = ImageTk.PhotoImage(background_image_Any)
    panel.configure(image = img)         
    panel.image = img

def get_joke():
    """
    Handles DatabaseAPI / JokeAPI interaction to change current Joke depending on current category
    """
    global _favorites_rank, _current_category
    if clicked.get() != "Favorites":
        set_new_api_current()
        _favorites_rank = 0
    else:
        if _current_category == "EOF" or _current_category == 'EOF':
            _favorites_rank = 0
        set_new_db_current(_favorites_rank)
        _favorites_rank += 1
    my_label_joke.configure(text = _current_joke)

def button_interaction(variant=""):
    """
    Handles the different Button Interactions
    Args:
        variant (str, optional): Changes behavior depending on clicked button. Defaults to "".
    Test:
        1) Press any Button -> Corresponding Control prompt should be printed
    """
    global _favorites_rank
    if variant == "":
        print("btn_clicked -> Well this shouldnt have happend")
    elif variant == "dislike":
        print("dislike clicked")
        if clicked.get() != "Favorites":
            pass                         # since you didnt like it
        else:
            DatabaseAPI.like_dekrement(joke = _current_joke, category = _current_category, likes = _current_likes)
    elif variant == "like":
        print("like clicked")
        if clicked.get() != "Favorites":
            DatabaseAPI.add_joke(joke = _current_joke, category = _current_category)
        else:
            DatabaseAPI.like_inkrement(joke = _current_joke, category = _current_category, likes = _current_likes)
    elif variant == "Next":
        print("Next")
        get_joke()
        change_background()
    elif variant == "Submit":
        print("Submit clicked")
        
        


# gui setup
main_window = tk.Tk()
main_window.title("Witzgram")
main_window.geometry("800x400")

main_window.minsize(800, 400)
main_window.maxsize(800, 400)

my_frame = tk.Frame(main_window)
my_frame.place(width=800, height=400)

# Basic DropDown-Setup by https://www.geeksforgeeks.org/dropdown-menus-tkinter/
# Dropdown menu options 
options = [
    "Any", "Misc", "Programming", "Dark", "Pun", "Spooky", "Christmas", "Favorites"
]
  
# datatype of menu text
clicked = tk.StringVar()
  
# initial menu text
clicked.set( "Any" )

# Create Dropdown menu
drop = tk.OptionMenu(my_frame , clicked , *options)

# Images
background_image_Any = Image.open('images/Fragezeichen.png').resize((800, 400))
background_image_Misc = Image.open('images/misc.png').resize((800, 400))
background_image_Programming = Image.open('images/programming1.jpg').resize((800, 400))
background_image_Dark = Image.open('images/dark.jpg').resize((800, 400))
background_image_Pun = Image.open('images/pun.png').resize((800, 400))
background_image_Spooky = Image.open('images/Spooky.jpg').resize((800, 400))
background_image_Christmas = Image.open('images/Christmas.jpg').resize((800, 400))
background_image_Favorites = Image.open('images/favorites.jpeg').resize((800, 400))

# Basic Label Background SetUp by https://www.educba.com/tkinter-background-image/
# PhotoImage class is used to add image to widgets, icons etc
img = ImageTk.PhotoImage(background_image_Any)

# create Background label
panel = tk.Label(my_frame, image = img)

# components

my_label_joke  = tk.Label(my_frame, text=_current_joke, wraplength=400 )
my_btn_like = tk.Button(my_frame, text="like", command=lambda:button_interaction("like"))
my_btn_dislike = tk.Button(my_frame, text="dislike", command=lambda:button_interaction("dislike")) 
my_btn_next = tk.Button(my_frame, text="Next", command=lambda:button_interaction("Next")) 
my_btn_submit = tk.Button(my_frame, text="Submit", command=lambda:button_interaction("Submit"))
my_btn_exit = tk.Button(my_frame, text="exit", command=main_window.quit)
# my_label_input = tk.Label( my_frame , text = " ")
my_label_own_joke = tk.Label(my_frame, text="Submit your own Joke: ")
my_entry_own_joke = tk.Entry(my_frame, bd=5, width=40)

# positioning
panel.place(x=0, y=0, width=800, height=400)
panel.lower()
drop.grid(row=0, column=1, pady = 10)
my_label_joke.grid(row=0, column=2, pady=20)
my_btn_like.grid(row=1, column=1, pady=10)
my_btn_next.grid(row=1, column=2, pady=10)
my_btn_dislike.grid(row=1, column=3, pady=10)
my_label_own_joke.grid(row=2, column=1, pady = 10)
my_entry_own_joke.grid(row=2,column=2, pady = 10)
my_btn_submit.grid(row=3, column=2)

my_btn_exit.grid(row=10, column=2)

main_window.update()
main_window.mainloop()