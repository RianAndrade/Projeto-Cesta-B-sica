import os
import pandas as pd
import inicializarVar
import segregacao
import matplotlib.pyplot as plt
import plots


mais_baratos_no_mes_por_subcategoria_2023 = segregacao.encontrar_mais_baratos_por_mes_segregado_em_tipos(inicializarVar.separado_por_tipo_2023, inicializarVar.mercados_2023_vende_tudo)


'''
    A função segregação.separado_por_tipo_2023 esta com problemas para efetuar o 
    calculo em novembro de 2023, aparentemente o problema esta no mercado BH
'''
def print_mais_baratos_no_mes_por_subcategoria(dados):

    for mes, categorias in dados.items():
        print(f"{mes}:")
        for categoria, mercados_precos in categorias.items():
            print(f"  {categoria}:")
            for mercado, preco in mercados_precos.items():
                print(f"    - {mercado}: R${preco:.2f}")


def imprimir_dados_separados_por_tipo(dados):
    for mes, lojas in dados.items():
        print(mes)
        for loja, categorias in lojas.items():
            print(f"\t{loja}:")
            for categoria, valor in categorias.items():
                print(f"\t\t{categoria}: R${valor:.2f}")

imprimir_dados_separados_por_tipo(inicializarVar.separado_por_tipo_2023)