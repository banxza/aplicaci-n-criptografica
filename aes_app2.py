
from tkinter import Tk, Canvas, Button, Entry, PhotoImage,Toplevel
from pathlib import Path
import aes_backend
from tkinter import messagebox
import binascii

class AESApp:
    def __init__(self, master=None):
        if master is None:
            self.window = Tk()
        else:
            self.window = Toplevel(master)
        
        self.window.geometry("678x457")
        self.window.title("Encriptador AES")
        self.window.configure(bg="#FFFFFF")
        
        # Asegúrate de inicializar el canvas antes de llamar a setup_ui
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=457, width=678, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        
        self.setup_ui()
        
        self.window.resizable(False, False)
        if master is None:
            self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        output_path = Path(__file__).parent
        assets_path = output_path / Path("images/aes")
        return assets_path / Path(path)
    
    def create_entry(self, image_file, x_image, y_image, x_entry, y_entry, width_entry, height_entry, bg_color):
        entry_image = PhotoImage(file=self.relative_to_assets(image_file))
        self.canvas.create_image(x_image, y_image, image=entry_image)
        entry = Entry(self.window, bd=0, bg=bg_color, fg="#000716", highlightthickness=0)
        entry.place(x=x_entry, y=y_entry, width=width_entry, height=height_entry)
        return entry, entry_image

    def create_button(self, image_file, x, y, width, height, command):
        button_image = PhotoImage(file=self.relative_to_assets(image_file))
        button = Button(self.window, image=button_image, borderwidth=0, highlightthickness=0, command=command, relief="flat")
        button.place(x=x, y=y, width=width, height=height)
        button.image = button_image  # Mantener una referencia
        return button
    
    #FUNCIONES DE ENCRIPTADO

    def on_encrypt_cbc_clicked(self):
        plain_text = self.entry_1.get().strip()
        if not plain_text:
            messagebox.showerror("Error", "El texto a cifrar está vacío.")
            return

        iv, key, encrypted_message = aes_backend.encrypt_message_cbc(plain_text)
        self.entry_2.delete(0, "end")
        self.entry_2.insert(0, iv.hex())
        self.entry_3.delete(0, "end")
        self.entry_3.insert(0, key.hex())
        self.entry_4.delete(0, "end")
        self.entry_4.insert(0, binascii.hexlify(encrypted_message).decode())

    def on_decrypt_cbc_clicked(self):
        encrypted_message_hex = self.entry_1.get().strip()
        iv_hex = self.entry_2.get().strip()
        key_hex = self.entry_3.get().strip()

        # Comprueba si algún campo está vacío y muestra un mensaje de error
        if not encrypted_message_hex or not iv_hex or not key_hex:
            messagebox.showerror("Error", "Por favor, asegúrate de que todos los campos estén completos.")
            return

        # Intenta descifrar el mensaje y maneja cualquier error potencial
        try:
            decrypted_message = aes_backend.decrypt_message_cbc(encrypted_message_hex, key_hex, iv_hex)
            self.entry_4.delete(0, "end")
            self.entry_4.insert(0, decrypted_message)
        except (ValueError, binascii.Error) as e:  # Atrapar errores comunes al descifrar
            messagebox.showerror("Error de descifrado", f"Ocurrió un error al descifrar: {e}")

    def on_encrypt_ecb_clicked(self):
        plaintext = self.entry_1.get().strip()
        key = self.entry_3.get().strip()

        if not plaintext or not key:
            messagebox.showerror("Error", "El texto y la clave no pueden estar vacíos.")
            return

        encrypted_hex = aes_backend.encrypt_message_ecb(plaintext, key.encode())
        self.entry_4.delete(0, "end")
        self.entry_4.insert(0, encrypted_hex)

    def on_decrypt_ecb_clicked(self):
        encrypted_hex = self.entry_1.get().strip()
        key = self.entry_3.get().strip()

        if not encrypted_hex or not key:
            messagebox.showerror("Error", "El texto cifrado y la clave no pueden estar vacíos.")
            return

        try:
            plaintext = aes_backend.decrypt_message_ecb(encrypted_hex, key.encode())
            self.entry_4.delete(0, "end")
            self.entry_4.insert(0, plaintext)
        except ValueError as e:
            messagebox.showerror("Error", f"Error al descifrar: {e}")

#CONFIGURACIÓN DE LA INTERFAZ GRAFICA
    def setup_ui(self):
        # Crear textos
        texts = [("ENCRIPTADOR Y DESENCRIPTADOR AES", 108, 29), 
                 ("Texto Encriptado/Plano", 24, 74), 
                 ("Código IV", 20, 142), 
                 ("Código de desbloqueo", 24, 213)]
        for text, x, y in texts:
            self.canvas.create_text(x, y, anchor="nw", text=text, fill="#000000", font=("KronaOne Regular", 20))
        
        # Crear entradas y botones
        self.entry_1, _ = self.create_entry("entry_1.png", 332.5, 120.0, 31.0, 105.0, 603.0, 28.0, "#F9AD75")
        self.entry_2, _ = self.create_entry("entry_2.png", 332.5, 189.0, 31.0, 174.0, 603.0, 28.0, "#F9AD75")
        self.entry_3, _ = self.create_entry("entry_3.png", 332.5, 260.0, 31.0, 245.0, 603.0, 28.0, "#F9AD75")
        self.entry_4, _ = self.create_entry("entry_4.png", 339.0, 370.5, 19.0, 349.0, 640.0, 41.0, "#8B89E2")
        
        # Crear botones
        self.create_button("button_1.png", 20.0, 295.0, 127.0, 40.0, self.on_encrypt_cbc_clicked)
        self.create_button("button_2.png", 159.0, 295.0, 156.0, 40.0, self.on_decrypt_cbc_clicked)
        self.create_button("button_3.png", 327.0, 295.0, 152.0, 43.0, self.on_encrypt_ecb_clicked)
        self.create_button("button_4.png", 490.0, 295.0, 169.0, 43.0, self.on_decrypt_ecb_clicked)

if __name__ == "__main__":
    app = AESApp()