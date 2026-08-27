import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()



def criar_tabela():
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS anotacoes (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                conteudo TEXT NOT NULL
                )
        """)


def salvar_anotacao(titulo, conteudo):
        cursor.execute("""
                INSERT INTO anotacoes  
                (titulo, conteudo)
                VALUES (?, ?)""", (titulo, conteudo))
        conexao.commit()

def listar_anotacoes():
        cursor.execute("""SELECT * FROM anotacoes""")

        textos = cursor.fetchall()
        return textos
        

