import opt

def menu():

    print("Bem-vindo ao sistema de visualização de dados:")
    print("1. Plotar gráfico do preço de todos os mercados de um mês")
    print("2. Plotar médias mensais de um ano")
    print("3. Plotar mercados mais baratos de um ano mês a mês")
    print("4. EScrever o preço dos mercados por subcategoria")
    print("0. Sair")

    op = input("Escolha uma opção: ")

    return op

def main():

    while True:

        opcao = menu()

        if opcao == '1':
            opt.op_1()
        elif opcao == '2':
            opt.op_2()
        elif opcao == '3':
            opt.op_3()
        elif opcao == '4':
            opt.op_4()
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

main()