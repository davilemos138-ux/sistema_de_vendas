estoque_produtos = {

    1: {"nome": "Chuteira Nike", "preço": 800.00, "quantidade": 40},
    2: {"nome": "Caneleira", "preço": 150.00, "quantidade":50},
    3: {"nome": "Bola de Futebol", "preço": 300.00, "quantidade": 125},
    4: {"nome": "Meião", "preço": 80.00, "quantidade": 200},
    5: {"nome": "Luva de Goleiro", "preço": 580.00, "quantidade": 40},
    6: {"nome": "Calção", "preço": 120.00, "quantidade": 100}
}

carrinho = []

while True:

    print("*"*30)
    print("Seja Bem Vindo a Minha Loja ")
    print("*"*30)

    print ("[1] Visualizar estoque")
    print ("[2] Adicionar item ao carrinho")
    print ("[3] Visualizar carrinho")
    print ("[4] Finalizar compra")
    print ("[5] Sair do sistema ")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Visualizando Estoque")
        for k, v in estoque_produtos.items():
            print(f"{k}:{v}")

    elif opcao == 2:
        print("Adicionando itens ao carrinho")
        id_produto = int(input("Qual ID do produto voce deseja comprar? "))
        if id_produto in estoque_produtos:
            qtd_produto =int(input("Quantas unidades voce deseja?"))
            if qtd_produto <= 0:
                print("Quantidade inválida!")
            elif qtd_produto <= estoque_produtos[id_produto]["quantidade"]:
                carrinho.append(estoque_produtos[id_produto])
                estoque_produtos[id_produto]["quantidade"] -= qtd_produto


    elif opcao == 3:
        print("Visualizando carrinho")

    elif opcao == 4:
        print("Finalizando Compra")

    elif opcao == 5:
        print("Saindo...")







