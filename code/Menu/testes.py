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


plots.imprimir_dados_separados_por_tipo(inicializarVar.separado_por_tipo_2023)