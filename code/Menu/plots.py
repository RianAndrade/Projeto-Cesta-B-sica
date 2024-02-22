import matplotlib.pyplot as plt
import seaborn as sns

def imprimir_dados_separados_por_tipo(dados):
    for mes, lojas in dados.items():
        print(mes)
        for loja, categorias in lojas.items():
            print(f"\t{loja}:")
            for categoria, valor in categorias.items():
                print(f"\t\t{categoria}: R${valor:.2f}")

def plot_grafico_medias_variacao(medias_por_mes, variacao_percentual):

    """
    Plota um gráfico de barras das médias mensais e inclui a variação percentual entre os meses.

    Parâmetros:
    - medias_por_mes (dict): Dicionário contendo as médias por mês.
    - variacao_percentual (dict): Dicionário contendo a variação percentual entre os meses.

    Retorna:
    - None
    """
        
    nome_mes = list(medias_por_mes.keys())
    valores = [float(valor) for valor in medias_por_mes.values()]

    sns.set_theme(style="whitegrid", palette="pastel")
    sns.set_palette("pastel")

    # Definindo uma paleta de cores com um tom de azul escuro pastel
    cor_azul = sns.color_palette("deep")[0]


    fig, ax1 = plt.subplots(figsize=(12, 8), facecolor="#f5f5f5")

    ax = sns.barplot(x=nome_mes, y=valores, color=cor_azul)

    cor_vermelho_pastel = (1.0, 0.8, 0.8)
    for limite in range(200, int(max(valores)) + 200, 200):
        ax1.axhline(limite, color='black', linestyle='--', linewidth=1)

    for i in range(len(nome_mes)-1):
        ax1.plot([i, i+1], [valores[i] + 10, valores[i+1] + 10], color=sns.color_palette("pastel")[3], linestyle='-', linewidth=3.5)

    for i, (mes, variacao) in enumerate(variacao_percentual.items()):
        ax1.text(i, valores[i] + 15, f"{variacao}%", ha='center', va='bottom', color='black')

    ax1.set_xlabel('Meses')
    ax1.set_ylabel('Médias por Mês', color='Black')
    ax1.set_title('Médias Mensais e Variação Percentual')

    plt.xticks(range(len(nome_mes)), nome_mes, rotation=45, ha='right')
    plt.yticks(range(0, int(max(valores)) + 200, 200))

    plt.savefig('grafico_com_linhas_subplots.png')
    plt.show()


def plotar_mercados_de_um_mes(valores_totais, ano, mes):

    """
    Plota um gráfico de barras dos valores totais dos mercados para um determinado mês e ano.

    Parâmetros:
    - valores_totais (dict): Dicionário contendo os valores totais de cada mercado.
    - ano (str): Ano dos dados a serem plotados.
    - mes (str): Mês dos dados a serem plotados.

    Retorna:
    - None
    """

    # Separando chaves e valores
    nomes_mercados = list(valores_totais.keys())
    valores = [float(valor) for valor in valores_totais.values()]

    sns.set_theme(style="whitegrid", palette="pastel")
    sns.set_palette("pastel")

    # Definindo uma paleta de cores com um tom de azul escuro pastel
    cor_azul = sns.color_palette("deep")[0]

    # Criando o gráfico de barras
    plt.figure(figsize=(12, 8), facecolor="#f5f5f5")

    # Utilizando barplot do Seaborn com a paleta de cores e cor de fundo definidas
    ax = sns.barplot(x=nomes_mercados, y=valores, color=cor_azul)

    # Adicionando linhas tracejadas a cada intervalo de 200
    for limite in range(200, int(max(valores)) + 200, 200):
        plt.axhline(limite, color='black', linestyle='--', linewidth=0.8)

    plt.xlabel('Mercados')
    plt.ylabel('Valores Totais')
    plt.title('Preço da Cesta Básica - ' + ano + ' - ' + mes)

    # Adicionando cor de fundo
    ax.set_facecolor("#f5f5f5")  # Altere para a cor desejada

    plt.xticks(rotation=45, ha='right')  # Ajustando os espaçamentos
    plt.yticks(range(0, int(max(valores)) + 200, 200))  # Ajustando os intervalos no eixo y
    plt.tight_layout()

    # Salvando o grafico para poder baixar
    plt.savefig('grafico.png')

    # Exibindo o gráfico
    plt.show()


def plotar_os_mais_baratos(mais_barato_ano):
    """
    Plota um gráfico de barras dos três mercados mais baratos para cada mês.

    Parâmetros:
    - mais_barato_ano (dict): Dicionário contendo os três mercados mais baratos para cada mês.

    Retorna:
    - None
    """
    # Cores para os mercados
    cores = ['b', 'g', 'r']

    # Largura das barras
    largura_barra = 0.25  # Ajuste o valor conforme necessário

    # Configurações do gráfico
    plt.figure(figsize=(20, 8))

    # Plotagem
    posicao_mes = 0
    for mes, mercados_precos in mais_barato_ano.items():
        if not mercados_precos:  # Verifica se a lista de mercados e preços está vazia
            continue
        mercados, precos = zip(*mercados_precos)
        # Espaço entre cada mercado dentro do mês
        espaco_entre_mercados = 0.05  # Ajuste o valor conforme necessário
        # Posições para as barras dentro de cada mês
        posicoes_barras = [posicao_mes + i * (largura_barra + espaco_entre_mercados) for i in range(len(mercados_precos))]
        for i, preco in enumerate(precos):
            # Adicionando o nome do mercado dentro da barra, letra por letra com quebra de linha
            for j, letra in enumerate(mercados[i]):
                plt.text(posicoes_barras[i], preco - j * 30 - 40, letra, ha='center', va='top', fontsize=10)  # Ajuste da posição vertical
            # Adicionando o preço acima de cada barra
            plt.text(posicoes_barras[i], preco + 50, f'{preco:.2f}', ha='center', va='bottom', fontsize=8, color='black')
        # Plotando as barras após ajustar as posições
        plt.bar(posicoes_barras, precos, color=cores[:len(precos)], width=largura_barra)

        posicao_mes += 1

    # Configurações dos eixos
    plt.xlabel('Meses')
    plt.ylabel('Preços')
    plt.title('Preços dos três mercados mais baratos por mês')
    plt.xticks(range(len(mais_barato_ano)), mais_barato_ano.keys())

    # Exibir o gráfico
    plt.tight_layout()
    plt.show()

def plotar_grafico_de_linhas_varição_por_subcategoria(mais_barato_ano):
    """
    Plota um gráfico de linhas mostrando os preços mais baixos para cada categoria em cada mês.

    Parâmetros:
    - mais_barato_ano (dict): Dicionário contendo os preços mais baixos para cada categoria em cada mês.

    Retorna:
    - None
    """
    # Categorias disponíveis
    categorias = ["Alimentos", "Limpeza", "Higiene"]

    # Cores para as categorias
    cores = ['b', 'g', 'r']

    # Configurações do gráfico
    plt.figure(figsize=(12, 6))

    # Plotagem
    for i, categoria in enumerate(categorias):
        meses = list(mais_barato_ano.keys())
        precos = [list(mais_barato_ano[mes][categoria].values())[0] for mes in meses]
        plt.plot(meses, precos, marker='o', linestyle='-', color=cores[i], label=categoria)

    # Configurações dos eixos
    plt.xlabel('Meses')
    plt.ylabel('Preços')
    plt.title('Preços mais baixos por categoria em cada mês')
    plt.legend()

    # Exibir o gráfico
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
