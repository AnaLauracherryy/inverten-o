import sqlite3


# Criação do banco de dados e tabelas
def criar_banco():
    conn = sqlite3.connect('loja_vestidos.db')
    cursor = conn.cursor()

    # Criação da tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Criação da tabela de vestidos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vestidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            tamanho TEXT NOT NULL
        )
    ''')

    # Adicionando o usuário fixo, se ainda não existir
    cursor.execute("SELECT * FROM usuarios WHERE username = ?", ("lalinha2006@gmail.com",))
    if cursor.fetchone() is None:  # Se o usuário não existir
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)",
                       ("lalinha2006@gmail.com", "123456"))

    conn.commit()
    conn.close()


# Chama a função para criar o banco e as tabelas
criar_banco()
