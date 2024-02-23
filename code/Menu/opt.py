import plots
import os
import inicializarVar


def linha():
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


def op_1():
    os.system('clear')
    linha()
    print("Você escolheu a opção 1.")
    linha()

    print('Anos disponiveis \n -2022 \n -2023 \n -2024')

    linha()

    ano = input('Qual ano você deseja: ')
    os.system('clear')
    print('Meses disponíveis para 2022')

    linha()

    if ano == '2022':
        for x in inicializarVar.nomes_dos_meses_2022:
            print(f"-{x}")

        linha()

        mes_num = int(input("Qual o mês: "))
        os.system('clear')
        mes = inicializarVar.nomes_dos_meses_2022[mes_num - 1]
        plots.plotar_mercados_de_um_mes(inicializarVar.mes_a_mes_2022[mes], ano, mes)

    elif ano == '2023':
        for x in inicializarVar.nomes_dos_meses_2023:
            print(f"-{x}")

        linha()

        mes_num = int(input("Qual o mês: "))
        os.system('clear')
        mes = inicializarVar.nomes_dos_meses_2023[mes_num - 1]
        plots.plotar_mercados_de_um_mes(inicializarVar.mes_a_mes_2023[mes], ano, mes)
    
    elif ano == '2024':
        for x in inicializarVar.nomes_dos_meses_2024:
            print(f"-{x}")

        linha()

        mes_num = int(input("Qual o mês: "))
        os.system('clear')
        mes = inicializarVar.nomes_dos_meses_2024[mes_num - 1]
        plots.plotar_mercados_de_um_mes(inicializarVar.mes_a_mes_2024[mes], ano, mes)

    else:
        print('Ano indisponível')


def op_2():
    os.system('clear')
    linha()
    print("Você escolheu a opção 2.")
    linha()

    print('Anos disponiveis \n -2022 \n -2023 \n -2024')

    linha()

    ano = input('Qual ano você deseja: ')
    os.system('clear')


    linha()

    if ano == '2022':
        plots.plot_grafico_medias_variacao(inicializarVar.medias_por_mes_2022, inicializarVar.variacao_2022)

    elif ano == '2023':
        plots.plot_grafico_medias_variacao(inicializarVar.medias_por_mes_2023, inicializarVar.variacao_2023)
    
    elif ano == '2024':
        plots.plot_grafico_medias_variacao(inicializarVar.medias_por_mes_2024, inicializarVar.variacao_2024)

    else:
        print('Ano indisponível')

def op_3():
    os.system('clear')
    linha()
    print("Você escolheu a opção 3.")
    linha()

    print('Anos disponiveis \n -2022 \n -2023 \n -2024')

    linha()

    ano = input('Qual ano você deseja: ')
    os.system('clear')


    linha()

    if ano == '2022':
        plots.plotar_os_mais_baratos(inicializarVar.mais_baratos_2022)

    elif ano == '2023':
        plots.plotar_os_mais_baratos(inicializarVar.mais_baratos_2023)
    
    elif ano == '2024':
        plots.plotar_os_mais_baratos(inicializarVar.mais_baratos_2024)

    else:
        print('Ano indisponível')

def op_4():
    os.system('clear')
    linha()
    print("Você escolheu a opção 4.")
    linha()

    print('Anos disponiveis \n -2022 \n -2023 \n -2024')

    linha()

    ano = input('Qual ano você deseja: ')
    os.system('clear')
    print('Meses disponíveis para 2022')

    linha()

    if ano == '2022':
        plots.imprimir_dados_separados_por_tipo(inicializarVar.separado_por_tipo_2022)

        linha()

    elif ano == '2023':
        plots.imprimir_dados_separados_por_tipo(inicializarVar.separado_por_tipo_2023)

        linha()
    elif ano == '2024':
        plots.imprimir_dados_separados_por_tipo(inicializarVar.separado_por_tipo_2024)

        linha()

    else:
        print('Ano indisponível')


def op_5():
    os.system('clear')
    linha()
    print("Você escolheu a opção 5.")
    linha()

    print('Anos disponiveis \n -2022 \n -2023 \n -2024')

    linha()

    ano = input('Qual ano você deseja: ')
    os.system('clear')
    print('Meses disponíveis para 2022')

    linha()

    if ano == '2022':
        plots.print_mais_baratos_no_mes_por_subcategoria(inicializarVar.mais_baratos_no_mes_por_subcategoria_2022)

        linha()

    elif ano == '2023':
        plots.print_mais_baratos_no_mes_por_subcategoria(inicializarVar.mais_baratos_no_mes_por_subcategoria_2023)

        linha()
    
    elif ano == '2024':
        plots.print_mais_baratos_no_mes_por_subcategoria(inicializarVar.mais_baratos_no_mes_por_subcategoria_2024)

        linha()

    else:
        print('Ano indisponível')

def op_6():
    os.system('clear')
    linha()
    print("Você escolheu a opção 5.")
    linha()

    print('Anos disponiveis \n -2022 \n -2023 \n -2024')

    linha()

    ano = input('Qual ano você deseja: ')
    os.system('clear')
    print('Meses disponíveis para 2022')

    linha()

    if ano == '2022':
        plots. plotar_grafico_de_linhas_varição_por_subcategoria(inicializarVar.mais_baratos_no_mes_por_subcategoria_2022)

        linha()

    elif ano == '2023':
        plots. plotar_grafico_de_linhas_varição_por_subcategoria(inicializarVar.mais_baratos_no_mes_por_subcategoria_2023)

        linha()
    
    elif ano == '2024':
        plots. plotar_grafico_de_linhas_varição_por_subcategoria(inicializarVar.mais_baratos_no_mes_por_subcategoria_2024)

        linha()

    else:
        print('Ano indisponível')


