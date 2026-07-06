import streamlit as st

# Título centralizado no alto usando markdown e HTML básico
st.markdown("<h1 style='text-align: center;'>Caderno Digital 📔</h1>", unsafe_allow_html=True)

# Espaçamento simples para os botões não ficarem colados no topo
st.write("")
st.write("")

# Criando as 5 colunas para os botões horizontais
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.button("Fundamentos")

with col2:
    st.button("Operadores")

with col3:
    st.button("Strings")

with col4:
    st.button("Controle")

with col5:
    st.button("Estruturas")