import tkinter as tk
from tkinter import messagebox
import sqlite3


def login():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect('loja_vestidos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login", "Login bem-sucedido!")
        root.destroy()  # Fecha a janela de login
        import main  # Importa a página principal
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")


root = tk.Tk()
root.title("Login")
root.geometry("1366x768")  # Define o tamanho da janela

label_username = tk.Label(root, text="Usuário:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Senha:")
label_password.pack()
entry_password = tk.Entry(root, show='*')
entry_password.pack()

button_login = tk.Button(root, text="Login", command=login)
button_login.pack()

root.mainloop()
