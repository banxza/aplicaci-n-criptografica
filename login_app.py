from tkinter import Tk, Canvas, Button, PhotoImage, Text
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Toplevel, Frame
import login_backend
from tkinter import messagebox
from tkinter import Toplevel, Label, Button, Radiobutton, StringVar , Label, Radiobutton, Button, StringVar
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Toplevel, Frame, Radiobutton, StringVar, messagebox
from aes_app2 import AESApp
import cesar_backend
from cesar_app import CaesarCipherApp

class LoginApp:
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.roles_usuario = []
        self.setup_ui()
    def relative_to_assets(self, path: str) -> Path:
        # Definición de relative_to_assets antes de su uso en setup_ui
        return Path(__file__).parent / Path("assets", path)
    def setup_ui(self):
        self.root.geometry("698x320")
        self.root.configure(bg="#7675BF")
        self.root.title("Aplicación criptografica de encriptación")
        self.root.resizable(False, False)
        
        self.canvas = Canvas(self.root,bg="#7675BF",height=320,width=698,bd=0,highlightthickness=0,relief="ridge")        
        self.canvas.place(x=0, y=0)
        self.assets_path = Path(__file__).parent / Path("images/login")
        image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(158.0, 160.0, image=image_image_1)
        
        
        self.canvas.create_text(364.0, 82.0, anchor="nw", text="Usuario:", fill="#000000", font=("Arial Black", 16 * -1))
        self.canvas.create_text(364.0, 144.0, anchor="nw", text="Contraseña:", fill="#000000", font=("Arial Black", 16 * -1))

        # Botón Iniciar Sesión
        button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=self.on_login_click,relief="flat")
        button_1.place(x=417.0, y=221.0, width=167.0, height=36.0)
        button_1.image = button_image_1  # Guardar referencia de la imagen
        #NOMBRE DE LA APLICACION
        self.canvas.create_text(406.0,44.0,anchor="nw",text="Aplicación Criptografica",fill="#000000",font=("Arial Black", 16 * -1))


        # Campos de texto
        entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(496.5, 121.0, image=entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#BE9DDF", highlightthickness=0)
        self.entry_1.place(x=364.0, y=103.0, width=265.0, height=34.0)

        entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.canvas.create_image(496.5, 187.0, image=entry_image_2)
        self.entry_2 = Entry(self.root, bd=0, bg="#BE9DDF", highlightthickness=0, show="*")
        self.entry_2.place(x=364.0, y=169.0, width=265.0, height=34.0)

        # Guardar referencias de las imágenes para evitar que sean recogidas por el recolector de basura
        self.canvas.image = image_image_1
        self.entry_bg_1 = entry_image_1
        self.entry_bg_2 = entry_image_2

    def show_cipher_methods(self):
        self.cipher_window = Toplevel(self.root)
        self.cipher_window.title("Métodos de Cifrado")
        self.cipher_window.geometry("300x200")
        self.cipher_window.configure(bg="#D3D3D3")

        Label(self.cipher_window, text="Selecciona un método de cifrado:", bg="#D3D3D3").pack(padx=10, pady=5)

        self.cipher_method = StringVar(value="")

        if 'todos_los_cifrados' in self.roles_usuario or 'cifrado_clasico' in self.roles_usuario:
            Radiobutton(self.cipher_window, text="Cifrado César", variable=self.cipher_method, value="Cesar", bg="#D3D3D3").pack(anchor='w')

        if 'todos_los_cifrados' in self.roles_usuario or 'cifrado_moderno' in self.roles_usuario:
            Radiobutton(self.cipher_window, text="Cifrado AES", variable=self.cipher_method, value="AES", bg="#D3D3D3").pack(anchor='w')

        Button(self.cipher_window, text="Aceptar", command=self.some_function).pack(pady=10)

    def some_function(self):
        if self.cipher_method.get() == "AES":
            aes_app = AESApp(self.root)
        elif self.cipher_method.get() == "Cesar":
            caesar_app = CaesarCipherApp(self.root)
        else:
            messagebox.showwarning("Selección de cifrado", "Por favor, selecciona un método de cifrado.")



    def on_login_click(self):
        # Este es el lugar donde capturas los intentos de inicio de sesión
        usuario = self.entry_1.get() 
        contraseña = self.entry_2.get() 
        roles_usuario = login_backend.verificar_usuario(usuario, contraseña)

        if roles_usuario:
            self.roles_usuario = roles_usuario  # Almacenar roles del usuario autenticado
            messagebox.showinfo("Inicio de sesión exitoso", "Has iniciado sesión correctamente.")
            self.show_cipher_methods()
        else:
            messagebox.showwarning("Inicio de sesión fallido", "Usuario o contraseña incorrectos.")


    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    root = Tk()
    app = LoginApp(root)
    root.mainloop()
