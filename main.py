from changing import changing
from search import search
from plot import plot
from signup import signup
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename

root = tk.Tk()

# configure the root window
root.geometry('700x500')
root.resizable(False, False)
root.title('project')
root.eval('tk::PlaceWindow . center')
# ttk.Button(root, text='sign up', command=signup).pack()
frame = Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
ttk.Button(root, text='signup person', command=signup).pack()
ttk.Button(root, text='search person', command=search).pack()
ttk.Button(root, text='create plot', command=plot).pack()
ttk.Button(root, text='update info', command=changing).pack()

# Create an object of tkinter ImageTk
try:
    img = ImageTk.PhotoImage(Image.open("index.png"))
    label = Label(frame, image=img)
    label.pack()
except:
    showerror(title='نبود فایل',message='فایل مربوط به عکس وجود ندارد لطفا آن را وارد کنید')
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    if filename:
        img = ImageTk.PhotoImage(Image.open(filename))
        label = Label(frame, image=img)
        label.pack()
    else:
        showerror(title='نبود فایل', message='فایل پیدا نشد ')


# Create a Label Widget to display the text or Image


# buttons to open pages

root.mainloop()
