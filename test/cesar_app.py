
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"images/cesar")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("686x336")
window.configure(bg = "#4AFF9D")


canvas = Canvas(
    window,
    bg = "#4AFF9D",
    height = 336,
    width = 686,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    343.0,
    108.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=145.0,
    y=94.0,
    width=396.0,
    height=27.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    342.5,
    288.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=159.0,
    y=274.0,
    width=367.0,
    height=27.0
)

canvas.create_text(
    64.0,
    20.0,
    anchor="nw",
    text="CIFRADO CESAR ",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    201.0,
    58.0,
    anchor="nw",
    text="Texto Plano/Encriptado",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    89.0,
    138.0,
    anchor="nw",
    text="Alfabeto",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    399.0,
    138.0,
    anchor="nw",
    text="Desplazamiento",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    501.5,
    188.5,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=374.0,
    y=174.0,
    width=255.0,
    height=27.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    140.0,
    188.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=41.0,
    y=174.0,
    width=198.0,
    height=27.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=346.0,
    y=230.0,
    width=180.0,
    height=29.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=159.0,
    y=230.0,
    width=150.0,
    height=29.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=584.0,
    y=178.0,
    width=26.0,
    height=22.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=201.0,
    y=178.0,
    width=26.0,
    height=22.0
)
window.resizable(False, False)
window.mainloop()
