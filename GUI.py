"""
building the GUI for User Interaction
"""
import tkinter as tk

def button_interaction(variant=""):
    if variant == "":
        print("btn_clicked")
    elif variant == "Random Joke":
        print("Random Joke clicked")
    elif variant == "Category":
        print("Category clicked")

# basic gui setup
main_screen = tk.Tk()
main_screen.title("Witzgram")
main_screen.geometry("800x600")
# not workable pseudo code main_screen.geometry HöhexBreite

my_frame = tk.Frame(main_screen)
my_frame.grid()

# components
my_lbl_1 = tk.Label(my_frame, text="Main Menu")
# my_lbl_2 = tk.Label(my_frame, text="pls. enter sth.")
my_btn_1 = tk.Button(my_frame, text="Random Joke", command=lambda:button_interaction("ok")) # command
my_btn_2 = tk.Button(my_frame, text="Category", command=lambda:button_interaction("cancel")) # command
# my_txt_1 = tk.Text(my_frame)



# positioning
# my_txt_1.grid(row=1, column=1, columnspan=2)

my_lbl_1.grid(row=0, column=0, columnspan=3)
# my_lbl_2.grid(row=1, column=0)

my_btn_1.grid(row=1,column=1)
my_btn_2.grid(row=2,column=1)


main_screen.update()
main_screen.mainloop()
