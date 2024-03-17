import tkinter as tk
from tkinter import ttk

class CifradoCesarApp:
    def cifrar(self):
        # La lógica para cifrar el texto va aquí
        pass

    def descifrar(self):
        # La lógica para descifrar el texto va aquí
        pass

    def __init__(self, master):
        self.master = master
        master.title("Cifrado César")

        # Configuración del estilo para los botones
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 10, 'bold'), foreground='white')

        # Resto de la configuración de la UI...

        # Botón de Cifrar
        self.cifrar_btn = ttk.Button(master, text="Cifrar", command=self.cifrar, style='TButton')
        self.cifrar_btn.pack(pady=5)
        self.cifrar_btn['background'] = '#4CAF50'

        # Botón de Descifrar
        self.descifrar_btn = ttk.Button(master, text="Descifrar", command=self.descifrar, style='TButton')
        self.descifrar_btn.pack(pady=5)
        self.descifrar_btn['background'] = '#4CAF50'

if __name__ == "__main__":
    root = tk.Tk()
    app = CifradoCesarApp(root)
    root.mainloop()
