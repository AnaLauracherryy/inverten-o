import tkinter as tk
import vestidos

def open_vestidos_page():
    root.destroy()  # Fecha a janela principal
    vestidos.open_vestidos_page()  # Abre a página de vestidos

root = tk.Tk()
root.title("Página Principal")
root.geometry("1366x768")  # Define o tamanho da janela

button_vestidos = tk.Button(root, text="Gerenciar Vestidos", command=open_vestidos_page)
button_vestidos.pack(pady=20)

root.mainloop()
