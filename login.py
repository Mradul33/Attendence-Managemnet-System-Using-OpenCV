
from pathlib import Path
import os

# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./asset")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def login():
    #getting form data
    uname=entry_1.get()
    pwd=entry_2.get()
    #applying empty validation
    if uname=='' or pwd=='':
       messagebox.showinfo("Message", "Fill the fields")
    else:
       if uname=="admin" and pwd=="admin":
            messagebox.showinfo("Message", "Login Success")
            window.destroy()
            import dashboard
            exit()
       else:
            messagebox.showinfo("Message", "Try Again")


window = Tk()
window.title("Mradul test3")

window.geometry("862x519")
window.configure(bg = "#FF0000")


canvas = Canvas(
    window,
    bg = "#3A7FF6",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    450,
    0.0,
    861.9999999999999,
    519.0,
    fill="#FCFCFC",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("login.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_1.place(
    x=547.9999999999999,
    y=324.0,
    width=180.0,
    height=55.0
)

canvas_text=canvas.create_text(
    39.999999999999886,
    127.0,
    anchor="nw",
    text="",
    fill="#FCFCFC",
    font=("Courier 24 bold")
    )
head_string = "Welcome To\n\nAttendance Managemnet\nSystem Using\nOpen CV"
#Time delay between chars, in milliseconds
delta = 70
delay = 0
for i in range(len(head_string) + 1):
    s = head_string[:i]
    update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
    canvas.after(delay, update_text)
    delay += delta


canvas.create_text(
    481.9999999999999,
    74.0,
    anchor="nw",
    text="Enter login ID.",
    fill="#505485",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_rectangle(
    39.999999999999886,
    160.0,
    99.99999999999989,
    165.0,
    fill="#FCFCFC",
    outline="")

def temp1_text(e):
   entry_1.delete(0,"end")
def temp2_text(e):
   entry_2.delete(0,"end")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    650.4999999999999,
    167.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_1.insert(0, "Enter the Email")
entry_1.bind("<FocusIn>", temp1_text)
entry_1.place(
    x=489.9999999999999,
    y=137.0,
    width=321.0,
    height=59.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_2 = canvas.create_image(
    650.4999999999999,
    248.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_2.insert(0, "Enter the Password")
entry_2.bind("<FocusIn>", temp2_text)
entry_2.place(
    x=489.9999999999999,
    y=218.0,
    width=321.0,
    height=59.0
)
window.resizable(False, False)
window.mainloop()