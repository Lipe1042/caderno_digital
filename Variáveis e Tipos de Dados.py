while True:
    print("""
                    ============================================================
                                CURSO DE LÓGICA DE PROGRAMAÇÃO (by Felipe)
                    ============================================================
                    [1] Variáveis e Tipos de Dados
""")
    
    opcao = input("Digite o número do tema que quer estudar:")

    if opcao == "1":

        print("""
-
                    ---------------------------------------------------------
                                    1. VARIÁVEIS E TIPOS 
                    ---------------------------------------------------------
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
""")

    opcao = input("\nPressione ENTER para voltar ao Menu Principal")
    if opcao == "sair":
        break