import sqlite3

conexao = sqlite3.connect("banco.db", check_same_thread=False)
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
        


def deletar_anotacao(id_nota):
        cursor.execute("DELETE FROM anotacoes WHERE id = ?", (id_nota,))
        conexao.commit()