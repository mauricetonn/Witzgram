"""
GUI to interakt with the User

    author: Simon Klingler / Maurice Tonn
    date: 31.05.2022
    version: 0.0.1
    license: free
"""

import tkinter as tk
from PIL import Image, ImageTk
import JokeAPI 
import DatabaseAPI

# variables to handle the acces to same jokes at different places
try:
    _current_joke = "Joke Of The Day:\n " # + JokeAPI.get_jod().replace("'", "´").replace("\n","") # only 10 Times per Hour!!!
    _current_category = "Joke Of The Day"
    print(_current_joke)
except:
    print("Maximum Amount of API-Request per Hour Reached. Joke is now random")
    current = JokeAPI.get_joke()
    _current_joke = current[0]
    _current_category = current[1]

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
    Tests:
        1) get_joke() while in "Favorites" should set Joke from the Database as _current_joke
        2) get_joke() while not in "Favorites" should set Joke from API as _current_joke
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

def submit_joke_db():
    """
        Submitts Joke to DB
    Test:
        1) Place Text in GUI -> set Category -> Submit -> Joke should be in Database
    """
    DatabaseAPI.add_joke(joke = my_entry_own_joke.get(), category=clicked_submit.get())
def submit_joke_api():
    """
    Submitts Joke to JokeAPI

    Test: 
        1) Submit from GUI -> look at printed response -> error? (Server was disabled at 02.06.22)
    """
    JokeAPI.submit_joke(category=clicked_submit.get(), joke=my_entry_own_joke.get(), nsfw=nsfw.get(),
     religious=religious.get(), political=political.get(), racist=racist.get(), sexist=sexist.get(), explicit=explicit.get(), language = "en")

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
            pass
        else:
            DatabaseAPI.like_dekrement(joke = _current_joke, category = _current_category, likes = _current_likes)
            if _current_likes == 1:
                _favorites_rank -= 1
            get_joke()
            change_background()
            
    elif variant == "like":
        print("like clicked")
        if clicked.get() != "Favorites":
            DatabaseAPI.add_joke(joke = _current_joke, category = _current_category)
        else:
            DatabaseAPI.like_inkrement(joke = _current_joke, category = _current_category, likes = _current_likes)
        get_joke()
        change_background()
    elif variant == "Next":
        print("Next")
        get_joke()
        change_background()
    elif variant == "Submit":
        print("Submit clicked")
        submit_joke_db()
        submit_joke_api()
    elif variant == "exit":
        DatabaseAPI.db_commit()
        main_window.quit()

def __CancelCommand(event=None):
    """
    A Command that does nothing
    Test:
        1) Press normal Exit Button -> Nothing happens
    """
    pass

# gui setup
main_window = tk.Tk()
main_window.title("Witzgram")
main_window.geometry("800x400")

main_window.minsize(800, 400)
main_window.maxsize(800, 400)

# beim drücken des X-Knopfes oben rechts passiert nichts
main_window.protocol('WM_DELETE_WINDOW', __CancelCommand)

my_frame = tk.Frame(main_window)
my_frame.place(x=0, y=0, width=800, height=400)
# devide main-frame into subframes
# get Joke Subframe:
my_get_joke_subframe = tk.Frame(my_frame)
my_get_joke_subframe.place(x=0, y=0, width=625, height=160)
# submit Joke Subframe
my_submit_joke_subframe = tk.Frame(my_frame)
my_submit_joke_subframe.place(x=0, y=210, width=800, height=100)
# Checkbox Subframe
my_cb_subframe = tk.Frame(my_submit_joke_subframe)
my_cb_subframe.grid(row=1, column=1)

# Basic DropDown-Setup by https://www.geeksforgeeks.org/dropdown-menus-tkinter/
# Dropdown menu options 
options = [
    "Any", "Misc", "Programming", "Dark", "Pun", "Spooky", "Christmas", "Favorites"
]
options_submit = [
    "Misc", "Programming", "Dark", "Pun", "Spooky", "Christmas"
]
# datatype of menu text
clicked = tk.StringVar()
clicked_submit = tk.StringVar()
  
# initial menu text
clicked.set( "Any" )
clicked_submit.set("Misc")

# Create Dropdown menu
#drop = tk.OptionMenu(my_get_joke_subframe , clicked , *options)
drop = tk.OptionMenu(my_frame , clicked , *options)
drop_submit = tk.OptionMenu(my_submit_joke_subframe, clicked_submit, *options_submit)

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

my_label_joke  = tk.Label(my_get_joke_subframe, text=_current_joke, width=50, height = 7, wraplength=400)
my_btn_like = tk.Button(my_get_joke_subframe, text="like", command=lambda:button_interaction("like"))
my_btn_dislike = tk.Button(my_get_joke_subframe, text="dislike", command=lambda:button_interaction("dislike")) 
my_btn_next = tk.Button(my_get_joke_subframe, text="Next", command=lambda:button_interaction("Next")) 
my_btn_submit = tk.Button(my_submit_joke_subframe, text="Submit", command=lambda:button_interaction("Submit"))
#my_btn_exit = tk.Button(my_frame, text="exit", command=main_window.quit)
my_btn_exit = tk.Button(my_frame, text="exit", command=lambda:button_interaction("exit"))

# my_label_input = tk.Label( my_frame , text = " ")
my_label_own_joke = tk.Label(my_submit_joke_subframe, text="Submit your own Joke: ")
my_entry_own_joke = tk.Entry(my_submit_joke_subframe, bd=5, width=40)

# CheckBoxes
nsfw = tk.BooleanVar()
religious = tk.BooleanVar()
political = tk.BooleanVar()
racist = tk.BooleanVar()
sexist = tk.BooleanVar()
explicit = tk.BooleanVar()

my_cb_nsfw = tk.Checkbutton(my_cb_subframe, variable=nsfw, text="NSFW", onvalue=True, offvalue=False)
my_cb_religious = tk.Checkbutton(my_cb_subframe, variable=religious, text="Religious", onvalue=True, offvalue=False)
my_cb_political = tk.Checkbutton(my_cb_subframe, variable=political, text="Political", onvalue=True, offvalue=False)
my_cb_racist = tk.Checkbutton(my_cb_subframe, variable=racist, text="Racist", onvalue=True, offvalue=False)
my_cb_sexist = tk.Checkbutton(my_cb_subframe, variable=sexist, text="Sexist", onvalue=True, offvalue=False)
my_cb_explicit = tk.Checkbutton(my_cb_subframe, variable=explicit, text="Explicit", onvalue=True, offvalue=False)

# positioning
# Background:
panel.place(x=0, y=0, width=800, height=400)
panel.lower()
# Get Joke:
drop.place(x=665, y=15)
my_label_joke.grid(row=0, column=1)
my_btn_like.grid(row=1, column=0)
my_btn_next.grid(row=1, column=1)
my_btn_dislike.grid(row=1, column=2)
# Submit Joke:
my_label_own_joke.grid(row=0, column=0)
my_entry_own_joke.grid(row=0,column=1)
my_btn_submit.grid(row=2, column=1)
drop_submit.grid(row = 0, column=2, padx=90)
# Checkboxes
my_cb_nsfw.grid(row=0, column=0)
my_cb_religious.grid(row=0, column=1)
my_cb_political.grid(row=0, column=2)
my_cb_racist.grid(row=0, column=3)
my_cb_sexist.grid(row=0, column=4)
my_cb_explicit.grid(row=0, column=5)
# Main
my_btn_exit.place(x=380, y = 360)

main_window.update()
main_window.mainloop()