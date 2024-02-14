"""
##Funções de segregação

"""

import pandas as pd
import os

def separamento_por_mes(ano, mes, list_ano):
    sublista_mes = [item for item in list_ano if item.startswith(ano + ' - ' + mes)]
    valores_totais={}
    erros_dic={}

    for mercado in sublista_mes:
        caminho_do_csv = '/home/rias/Documentos/Felipeaaaummm/'+ ano +'/' + mercado
        nome_do_mercado = os.path.splitext(mercado.replace(ano + ' - ' + mes, '').replace('.csv', '').strip())[0]

    # Verifica se o arquivo existe antes de tentar lê-lo
        if os.path.exists(caminho_do_csv):
            df = pd.read_csv(caminho_do_csv, index_col=[0, 1])
            valor_total = df.xs(('Valor Total', 'marca'))['Total/Int'].values[0]


            if valor_total != '#DIV/0!' and valor_total != '#VALUE!' and valor_total != 'TOTAL' and valor_total != '#REF!':
                if isinstance(valor_total, str):
                    if valor_total.startswith("R$"):
                        valor_total = valor_total.replace(",", ".")
                        valor_total = valor_total.replace(".", "", 1)
                        valor_total = valor_total.replace("R$", "").strip()
                valores_totais[nome_do_mercado] = valor_total
            else:
                print("Encontrado Erro!!!")
                erros_dic[nome_do_mercado] = valor_total
        else:
            print(f"Arquivo não encontrado: {caminho_do_csv}")
    return valores_totais #erros_dic



# Função para calcular a média dos valores acima de 850 em um dicionário


def verificar_se_vende_todos(ano, mes, list_ano):
    sublista_mes = [item for item in list_ano if item.startswith(ano + ' - ' + mes)]
    vendem_todos= []
    print()
    for mercado in sublista_mes:
        caminho_do_csv = '/home/rias/Documentos/Felipeaaaummm/'+ ano +'/' + mercado
        nome_do_mercado = os.path.splitext(mercado.replace(ano + ' - ' + mes, '').replace('.csv', '').strip())[0]

    # Verifica se o arquivo existe antes de tentar lê-lo
        if os.path.exists(caminho_do_csv):
            tem_todos = True
            df = pd.read_csv(caminho_do_csv, index_col=[0, 1])
            all_preco = []
            all_indice = df.index.dropna().tolist()
            for nome_produto, categoria in all_indice:
                if categoria == "preço" and nome_produto != 'ABSORVENTE (pac. 8 unid.)' and nome_produto != 'Valor Total':
                    if nome_produto in df.index:
                        preco = df.loc[nome_produto]['Total'].iloc[1]
                        if pd.isna(preco) or preco == '0' or preco == 0:
                            print(mercado + ' Falta ' + nome_produto)
                            tem_todos = False
                        all_preco.append(preco)
                    else:
                        print(f"NOME NÃO EXISTE: {nome_produto}")
            if tem_todos:
                vendem_todos.append(nome_do_mercado)
        else:
            print(f"Arquivo não encontrado: {caminho_do_csv}")
    return vendem_todos

def os_mercados_mais_baratos_por_mes(mes_a_mes, mercados_vende_tudo):
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
