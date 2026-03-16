# Função para adicionar materiais ao stock
def adicionar_material(stock):
    nome = input("Nome do material: ")
    if nome in stock:
        print("O material já existe no stock!")
    else:
        quantidade = int(input(f"Quantidade inicial de {nome}: "))
        stock[nome] = quantidade
        print(f"{nome} adicionado com sucesso!")


# Função para consultar o stock de um material
def consultar_stock(stock):
    nome = input("Nome do material para consulta: ")
    if nome in stock:
        print(f"O stock atual de {nome} é: {stock[nome]}")
    else:
        print(f"{nome} não encontrado no stock.")


# Função para atualizar o stock
def atualizar_stock(stock):
    nome = input("Nome do material a atualizar: ")
    if nome in stock:
        operacao = input("Deseja adicionar (A) ou remover (R)? ").upper()
        quantidade = int(input("Quantidade: "))

        if operacao == "A":
            stock[nome] += quantidade
            print(f"{quantidade} unidade(s) adicionada(s) ao stock de {nome}.")

        elif operacao == "R":
            if quantidade <= stock[nome]:
                stock[nome] -= quantidade
                print(f"{quantidade} unidade(s) removida(s) do stock de {nome}.")
            else:
                print("Quantidade insuficiente em stock!")
        else:
            print("Operação inválida!")
    else:
        print(f"{nome} não encontrado no stock.")


# Função para exibir o estado geral do stock
def exibir_stock(stock):
    print("\nEstado Geral do Stock:")
    print("Material\tQuantidade")
    print("-" * 30)

    for material, quantidade in stock.items():
        print(f"{material}\t\t{quantidade}")



# Função principal (menu)
def main():
    stock = {}

    while True:
        print("""
  ____           _        ____  _             _    
 / ___| ___  ___| |_ ___ / ___|| |_ ___   ___| | __
| |  _ / _ \/ __| __/ _ \\\___ \| __/ _ \ / __| |/ /
| |_| |  __/\__ \ || (_) |___) | || (_) | (__|   < 
 \____|\___||___/\__\___/|____/ \__\___/ \___|_|\_\\

              GESTÃO DE STOCK
""")

        print("1. Adicionar Material")
        print("2. Consultar Stock")
        print("3. Atualizar Stock")
        print("4. Exibir Stock Geral")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")


        if opcao == "1":
            adicionar_material(stock)

        elif opcao == "2":
            consultar_stock(stock)

        elif opcao == "3":
            atualizar_stock(stock)

        elif opcao == "4":
            exibir_stock(stock)

        elif opcao == "5":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
