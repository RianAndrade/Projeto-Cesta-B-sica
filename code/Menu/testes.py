import os
import pandas as pd
import inicializarVar
import segregacao
import matplotlib.pyplot as plt
import plots


'''
    1 - Problema encontrado : A função segregação.separado_por_tipo_2023 esta com problemas para efetuar o 
    calculo em novembro de 2023, aparentemente o problema esta no mercado BH
'''
def os_mercados_mais_baratos_por_mes(mes_a_mes, mercados_vende_tudo):
    """
    Encontra os mercados mais baratos para cada mês.

    Parâmetros:
    - mes_a_mes (dict): Dicionário contendo os preços para cada mês.
    - mercados_vende_tudo (dict): Dicionário contendo os mercados que vendem todos os produtos para cada mês.

    Retorna:
    - mercados_mais_baratos_por_mes (dict): Dicionário contendo os três mercados mais baratos para cada mês.
    """
    mercados_mais_baratos_por_mes = {}

    for mes, mercados in mercados_vende_tudo.items():
        mercados_disponiveis = mercados.copy()

        if mes in mes_a_mes:
            precos = mes_a_mes[mes]
            precos = {mercado: float(preco) for mercado, preco in precos.items()}

            # Verifica se o mercado está presente nos preços antes de ordená-los
            mercados_ordenados = [mercado for mercado in mercados_disponiveis if mercado in precos]
            mercados_ordenados = sorted(mercados_ordenados, key=precos.get)

            tres_mais_baratos = [(mercado, precos[mercado]) for mercado in mercados_ordenados[:3]]
            # Se houver menos de 3 mercados, preencha com "SEM MERCADO"
            while len(tres_mais_baratos) < 3:
                tres_mais_baratos.append(("SEM MERCADO", 800))

            mercados_mais_baratos_por_mes[mes] = tres_mais_baratos

    return mercados_mais_baratos_por_mes


print(inicializarVar.mercados_2024_vende_tudo)