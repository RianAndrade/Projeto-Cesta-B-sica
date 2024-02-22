"""##Funções de calculo"""

def calcular_media_acima_de_850(dicionario_ano):
    """
    Calcula a média dos valores acima de 850 para cada mês.

    Parâmetros:
    - dicionario_ano (dict): Dicionário contendo os valores totais de cada mercado para cada mês.

    Retorna:
    - media_mes_a_mes (dict): Dicionário contendo a média dos valores acima de 850 para cada mês.
    """
    media_mes_a_mes = {}  # Dicionário para armazenar a média dos valores acima de 850 para cada mês
    for mes in dicionario_ano.keys():  # Itera sobre os meses no dicionário
        # Filtra os valores acima de 850 e os converte para float
        valores_acima_de_850 = [float(valor) for valor in dicionario_ano[mes].values() if float(valor) > 850]
        # Calcula a média dos valores acima de 850 para o mês atual e arredonda para 2 casas decimais
        media_mes_a_mes[mes] = round(sum(valores_acima_de_850) / len(valores_acima_de_850), 2)
    return media_mes_a_mes  # Retorna o dicionário de médias por mês

def varicao_percentual_ano(media_por_mes):
    """
    Calcula a variação percentual entre as médias mensais.

    Parâmetros:
    - media_por_mes (dict): Dicionário contendo as médias por mês.

    Retorna:
    - variacao_percentual (dict): Dicionário contendo a variação percentual entre as médias mensais.
    """
    variacao_percentual = {}  # Dicionário para armazenar a variação percentual entre as médias mensais
    meses = list(media_por_mes.keys())  # Obtém a lista de meses
    for i in range(len(meses)):  # Itera sobre os meses
        mes_atual = meses[i]  # Mês atual
        mes_seguinte = meses[i - 1]  # Mês seguinte
        # Condição para evitar calcular a variação com o mês de dezembro
        if mes_atual.startswith("1") and mes_atual[1] != "0" and mes_atual[1] != "1" and mes_atual[1] != "2":
            variacao_percentual[mes_atual] = 0  # Define a variação como 0
        else:
            media_atual = media_por_mes[mes_atual]  # Média atual
            media_seguinte = media_por_mes[mes_seguinte]  # Média seguinte
            if media_atual > 0:  # Verifica se a média atual é maior que 0 para evitar divisão por zero
                # Calcula a variação percentual e arredonda para 2 casas decimais
                variacao = ((media_seguinte - media_atual) / media_atual) * 100
                # Armazena a variação percentual no dicionário
                variacao_percentual[mes_atual + '-' + mes_seguinte] = (round(variacao, 2)) * (-1)
    return variacao_percentual  # Retorna o dicionário de variações percentuais
