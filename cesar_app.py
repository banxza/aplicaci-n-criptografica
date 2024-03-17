from tkinter import Tk, Canvas, Text, Button, PhotoImage, messagebox, Toplevel
from pathlib import Path
from tkinter import Toplevel, Label, Radiobutton, Button, StringVar , Entry
from tkinter import *
import cesar_backend
from cesar_backend import *
from cesar_backend import caesar_cipher_encrypt, caesar_cipher_decrypt

class CaesarCipherApp:
    def __init__(self, master=None):
        if master is None:
            self.window = Tk()
        else:
            self.window = Toplevel(master)
        
        self.window.geometry("686x336")
        self.window.title("Encriptador Cesar")
        self.window.configure(bg="#4AFF9D")
        
        self.canvas = Canvas(self.window, bg="#4AFF9D", height=336, width=686, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        
        self.setup_ui()
        
        self.window.resizable(False, False)
        if master is None:
            self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        output_path = Path(__file__).parent
        assets_path = output_path / Path("images/cesar")
        return assets_path / Path(path)

    def setup_ui(self):
        self.entry_bg_1_image = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(343.0, 108.5, image=self.entry_bg_1_image)
        #SE ESCRIBE EL TEXTO ENCRIPTADO
        self.entry_1 = Entry(self.window, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=145.0, y=94.0, width=396.0, height=27.0)

        self.entry_bg_2_image = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(342.5, 288.5, image=self.entry_bg_2_image)
        
        #SE MUESTRA EL TEXTO ENCRIPTADO
        self.entry_2 = Entry(self.window, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=159.0, y=274.0, width=367.0, height=27.0)

        # Repetir para el resto de las entradas y botones

        self.canvas.create_text(64.0, 20.0, anchor="nw", text="CIFRADO CESAR ", fill="#000000", font=("Inter Bold", 24 * -1))
        self.canvas.create_text(201.0, 58.0, anchor="nw", text="Texto Plano/Encriptado", fill="#000000", font=("Inter Bold", 24 * -1))
        self.canvas.create_text(89.0, 138.0, anchor="nw", text="Alfabeto", fill="#000000", font=("Inter Bold", 24 * -1))
        self.canvas.create_text(399.0, 138.0, anchor="nw", text="Desplazamiento", fill="#000000", font=("Inter Bold", 24 * -1))
        
        # Botón 1: Cifrar
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self.window, image=self.button_image_1, borderwidth=0, highlightthickness=0, command=self.on_encrypt_button_clicked , relief="flat")
        self.button_1.place(x=346.0, y=230.0, width=180.0, height=29.0)

        # Botón 2: Descifrar
        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(self.window, image=self.button_image_2, borderwidth=0, highlightthickness=0, command=self.on_decrypt_button_clicked , relief="flat")
        self.button_2.place(x=159.0, y=230.0, width=150.0, height=29.0)

        self.entry_bg_3_image = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(501.5, 188.5, image=self.entry_bg_3_image)
        
        # Campo de entrada para el alfabeto
        self.entry_3 = Entry(self.window, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, readonlybackground="#FFFFFF", state='readonly')
        self.entry_3.place(x=374.0, y=174.0, width=255.0, height=27.0)
        #Campo de desplazamiento
        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(self.window, image=self.button_image_3, borderwidth=0, highlightthickness=0, command=self.on_additional_action_1, relief="flat")
        self.button_3.place(x=584.0, y=178.0, width=26.0, height=22.0)

        self.entry_bg_4_image = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(140.0, 188.5, image=self.entry_bg_4_image)
        
        # Campo de entrada para el desplazamiento
        self.entry_4 = Entry(self.window, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, readonlybackground="#FFFFFF", state='readonly')
        self.entry_4.place(x=41.0, y=174.0, width=198.0, height=27.0)
        
        # SELECCION DEL ALFABETO
        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(self.window, image=self.button_image_4, borderwidth=0, highlightthickness=0, command=self.on_additional_action_2, relief="flat")
        self.button_4.place(x=201.0, y=178.0, width=26.0, height=22.0)

    #FUNCIONES DE LOS BOTONES ENCRIPTAR Y DESENCRIPTAR
    def on_encrypt_button_clicked(self):
        plaintext = self.entry_1.get()
        if not plaintext:
            messagebox.showerror("Error", "Por favor ingrese un texto para encriptar.")
            return
        try:
            shift = int(self.entry_3.get())
            selected_alphabet = self.entry_4.get().strip()
            if not selected_alphabet:
                raise ValueError("Por favor seleccione un alfabeto.")
            alphabet = alphabet_loader(selected_alphabet)

            encrypted_text = caesar_cipher_encrypt(plaintext, -shift, alphabet)
            self.entry_2.delete(0, END)
            self.entry_2.insert(0, encrypted_text)
        except ValueError as ve:
            messagebox.showerror("Error de Valor", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Un error inesperado ha ocurrido: {e}")

    def on_decrypt_button_clicked(self):
        ciphertext = self.entry_1.get()
        if not ciphertext:
            messagebox.showerror("Error", "Por favor ingrese un texto para desencriptar.")
            return
        try:
            shift = int(self.entry_3.get())
            selected_alphabet = self.entry_4.get().strip()
            if not selected_alphabet:
                raise ValueError("Por favor seleccione un alfabeto.")
            alphabet = alphabet_loader(selected_alphabet)

            decrypted_text = caesar_cipher_decrypt(ciphertext, shift, alphabet)
            self.entry_2.delete(0, END)
            self.entry_2.insert(0, decrypted_text)
        except ValueError as ve:
            messagebox.showerror("Error de Valor", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Un error inesperado ha ocurrido: {e}")

    #CLICK ADICCIONAL PARA EL DESPLAZAMIENTO 
    # Ejemplo de función para manejar un evento de clic adicional
    def on_additional_action_1(self):
        # Crear una nueva ventana emergente para seleccionar desplazamientos
        self.alphabet_window = Toplevel(self.window)
        self.alphabet_window.title("Selección de Desplazamiento")
        self.alphabet_window.geometry("300x200")  # Tamaño ajustado para simplificar

        # Hace la ventana modal
        self.alphabet_window.grab_set()

        # Etiqueta para indicar la acción a realizar
        Label(self.alphabet_window, text="Selecciona un desplazamiento:", font=("Arial", 12)).pack(padx=10, pady=10)

        # Variable para almacenar la selección del desplazamiento
        self.selected_shift = IntVar(value=1)

        # Frame para los botones de radio
        frame = Frame(self.alphabet_window)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Opciones de desplazamientos con botones de radio
        for i in range(3, 6, 2):
            Radiobutton(frame, text=str(i), variable=self.selected_shift, value=i, font=("Arial", 12)).pack(anchor='w')

        # Botón para confirmar la selección
        Button(self.alphabet_window, text="Aceptar", font=("Arial", 12), bg="green", relief="raised", bd=2, command=self.confirm_shift_selection).pack(pady=10)

    #CLICK ADICCIONAL PARA EL ALFABETO
    # Funcion para manejar el alfabeto
    def on_additional_action_2(self):
        # Crear una nueva ventana emergente para seleccionar alfabetos
        self.alphabet_window = Toplevel(self.window)
        self.alphabet_window.title("Selección de Alfabeto")
        self.alphabet_window.geometry("300x200")

        # Etiqueta para indicar la acción a realizar
        Label(self.alphabet_window, text="Selecciona un alfabeto:", font=("Arial", 12), relief="groove", bd=2).pack(padx=10, pady=5)

        # Variable para almacenar la selección del alfabeto
        self.selected_alphabet = StringVar(value="Español")

        # Opciones de alfabetos con botones de radio
        Radiobutton(self.alphabet_window, text="Español", variable=self.selected_alphabet, value="Español", font=("Arial", 12), relief="ridge", bd=2).pack(anchor='w', padx=10, pady=2)
        Radiobutton(self.alphabet_window, text="Inglés", variable=self.selected_alphabet, value="Inglés", font=("Arial", 12), relief="ridge", bd=2).pack(anchor='w', padx=10, pady=2)

        # Botón para confirmar la selección
        Button(self.alphabet_window, text="Aceptar", font=("Arial", 12), relief="raised", bd=2, command=self.set_alphabet).pack(pady=10)

    #FUNCION DEL ALFABETO 
    def set_alphabet(self):
        chosen_alphabet = self.selected_alphabet.get()
        self.entry_4.configure(state='normal')  # Temporalmente cambia el estado a normal para permitir la edición
        self.entry_4.delete(0, 'end')  # Borra el contenido actual
        self.entry_4.insert(0, chosen_alphabet)  # Inserta el nuevo valor
        self.entry_4.configure(state='readonly')  # Vuelve a cambiar el estado a solo lectura
        self.alphabet_window.destroy()  # Cierra la ventana emergente

        # Cierra la ventana emergente de selección de alfabeto
        self.alphabet_window.destroy()
        #CLICK DE CONFIRMACIÓN DEL DESPLAZAMIENTO
    def confirm_shift_selection(self):
        chosen_shift = self.selected_shift.get()
        self.entry_3.configure(state='normal')  # Temporalmente cambia el estado a normal para permitir la edición
        self.entry_3.delete(0, END)  # Borra el contenido actual
        self.entry_3.insert(0, str(chosen_shift))  # Inserta el nuevo valor
        self.entry_3.configure(state='readonly')  # Vuelve a cambiar el estado a solo lectura
        self.alphabet_window.destroy()  # Cierra la ventana emergente

        
if __name__ == "__main__":
    app = CaesarCipherApp()

