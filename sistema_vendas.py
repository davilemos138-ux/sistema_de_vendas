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
               item = {
                   "qtd": qtd_produto,
                   "nome": estoque_produtos[id_produto]["nome"],
                   "preco": estoque_produtos[id_produto]["preco"],
                   "preco_total": qtd_produto * estoque_produtos[id_produto]["preco"]
               }
               carrinho.append(item)
               estoque_produtos[id_produto]["quantidade"] -= qtd_produto
               print(item)
            else:
                print(f"Quantidade indisponível, temos apenas {estoque_produtos[id_produto]["quantidade"]} no estoque.")

        else:
            print("ID informado não existe no estoque!")



    elif opcao == 3:
        if carrinho:

            print("Visualizando carrinho")
            subtotal = 0
            for i in carrinho:
                print(f"{i["qtd"]}x {i["nome"]} no valor R$ {i["preco"]}(cada)\nTotal R${i["preco_total"]} ")
                subtotal += i["preco_total"]
            print(f"Subtotal da Compra R${subtotal}")

    elif opcao == 4:

        if carrinho:
            print("<>" * 15)
            print("\n=== Finalizar Compra ===")
            print("<>" * 15)
            total_compra = sum(item["preco_total"] for item in carrinho)
            cupom = input("Digite um cupom (ou pressione Enter): ").upper()
            desconto = 0
            if cupom == "DEV10":
                desconto = total_compra * 0.1
                print("Cupom Valido: Voce obteve 10% de desconto.")
            elif cupom == "DEV20" and total_compra > 500:
                desconto = total_compra * 0.2
                print("Cupom valido: Voce obteve 20% de desconto.")
            elif len(cupom) == 0:
                print("Nenhum cupom adicionado.")
            else:
                print("Cupom invalido, nenhum desconto adicionado.")

            total = total_compra - desconto

            print("------RESUMO DO PEDIDO-------")
            print(f"Subtotal da compra: R${subtotal:.2f}")
            print(f"Desconto: R$ {desconto:.2f}")
            print(f"Valor final: R${subtotal - desconto:.2f}")
            print("-" * 30)
            carrinho.clear()
        else:
            print("Não há itens no carrinho para finalizar.")


    elif opcao == 5:
        print("<>" * 15)
        print("Encerrando!!!")
        print("<>" * 15)
        break
    else:
        print("Opção invalida")






