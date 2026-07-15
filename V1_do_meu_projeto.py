"""
Para rodar: streamlit run V1_do_meu_projeto.py
"""
import streamlit as st


class caderno: # Definição da classe 
    def __init__(self, Titulo, Categoria, Conteudo):  
        # método construtor definindo os parâmetros 


        # atributos da instância
        self.Titulo = Titulo
        self.Categoria = Categoria
        self.Conteudo = Conteudo    



    def exibir_caderno(self): 
        # Renderiza o conteúdo do tema na tela
        st.markdown(self.Conteudo)



# criando as variaveis de cada tema 
texto1 = """


### 1. Variáveis e Tipos
Variáveis podem ter seu valor alterado ("ou variado") ao longo da execução do código.
Ou seja, você pode atribuir um valor no início e depois em outro ponto você pode atribuir
um novo valor sem problemas.


#### Como se Escreve (Sintaxe)
No Python, é muito simples. Você dá um nome, coloca o sinal de igual (=) e o valor.
Não precisa falar o tipo (int, string), o Python descobre sozinho!


### Exemplos Práticos:

```python
# 1. TEXTO (String/str) -> Sempre entre aspas!
nome = "Felipe"
mensagem = 'Olá mundo'


# 2. NÚMERO INTEIRO (Integer/int) -> Sem aspas e sem vírgula.
idade = 20
quantidade = 5


# 3. NÚMERO DECIMAL (Float) -> Use PONTO, não vírgula!
preco = 19.99
altura = 1.75


# 4. BOOLEANO (Bool) -> Verdadeiro ou Falso (1ª letra Maiúscula).
tem_carteira = True
eh_maior_de_idade = False
```
"""




texto2 = """

### 1. Operadores Aritméticos
No dia a dia do trabalho, você vai usar esses operadores para qualquer tipo de cálculo no sistema:
desde calcular o valor total de um carrinho de compras com desconto, até descobrir
a média de notas de um aluno ou controlar o estoque de produtos.


| Operador | Descrição | Exemplo de Sintaxe |
| :---: | :--- | :--- |
| **+** | Adição | total = preco + frete |
| **-** | Subtração | desconto = total - 10 |
| ***_** | Multiplicação | imposto = faturamento * 0.05 |
| **/** | Divisão | media = soma / 4 |
| **//** | Divisão Inteira | parcelas = 100 // 3 |
| **%** | Módulo | resto = 10 % 3 |
| **_** | Exponenciação | resultado = 2 ** 3 |



### 2. Operadores de Atribuição
No dia a dia, eles servem para atualizar os valores das variáveis de forma rápida.
Em vez de escrever o nome da variável duas vezespara somar algo nela,
você usa esses atalhos para economizar digitação.


| Operador | Descrição | Exemplo de Sintaxe |
| :---: | :--- | :--- |
| **=** | Atribuição simples | idade = 18 |
| **+=** | Soma e atribui | pontos += 10 |
| **-=** | Subtrai e atribui | vida -= 1 |
| **\*=** | Multiplica e atribui | salario *= 1.1 |



### 3. Operadores Relacionais (Comparação)
São usados o tempo todo para tomadas de decisão nos sistemas
(os famosos if e elif). No trabalho, você usa isso para checar se
o usuário digitou a senha certa ou se o produto tem estoque.


| Operador | Descrição | Exemplo de Sintaxe |
| :---: | :--- | :--- |
| **==** | Igual a | opcao == "1" |
| **!=** | Diferente de | usuario != "admin" |
| **>** | Maior que | preco > 100 |
| **<** | Menor que | estoque < 5 |
| **>=** | Maior ou igual a | idade >= 18 |
| **<=** | Menor ou igual a | tentativas <= 3 |



### 4. Operadores Lógicos
No trabalho, os sistemas raramente dependem de uma condição só.
Eles servem para juntar várias perguntas na mesma linha. Por exemplo:
"Para liberar o acesso, o usuário precisa ser admin E estar ativo".


| Operador | Descrição | Exemplo de Sintaxe |
| :---: | :--- | :--- |
| **and** | E (tudo precisa ser True) | tem_carteira and eh_maior |
| **or** | OU (pelo menos um True) | eh_estudante or eh_professor |
| **not** | NÃO (inverte o valor) | not ativo |



### 5. Operadores de Associação
Esse é muito usado em Python para pesquisar coisas. No dia a dia, você usa
para checar se um e-mail tem o símbolo @ ou se o nome de um usuário 
está dentro de uma lista de bloqueados.


| Operador | Descrição | Exemplo de Sintaxe |
| :---: | :--- | :--- |
| **in** | Está dentro de | "Python" in lista_cursos |
| **not in** | Não está dentro de | "admin" not in lista_nomes |
"""




texto3 = """


### 1. O Problema da Padronização

O computador é literal. Para ele, `"python"`, `"PYTHON"` e `"   python   "` são três coisas completamente diferentes. Se o usuário digitar com espaços ou letras maiúsculas diferentes, sua busca ou login vai quebrar.

**A SOLUÇÃO: Métodos da classe String**

**A) Padronização (Case Insensitive):**
- `.upper()` → Transforma tudo em MAIÚSCULO
- `.lower()` → Transforma tudo em minúsculo *(essencial para validar buscas)*
- `.title()` → Deixa apenas a Primeira Letra Maiúscula

**B) Limpeza (Remover espaços em branco):**
- `.strip()` → Remove espaços do início e do fim *(essencial para senhas)*
- `.lstrip()` → Remove espaços apenas da esquerda
- `.rstrip()` → Remove espaços apenas da direita

**C) Visual e Formatação:**
- `.center(tamanho, "caractere")` → Centraliza o texto e preenche as laterais
- `.join(lista)` → Junta uma lista de palavras usando um separador

**Exemplo em Código:**
```python
texto = "   pYtHoN   "
print(texto.strip().lower())       # Resultado: "python"
print("MENU".center(20, "-"))      # Resultado: "--------MENU--------"
```

---

### 2. Interpolação (F-Strings)

Conceito: Colocar o valor de uma variável direto dentro de um texto. Antigamente usava-se `%` ou `.format()`, mas eram métodos longos e confusos.

**A Regra de Ouro (Python 3.6+):** Usamos a f-string. Basta colocar a letra `f` antes das aspas e usar chaves `{}` onde a variável entra.

- **Sintaxe:** `f"Texto {variavel}"`
- **Formatação de Moeda/Decimais:** `{valor:.2f}` → Limita para 2 casas decimais

**Exemplo em Código:**
```python
nome = "Felipe"
preco = 49.9
print(f"Olá {nome}, o total foi de R$ {preco:.2f}")
# Resultado: Olá Felipe, o total foi de R$ 49.90
```

---

### 3. Fatiamento de Strings (Slicing)

Conceito: Técnica para extrair partes de um texto original. Cada caractere possui um índice numérico que começa do `0`.

**Sintaxe:** `string[ início : fim : passo ]`

> ⚠️ **REGRA DO FIM EXCLUSIVO:** O número do "fim" nunca entra no corte. O Python para exatamente um caractere ANTES dele.

**Para que serve na vida real?**
1. **Formatação:** Inverter datas (de formato americano para brasileiro)
2. **Segurança:** Ofuscar dados, mostrando apenas os últimos dígitos do CPF/Cartão
3. **Validação:** Verificar se as últimas letras de um arquivo são `.exe` ou `.pdf`

**Exemplo em Código:**
```python
id_pedido = "COD-98765-BR"
codigo = id_pedido[4:9]  # Pega do índice 4 até o 8 (o 9 fica de fora)
print(codigo)             # Resultado: "98765"
```

---

### 4. Strings de Múltiplas Linhas (Aspas Triplas)

O que é: Forma de criar blocos de texto longos sem precisar usar `\\n` a todo momento. O Python guarda toda a formatação exatamente do jeito que você digitou.

**Sintaxe:**
```python
menu = \"\"\"
1. Entrar
2. Configurações
3. Sair
\"\"\"
```
"""




texto4 = """

### 1. Estruturas Condicionais (Tomada de Decisão)

Permitem que o programa siga caminhos diferentes dependendo das condições.

- **`if` (Se):** Executa um bloco de código APENAS se a condição for verdadeira.
- **`elif` (Senão Se):** Testa uma NOVA condição caso a anterior tenha sido falsa.
- **`else` (Senão):** Executa um código geral caso NENHUMA das condições anteriores tenha sido verdadeira.

**Sintaxe Geral:**
```python
if condicao_1:
    # código executado se a condicao_1 for True
elif condicao_2:
    # código executado se a condicao_1 for False e a condicao_2 for True
else:
    # código executado se todas as anteriores forem False
```

---

### 2. Laços de Repetição (Loops)

Objetivo: Repetir um bloco de código várias vezes sem precisar reescrever as mesmas linhas.

---

#### A) Loop FOR — O Inspetor

Usado quando sabemos o limite ou quantas vezes queremos repetir. Perfeito para percorrer sequências (listas, strings, dicionários). **Ele para sozinho.**

**Jeito 1 — Percorrer Lista:**
```python
mochila = ["faca", "corda", "lanterna"]
for item in mochila:
    print(f"Você está carregando: {item}")
```

**Jeito 2 — Repetir X vezes com range:**
```python
for numero in range(3):
    print("Atirando!")
```

**Jeito 3 — For Duplo em Dicionários com `.items()`:**
```python
# Força o Python a ler tanto a chave quanto o valor simultaneamente
for chave, valor in agentes.items():
    print(f"Agente: {chave} | Nível: {valor}")
```

---

#### B) Loop WHILE — O Motor

Usado quando **não sabemos** exatamente quantas vezes o loop vai rodar. Continua executando enquanto a condição permanecer verdadeira.

**While Condicional — Para sozinho quando a condição muda:**
```python
municao = 3
while municao > 0:
    print("Atirando!")
    municao -= 1  # Diminui a munição até a condição virar False
```

**While True — Loop infinito, exige parada manual:**
```python
while True:
    opcao = input("Digite 1 para sair: ")
    if opcao == "1":
        break  # Destrói o loop imediatamente
```

---

> 💡 **Sobre o 'do while' em Python:**
> Python não tem um comando `do while`. Para fazer um código rodar pelo menos uma vez antes de testar a condição, usamos o `while True` com um `if` e `break` na última linha do bloco.
"""




texto5 = """

### 1. Listas `[]` — A Caixa Aberta (Mutável)

Guarda várias variáveis juntas em uma única sequência. Você pode adicionar, remover ou alterar qualquer item a qualquer momento. **A contagem das posições sempre começa no número 0.**

**Formas Rápidas de Acessar os Dados:**
- `minha_lista[-1]` → Pega o último elemento sem precisar saber o tamanho
- `matriz[0][0]` → Acessa uma lista dentro de outra (Linha e Coluna)
- `minha_lista[::-1]` → Inverte a ordem de todos os elementos na hora

**Como Percorrer e Criar Listas de Forma Inteligente:**

*Usando o Laço `for` com `enumerate`:*
```python
for i, v in enumerate(lista):  # Pega a posição (i) e o valor (v) juntos
    print(i, v)
# Uso real: rankings, históricos ou numerar linhas na tela
```

*Usando List Comprehension (Atalho de 1 linha):*
```python
[n for n in num if n % 2 == 0]
# Uso real: filtrar dados de bancos de dados (ex: ver só compras negativadas)
```

**Sintaxe e Métodos Principais:**
```python
minha_lista = ["Python", "C#", "Java"]
len(minha_lista)        # Retorna a quantidade de elementos
minha_lista.append("JavaScript")  # Adiciona item no final
minha_lista.extend(outra_lista)   # Funde outra lista no final
sorted(minha_lista)     # Cria uma cópia ordenada
minha_lista.pop(0)      # Remove o item da posição indicada
minha_lista.remove("Java")        # Remove a primeira ocorrência
minha_lista.count("Python")       # Conta quantas vezes aparece
minha_lista.index("C#")           # Retorna a posição do valor
minha_lista.sort()      # Organiza a lista original na memória
```

---

### 2. Tuplas `()` — A Caixa Lacrada (Imutável)

Igual à lista, mas com informações **FIXAS**. Depois que você cria uma tupla, o Python tranca ela. Excelente para guardar configurações do sistema, endereços de IP fixos ou os meses do ano.

> ⚠️ **Regra de Ouro:** Para criar uma tupla de 1 item só, você **PRECISA** colocar uma vírgula no final, senão o Python acha que é um texto comum.

```python
meu_ip = ("192.168.0.1")   # ❌ Vira uma String comum
meu_ip = ("192.168.0.1",)  # ✅ Vira uma Tupla blindada
```

**Métodos Principais:**
```python
minha_tupla = ("Janeiro", "Fevereiro", "Março")
minha_tupla.count("Janeiro")  # Conta as ocorrências
minha_tupla.index("Março")    # Mostra a posição do item
```

---

### 3. Conjuntos `{}` — O Saco Mágico Sem Fundo (Set)

Estrutura que **não aceita itens repetidos** e não possui nenhuma ordem. Perfeita para limpar dados duplicados e cruzar listas grandes.

> 💡 Como não tem ordem fixa, não possui índices. Para acessar posições, use `list(meu_set)`.

**Sintaxe e Métodos Principais:**
```python
meu_set = {"Python", "C#", "C#"}  # Vira apenas {"Python", "C#"}

"Python" in meu_set       # Retorna True/False ultrarrápido
meu_set.add("Java")       # Adiciona item (ignora se já existir)
meu_set.discard("PHP")    # Remove com segurança (sem quebrar o código)
meu_set.intersection(set2) # Mostra elementos que existem nos dois sets
meu_set.difference(set2)   # Mostra o que tem no primeiro e não no outro
meu_set.union(set2)        # Junta os dois eliminando repetidos
```

---

### 4. Dicionários `{}` — O Fichário Inteligente (Dict)

Não usa posições numéricas. Funciona guardando dados em pares de **Chave** e **Valor**. A chave é a etiqueta única e imutável, o valor é o conteúdo real.

**Sintaxe e Métodos Principais:**
```python
meu_dict = {"nome": "Felipe", "cargo": "Estagiário Back-End"}

meu_dict["linguagem"] = "Python"          # Cria ou altera um valor
meu_dict.get("idade", "Não informado")    # Busca sem quebrar o código
meu_dict.keys()    # Retorna todas as chaves
meu_dict.values()  # Retorna todos os valores
meu_dict.items()   # Retorna o par completo

# Perfeito para usar no for:
for chave, valor in meu_dict.items():
    print(f"{chave}: {valor}")
```
"""



# Criando a lista que vai guardar os temas
lista_temas = [texto1, texto2, texto3, texto4, texto5]



# Configuração da página
st.set_page_config(
    page_title="Caderno Digital",
    page_icon="🐍",
    layout="centered",
    initial_sidebar_state="expanded")



# Lista de categorias com a Home inclusa
CATEGORIAS = [
    "🏠 Home",
    "Fundamentos e Tipos de Dados",
    "Operadores",
    "Manipulação de Strings",
    "Estruturas de Controle",
    "Estruturas de Dados",]



# Navegação lateral com os temas disponíveis
with st.sidebar:
    st.header("📌 Temas")
    pagina = st.radio(
        "",
        options=CATEGORIAS,
        label_visibility="collapsed")
    st.divider()



# ROTEAMENTO DE CONTEÚDO (Onde o seu front antigo encontra seu Back-End)
if pagina == "🏠 Home":
    st.title("Central de Estudos Back-End 📓✏️")
    st.divider()
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("Selecione um dos módulos na barra lateral.")
    st.divider()
    
    col1, col2, col3, = st.columns([1, 2, 1])
    with col2:
        st.image("https://www.python.org/static/community_logos/python-logo-generic.svg", width=180)


elif pagina == "Fundamentos e Tipos de Dados":
    st.title("💻 Fundamentos e Tipos de Dados")

    # Chamando seu Back-End para renderizar o texto real das aspas triplas!
    meu_objeto = caderno("CURSO DE LÓGICA DE PROGRAMAÇÃO (by Felipe)", "tema: Fundamentos e Tipos de Dados", lista_temas[0])
    meu_objeto.exibir_caderno()


elif pagina == "Operadores":
    st.title("🔢 Operadores")
    st.divider()
    
    meu_objeto = caderno("CURSO DE LÓGICA DE PROGRAMAÇÃO (by Felipe)", "tema: Operadores", lista_temas[1])
    meu_objeto.exibir_caderno()


elif pagina == "Manipulação de Strings":
    st.title("🔤 Manipulação de Strings")

    st.divider()
    
    meu_objeto = caderno("CURSO DE LÓGICA DE PROGRAMAÇÃO (by Felipe)", "tema: Manipulação de Strings", lista_temas[2])
    meu_objeto.exibir_caderno()


elif pagina == "Estruturas de Controle":
    st.title("⚙️ Estruturas de Controle")
    
    st.divider()
    
    meu_objeto = caderno("CURSO DE LÓGICA DE PROGRAMAÇÃO (by Felipe)", "tema: Estruturas de Controle", lista_temas[3])
    meu_objeto.exibir_caderno()


elif pagina == "Estruturas de Dados":
    st.title("📦 Estruturas de Dados")
    
    st.divider()
    
    meu_objeto = caderno("CURSO DE LÓGICA DE PROGRAMAÇÃO (by Felipe)", "tema: Estruturas de Dados", lista_temas[4])
    meu_objeto.exibir_caderno()