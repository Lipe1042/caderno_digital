class caderno:
    def __init__(self, Titulo, Categoria, Conteudo):
        
        self.Titulo = Titulo
        self.Categoria = Categoria
        self.Conteudo = Conteudo    



    def exibir_caderno(self):


        print(f"""
                    ==================================================================
                                {self.Titulo}
                    ==================================================================""")


        print(f"""                                    {self.Categoria}""")


        print(f"""{self.Conteudo}""")



print("""\n=== ESCOLHA O TEMA ===


1 - Fundamentos e Tipos de Dados

2 - Operadores

3 - Manipulação de Strings

4 - Estruturas de Controle

5 - Estruturas de Dados
""")



texto1 = """
                    ------------------------------------------------------------------
                                        1. VARIÁVEIS E TIPOS 
                    ------------------------------------------------------------------

            Variáveis podem ter seu valor alterado ("ou variado") ao longo da execução do código. 
            Ou seja, você pode atribuir um valor no inicio e depois em outro ponto você pode atribuir
            um novo valor sem problemas. 



                    ---------------------------------------------------------
                                    COMO SE ESCREVE (SINTAXE)
                    ---------------------------------------------------------
        No Python, é muito simples. Você dá um nome, coloca o sinal de igual (=) e o valor.
        Não precisa falar o tipo (int, string), o Python descobre sozinho!


Exemplos Práticos:

    1. TEXTO (String/str) -> Sempre entre aspas!
        nome = "Felipe"
        mensagem = 'Olá mundo'


    2. NÚMERO INTEIRO (Integer/int) -> Sem aspas e sem vírgula.
        idade = 20
        quantidade = 5


    3. NÚMERO DECIMAL (Float) -> Use PONTO, não vírgula!
        preco = 19.99
        altura = 1.75


    4. BOOLEANO (Bool) -> Verdadeiro ou Falso (1ª letra Maiúscula).
        tem_carteira = True
        eh_maior_de_idade = False
"""




texto2 = """

                                        1. Operadores Aritméticos
                        No dia a dia do trabalho, você vai usar esses operadores para
                        qualquer tipo de cálculo no sistema:desde calcular o valor 
                        total de um carrinho de compras com desconto, até descobrir
                        a média de notas de um aluno ou controlar o estoque de produtos.


                            Operador       Descrição        Exemplo de Sintaxe
                                +            Adição          total = preco + frete
                                -           Subtração        desconto = total - 10
                                *         Multiplicação      imposto = faturamento * 0.05
                                /            Divisão         media = soma / 4
                                //        Divisão Inteira    parcelas = 100 // 3
                                %             Módulo         resto = 10 % 3
                                **         Exponenciação     resultado = 2 ** 3



                                        2. Operadores de Atribuição
                        No dia a dia, eles servem para atualizar os valores das variáveis
                        de forma rápida. Em vez de escrever o nome da variável duas vezes 
                        para somar algo nela, você usa esses atalhos para economizar digitação.


                            Operador       Descrição           Exemplo de Sintaxe
                                =      Atribuição simples         idade = 18
                                +=     Soma e atribui             pontos += 10
                                -=     Subtrai e atribui          vida -= 1
                                *=     Multiplica e atribui      salario *= 1.1



                                    3. Operadores Relacionais (Comparação)
                        São usados o tempo todo para tomadas de decisão nos sistemas
                        (os famosos if e elif). No trabalho, você usa isso para checar se
                        o usuário digitou a senha certa ou se o produto tem estoque.


                            Operador       Descrição        Exemplo de Sintaxe
                                ==	        Igual a	          opcao == "1"
                                !=	      Diferente de        usuario != "admin"
                                >	       Maior que	       preco > 100
                                <	       Menor que	       estoque < 5
                                >=	    Maior ou igual a	   idade >= 18
                                <=	    Menor ou igual a	tentativas <= 3



                                            4. Operadores Lógicos
                        No trabalho, os sistemas raramente dependem de uma condição só.
                        Eles servem para juntar várias perguntas na mesma linha. Por exemplo:
                        "Para liberar o acesso, o usuário precisa ser admin E estar ativo".


                            Operador               Descrição             Exemplo de Sintaxe
                                and          E (tudo precisa ser True)       tem_carteira and eh_maior
                                or            OU (pelo menos um True)        eh_estudante or eh_professor
                                not            NÃO (inverte o valor)         not ativo



                                                5. Operadores de Associação
                        Esse é muito usado em Python para pesquisar coisas. No dia a dia, você usa
                            para checar se um e-mail tem o símbolo @ ou se o nome de um usuário 
                                        está dentro de uma lista de bloqueados.


                            Operador          Descrição                Exemplo de Sintaxe
                                in           Está dentro de          "Python" in lista_cursos
                                not in       Não está dentro de      "admin" not in lista_nomes
"""




texto3 = """

[1] O PROBLEMA DA PADRONIZAÇÃO
-------------------------------------------------------------------------------
O computador é literal. Para ele, "python", "PYTHON" e "   python   " são três 
coisas completamente diferentes. Se o usuário digitar com espaços ou letras 
maiusculas diferentes, sua busca ou login vai quebrar.


A SOLUÇÃO: Métodos da classe String (Ferramentas prontas do Python)

A) Padronização (Case Insensitive):
    .upper() -> Transforma tudo em MAIÚSCULO.
    .lower() -> Transforma tudo em minúsculo (essencial para validar buscas).
    .title() -> Deixa apenas a Primeira Letra Maiúscula.


B) Limpeza (Remover espaços em branco):
    .strip()  -> Remove espaços inúteis do início e do fim (essencial para senhas).
    .lstrip() -> Remove espaços apenas da esquerda (Left).
    .rstrip() -> Remove espaços apenas da direita (Right).


C) Visual e Formatação:
    .center(tamanho, "caractere") -> Centraliza o texto e preenche as laterais.
    .join(lista) -> Junta uma lista de palavras usando um separador de texto.


Exemplo em Código:
-------------------------------------------------------------------------------
texto = "   pYtHoN   "
print(texto.strip().lower()) # Resultado: "python" (limpo e padronizado!)
print("MENU".center(20, "-")) # Resultado: "--------MENU--------"



[2] INTERPOLAÇÃO (F-STRINGS)
-------------------------------------------------------------------------------
Conceito: Colocar o valor de uma variável direto dentro de um texto. 
Antigamente usava-se '%' ou '.format()', mas eram métodos longos e confusos.


A Regra de Ouro (Python 3.6+): Usamos a f-string. 
Basta colocar a letra 'f' antes das aspas e usar chaves {} onde a variável entra.


Sintaxe: f"Texto {variavel}"
Formatação de Moeda/Decimais: {valor:.2f} -> Limita para 2 casas decimais.

Exemplo em Código:
-------------------------------------------------------------------------------
nome = "Felipe"
preco = 49.9
print(f"Olá {nome}, o total foi de R$ {preco:.2f}") 
# Resultado: Olá Felipe, o total foi de R$ 49.90



[3] FATIAMENTO DE STRINGS (SLICING)
-------------------------------------------------------------------------------
Conceito: Técnica para extrair partes (substrings) de um texto original.
Cada caractere possui um índice numérico que começa do 0.


Sintaxe: string[ início : fim : passo ]


⚠️ REGRA DO FIM EXCLUSIVO: O número do "fim" nunca entra no corte. O Python 
para exatamente um caractere ANTES dele.


Para que serve na vida real?
1. Formatação: Inverter datas (de formato americano para brasileiro).
2. Segurança: Ofuscar dados, mostrando apenas os últimos dígitos do CPF/Cartão.
3. Validação: Verificar se as últimas letras de um arquivo são ".exe" ou ".pdf".

Exemplo em Código:
-------------------------------------------------------------------------------
id_pedido = "COD-98765-BR"
codigo = id_pedido[4:9] # Pega do índice 4 até o 8 (o 9 fica de fora)
print(codigo) # Resultado: "98765"



[4] STRINGS DE MÚLTIPLAS LINHAS (ASPAS TRIPLAS)
-------------------------------------------------------------------------------
O que é: Forma de criar blocos de texto longos sem precisar entupir o código 
com quebras de linha (\\n). 


O Python guarda toda a formatação (parágrafos e espaços) exatamente do jeito 
que você digitou. Funciona como as "chaves" de outras linguagens para blocos.


Sintaxe:
-------------------------------------------------------------------------------
menu = \"\"\"
1. Entrar
2. Configurações
3. Sair
\"\"\"
===============================================================================
"""




texto4 = """

[1] ESTRUTURAS CONDICIONAIS (TOMADA DE DECISÃO)
-------------------------------------------------------------------------------
Permitem que o programa siga caminhos diferentes dependendo das condições.


A) if (Se): Executa um bloco de código APENAS se a condição for verdadeira.

B) elif (Senão Se): Testa uma NOVA condição caso a anterior tenha sido falsa.

C) else (Senão): Executa um código geral caso NENHUMA das condições anteriores 
tenha sido verdadeira (é o caso contrário).


Sintaxe Geral:
-------------------------------------------------------------------------------
if condicao_1:
    # código executado se a condicao_1 for True
elif condicao_2:
    # código executado se a condicao_1 for False e a condicao_2 for True
else:
    # código executado se todas as anteriores forem False


[2] LAÇOS DE REPETIÇÃO (LOOPS)
-------------------------------------------------------------------------------
Objetivo: Repetir um bloco de código várias vezes sem precisar reescrever as 
mesmas linhas de comando.

A) LOOP FOR (O Inspetor)
   Usado quando sabemos o limite ou quantas vezes queremos repetir. É perfeito 
   para percorrer sequências (listas, strings, dicionários). Ele para sozinho.

   * Jeito 1 (Percorrer Lista):
     mochila = ["faca", "corda", "lanterna"]
     for item in mochila:
         print(f"Você está carregando: {item}")

   * Jeito 2 (Repetir X vezes com range):
     for numero in range(3):
         print("Atirando!")

   * Jeito 3 (For Duplo em Dicionários com .items()):
     # Força o Python a ler tanto a chave quanto o valor simultaneamente
     for chave, valor in agentes.items():
         print(f"Agente: {chave} | Nível: {valor}")


B) LOOP WHILE (O Motor)
   Usado quando não sabemos exatamente quantas vezes o loop vai rodar. Ele continua 
   executando enquanto a condição permanecer verdadeira.

   * 1. While Condicional (Para sozinho quando a condição muda):
     municao = 3
     while municao > 0:
         print("Atirando!")
         municao -= 1 # Diminui a munição até a condição virar False

   * 2. While True (Loop infinito, exige parada manual):
     while True:
         opcao = input("Digite 1 para sair: ")
         if opcao == "1":
             break # Destrói o loop imediatamente


💡 SOBRE O 'DO WHILE' EM PYTHON:
Python não tem um comando 'do while'. Para fazer um código rodar pelo menos 
uma vez antes de testar a condição, usamos a estrutura do 'While True' com 
um 'if' e 'break' na última linha do bloco.
===============================================================================
"""



lista_temas = [texto1, texto2, texto3, texto4]



while True:

    opcao = input("Digite o número do tema que quer estudar: ")


    if opcao == "1":
        meu_objeto = caderno("CURSO DE LOGÍCA DE PROGRAMAÇÃO (by Felipe)", "tema: Fundamentos e Tipos de Dados", lista_temas [0])
        meu_objeto.exibir_caderno()


    elif opcao =="2":
        meu_objeto = caderno("CURSO DE LOGÍCA DE PROGRAMAÇÃO (by Felipe)", "tema: Operadores", lista_temas [1])
        meu_objeto.exibir_caderno()


    elif opcao =="3":
        meu_objeto = caderno("CURSO DE LOGÍCA DE PROGRAMAÇÃO (by Felipe)", "tema: Manipulação de Strings", lista_temas [2])
        meu_objeto.exibir_caderno()


    elif opcao =="4":
        meu_objeto = caderno("CURSO DE LOGÍCA DE PROGRAMAÇÃO (by Felipe)", "tema: Estruturas de Controle", lista_temas [3])
        meu_objeto.exibir_caderno()


    elif opcao == "5":
        meu_objeto = caderno("CURSO DE LOGÍCA DE PROGRAMAÇÃO (by Felipe)", "tema: Estruturas de Dados", lista_temas [4])