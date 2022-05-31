"""
Gui to interakt with the User

    author: Simon Klingler
    date: 31.05.2022
    version: 0.0.1
    license: free
"""

import tkinter as tk

def button_interaction(variant=""):
    if variant == "":
        print("btn_clicked")
    elif variant == "disliked":
        print("disliked clicked")
    elif variant == "liked":
        print("liked clicked")
    elif variant == "newJoke":
        print("newJoke clicked")
    elif variant == "myownJoke":
        print("myownJoke clicked")



# gui setup
main_window = tk.Tk()
main_window.title("Witzgram")
main_window.geometry("600x400")

my_frame = tk.Frame(main_window)
my_frame.grid()

# components
my_witz  = tk.Label(my_frame, text="Witz: BLABLABLABLABLABLABLABLABLABLABLABLABLA")
my_btn_1 = tk.Button(my_frame, text="liked", command=lambda:button_interaction("liked"))
my_btn_2 = tk.Button(my_frame, text="disliked", command=lambda:button_interaction("disliked")) 
my_btn_3 = tk.Button(my_frame, text="neuer Witz", command=lambda:button_interaction("newJoke")) 
my_btn_4 = tk.Button(my_frame, text="Witz erstellen", command=lambda:button_interaction("myownJoke"))
my_btn_5 = tk.Button(my_frame, text="exit", command=main_window.quit)

my_label = tk.Label(my_frame, text="Gib deinen eigenen Witz ein: ")
input = tk.Entry(my_frame, bd=5, width=40)



# positioning
# my_witz.grid(row=1, column=2, columnspan=2)
my_witz.grid(row=0, column=2, pady=20)
my_btn_1.grid(row=1, column=1, pady=10)
my_btn_2.grid(row=1, column=3, pady=10)
my_btn_3.grid(row=2, column=2, pady=10)
my_label.grid(row=3, column=1, pady=10)
input.grid(row=3,column=2)
my_btn_4.grid(row=4, column=2)



my_btn_5.grid(row=10, column=2)



main_window.update()
main_window.mainloop()