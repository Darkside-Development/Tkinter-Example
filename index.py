import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("300x300")
window.title("Tkinter Example")

text = tk.Label(window,
                text="Tkinter Example",
                font=("COMIC Sans MS", 20))

credits = tk.Label(window,
                 text="@Darkside-Development",
                 font=("COMIC Sans MS", 12))

text.place(relx = 0.5, rely = 0.5,
           anchor='center')

credits.place(relx = 0.5, rely = 0.6,
            anchor='center')

""" ico = Image.open('iconn.ico')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo) """

window.mainloop()