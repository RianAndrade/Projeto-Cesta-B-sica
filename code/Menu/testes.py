import os
import pandas as pd
import inicializarVar
import segregacao
import matplotlib.pyplot as plt
import plots


def encontrar_mais_baratos_por_mes(dados, mercado_vende_tudo):
    mais_baratos = {}
    for mes, mercados in dados.items():
        mais_baratos[mes] = {"Alimentos": {}, "Limpeza": {}, "Higiene": {}}
        if mes in mercado_vende_tudo:  # Verifica se há dados de mercado para este mês
            mercados_permitidos = mercado_vende_tudo[mes]
            for categoria in ["Alimentos", "Limpeza", "Higiene"]:
                preco_mais_baixo = float("inf")
                supermercado_mais_barato = ""
                for mercado in mercados_permitidos:
                    if mercado in mercados:  # Verifica se o mercado está presente nos dados
                        preco_produto = mercados[mercado].get(categoria)
                        if preco_produto is not None and preco_produto < preco_mais_baixo:
                            preco_mais_baixo = preco_produto
                            supermercado_mais_barato = mercado
                if supermercado_mais_barato:  # Verifica se encontrou algum mercado para esta categoria
                    mais_baratos[mes][categoria][supermercado_mais_barato] = preco_mais_baixo
    return mais_baratos

# Chamada da função para o ano de 2023 com a lista de nomes dos meses
resultado = encontrar_mais_baratos_por_mes(inicializarVar.separado_por_tipo_2023, inicializarVar.mercados_2023_vende_tudo)

print(resultado)

print(f'\n\n{inicializarVar.mercados_2023_vende_tudo["11 Novembro"]}')

#plots.plotar_grafico_de_linhas_varição_por_subcategoria(resultado)