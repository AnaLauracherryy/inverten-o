import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3


def load_vestidos(tree):
    # Limpa a árvore
    for row in tree.get_children():
        tree.delete(row)

    # Carrega os vestidos do banco de dados
    conn = sqlite3.connect('loja_vestidos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vestidos")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)
    conn.close()


def add_vestido(tree, nome, preco, tamanho):
    conn = sqlite3.connect('loja_vestidos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vestidos (nome, preco, tamanho) VALUES (?, ?, ?)", (nome, preco, tamanho))
    conn.commit()
    conn.close()
    load_vestidos(tree)


def update_vestido(tree, selected_item, nome, preco, tamanho):
    vestido_id = tree.item(selected_item)["values"][0]
    conn = sqlite3.connect('loja_vestidos.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE vestidos SET nome=?, preco=?, tamanho=? WHERE id=?", (nome, preco, tamanho, vestido_id))
    conn.commit()
    conn.close()
    load_vestidos(tree)


def delete_vestido(tree, selected_item):
    vestido_id = tree.item(selected_item)["values"][0]
    conn = sqlite3.connect('loja_vestidos.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM vestidos WHERE id=?", (vestido_id,))
    conn.commit()
    conn.close()
    load_vestidos(tree)


def open_vestidos_page():
    def on_select(event):
        selected_item = tree.selection()[0]
        values = tree.item(selected_item)["values"]
        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, values[1])
        entry_preco.delete(0, tk.END)
        entry_preco.insert(0, values[2])
        entry_tamanho.delete(0, tk.END)
        entry_tamanho.insert(0, values[3])

    def add_command():
        nome = entry_nome.get()
        preco = float(entry_preco.get())
        tamanho = entry_tamanho.get()
        add_vestido(tree, nome, preco, tamanho)
        entry_nome.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        entry_tamanho.delete(0, tk.END)

    def update_command():
        selected_item = tree.selection()[0]
        nome = entry_nome.get()
        preco = float(entry_preco.get())
        tamanho = entry_tamanho.get()
        update_vestido(tree, selected_item, nome, preco, tamanho)

    def delete_command():
        selected_item = tree.selection()[0]
        delete_vestido(tree, selected_item)

    window = tk.Tk()
    window.title("Gerenciar Vestidos")
    window.geometry("1366x768")  # Define o tamanho da janela

    tree = ttk.Treeview(window, columns=("ID", "Nome", "Preço", "Tamanho"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Preço", text="Preço")
    tree.heading("Tamanho", text="Tamanho")
    tree.pack()

    load_vestidos(tree)

    tree.bind("<<TreeviewSelect>>", on_select)

    label_nome = tk.Label(window, text="Nome:")
    label_nome.pack()
    entry_nome = tk.Entry(window)
    entry_nome.pack()

    label_preco = tk.Label(window, text="Preço:")
    label_preco.pack()
    entry_preco = tk.Entry(window)
    entry_preco.pack()

    label_tamanho = tk.Label(window, text="Tamanho:")
    label_tamanho.pack()
    entry_tamanho = tk.Entry(window)
    entry_tamanho.pack()

    button_add = tk.Button(window, text="Adicionar", command=add_command)
    button_add.pack()

    button_update = tk.Button(window, text="Atualizar", command=update_command)
    button_update.pack()

    button_delete = tk.Button(window, text="Excluir", command=delete_command)
    button_delete.pack()

    window.mainloop()


# Permitir que a página de vestidos seja aberta diretamente
if __name__ == "__main__":
    open_vestidos_page()
