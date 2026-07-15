"""
Para rodar: streamlit run test.py
"""

import streamlit as st

# -- CONFIGURAÇÃO DA PÁGINA --
st.set_page_config(
    page_title="Caderno Digital",
    page_icon="🐍",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Lista de categorias com a Home inclusa
CATEGORIAS = [
    "🏠 Home",
    "Fundamentos e Tipos de Dados",
    "Operadores",
    "Manipulação de Strings",
    "Estruturas de Controle",
    "Estruturas de Dados",
    "Sintaxe"
]

# -- SIDEBAR (MENU LATERAL) --
with st.sidebar:
    st.header("📌 Temas")
    pagina = st.radio(
        "",
        options=CATEGORIAS,
        label_visibility="collapsed"
    )
    st.divider()


# -- ROTEAMENTO DE CONTEÚDO (MOTOR BACK-END) --

if pagina == "🏠 Home":
    # Cabeçalho único e imponente para a tela inicial
    st.title("Central de Estudos Back-End 📓✏️")
    st.divider()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("Selecione um dos módulos na barra lateral.")
    st.divider()
    
    # Sistema de colunas para centralizar o logotipo do Python
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://www.python.org/static/community_logos/python-logo-generic.svg", width=180)

elif pagina == "Fundamentos e Tipos de Dados":
    st.title("🧱 Fundamentos e Tipos de Dados")
    st.caption("Caderno Digital Python")
    st.divider()
    st.write("Aqui você vai colocar suas anotações sobre int, float, str, bool e variáveis.")

elif pagina == "Operadores":
    st.title("🧮 Operadores")
    st.caption("Caderno Digital Python")
    st.divider()
    st.write("Aqui vão as explicações sobre operadores aritméticos (+, -, *, /) e lógicos (and, or, not).")

elif pagina == "Manipulação de Strings":
    st.title("🔤 Manipulação de Strings")
    st.caption("Caderno Digital Python")
    st.divider()
    st.write("Conteúdo focado em métodos de strings, f-strings, fatiamento e concatenação.")

elif pagina == "Estruturas de Controle":
    st.title("🎛️ Estruturas de Controle")
    st.caption("Caderno Digital Python")
    st.divider()
    st.write("Área dedicada aos conceitos de condicionais (if, elif, else) e laços de repetição (for, while).")

elif pagina == "Estruturas de Dados":
    st.title("📦 Estruturas de Dados")
    st.caption("Caderno Digital Python")
    st.divider()
    st.write("Espaço para documentar o uso de listas, tuplas, dicionários e conjuntos (sets).")

elif pagina == "Sintaxe":
    st.title("✍️ Sintaxe")
    st.caption("Caderno Digital Python")
    st.divider()
    st.write("Regras gerais de escrita de código limpo, indentação e boas práticas em Python.")





2. NÚMERO INTEIRO (Integer/int) -> Sem aspas e sem vírgula.
        idade = 20
        quantidade = 5


3. NÚMERO DECIMAL (Float) -> Use PONTO, não vírgula!
        preco = 19.99
        altura = 1.75


    4. BOOLEANO (Bool) -> Verdadeiro ou Falso (1ª letra Maiúscula).
        tem_carteira = True
        eh_maior_de_idade = False