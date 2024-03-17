
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Carrera Técnica\SEMESTRE 5\CRIPTOGRAFIA\programa\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("698x320")
window.configure(bg = "#7675BF")


canvas = Canvas(window,bg = "#7675BF",height = 320,width = 698,bd = 0,highlightthickness = 0,relief = "ridge")

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))

image_1 = canvas.create_image(158.0,160.0,image=image_image_1)

canvas.create_text(364.0,82.0,anchor="nw",text="Usuario:",fill="#000000",font=("Arial Black", 16 * -1))

canvas.create_text(364.0,144.0,anchor="nw",text="Contraseña:",fill="#000000",font=("Arial Black", 16 * -1))

#BOTON INICIAR SESIÓN
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,
#LLAMA A FUNCIONES CREADAS
    command=lambda: print("button_1 clicked"),relief="flat")

button_1.place(x=417.0,y=221.0,width=167.0,height=36.0)
#BOTON REGISTRARSE
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,
#LLAMA A FUNCIONES CREADAS
    command=lambda: print("button_2 clicked"),relief="flat")
button_2.place(x=417.0,y=265.0,width=167.0,height=36.0)

#NOMBRE DE LA APLICACION
canvas.create_text(406.0,44.0,anchor="nw",text="Aplicación Criptografica",fill="#000000",font=("Inter Bold", 16 * -1))

#CAMPOS DE TEXTO
#CAMPO DE TEXTO USUARIO
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(496.5,121.0,image=entry_image_1)
entry_1 = Text(bd=0,bg="#BE9DDF",fg="#000716",highlightthickness=0)
entry_1.place(x=364.0,y=103.0,width=265.0,height=34.0)

#CAMPO DE TEXTO CONTRASEÑA
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(496.5,187.0,image=entry_image_2)
entry_2 = Text(bd=0,bg="#BE9DDF",fg="#000716",highlightthickness=0)
entry_2.place(x=364.0,y=169.0,width=265.0,height=34.0
              )
window.resizable(False, False)
window.mainloop()
