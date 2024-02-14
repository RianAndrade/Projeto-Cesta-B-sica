

"""##Funções de calculo"""

def calcular_media_acima_de_850(dicionario_ano):
    media_mes_a_mes = {}
    for mes in dicionario_ano.keys():
        valores_acima_de_850 = [float(valor) for valor in dicionario_ano[mes].values() if float(valor) > 850]

        media_mes_a_mes[mes] = round(sum(valores_acima_de_850) / len(valores_acima_de_850), 2)
    return media_mes_a_mes

def varicao_percentual_ano(media_por_mes):

    variacao_percentual = {}

    meses = list(media_por_mes.keys())
    for i in range(len(meses)):
        mes_atual = meses[i]
        mes_seguinte = meses[i - 1]
        if mes_atual.startswith("1") and mes_atual[1] != "0" and mes_atual[1] != "1" and mes_atual[1] != "2":
            variacao_percentual[mes_atual] = 0
        else:
            media_atual = media_por_mes[mes_atual]
            media_seguinte = media_por_mes[mes_seguinte]
            if media_atual > 0:
                variacao = ((media_seguinte - media_atual) / media_atual) * 100
                variacao_percentual[mes_atual + '-' + mes_seguinte] = (round(variacao, 2))*(-1)
    return variacao_percentual
