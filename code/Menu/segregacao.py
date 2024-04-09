"""
Funções de segregação

Este módulo contém funções para processar e analisar dados da recolha de preços da cesta básica na cidade de Januária.

"""

import pandas as pd
import os

def converter_str_int(valor_total):
    if isinstance(valor_total, str):
                    if valor_total.startswith("R$"):
                        valor_total = valor_total.replace(",", ".")
                        valor_total = valor_total.replace(".", "", 1)
                        valor_total = valor_total.replace("R$", "").strip()
    return valor_total

def separamento_por_mes(ano, mes, list_ano):
    """
    Separa os dados por mês e ano.

    Parâmetros:
    - ano (str): Ano dos dados a serem separados.
    - mes (str): Mês dos dados a serem separados.
    - list_ano (list): Lista de arquivos contendo os dados.

    Retorna:
    - valores_totais (dict): Dicionário contendo os valores totais de cada mercado para o mês e ano especificados.
    """
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
                valor_total = converter_str_int(valor_total)
                valores_totais[nome_do_mercado] = valor_total
            else:
                print("Encontrado Erro!!!")
                erros_dic[nome_do_mercado] = valor_total
        else:
            print(f"Arquivo não encontrado: {caminho_do_csv}")
    return valores_totais #erros_dic

def verificar_se_vende_todos(ano, mes, list_ano):
    """
    Verifica se todos os produtos estão disponíveis em todos os mercados para um determinado mês e ano.

    Parâmetros:
    - ano (str): Ano dos dados a serem verificados.
    - mes (str): Mês dos dados a serem verificados.
    - list_ano (list): Lista de arquivos contendo os dados.

    Retorna:
    - vendem_todos (list): Lista de mercados que vendem todos os produtos para o mês e ano especificados.
    """
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

def separar_por_tipo(ano, list_ano, nomes_meses):
    """
    Separa os mercados por tipo, sendo os tipos Alimentos, Higiene e Limpeza.

    Parâmetros:
    - ano (str): Ano dos dados a serem verificados.
    - mes (str): Mês dos dados a serem verificados.
    - list_ano (list): Lista de arquivos contendo os dados.
    -nomes_meses (list) : Lista do nome dos meses 

    Retorna: mercados_preco_por_categoria (dict): Dicionário contendo os meses com todos os mercados e os preços separados por categoria 

    - 
    """
    
    mercados_preco_por_categoria = {}

    for mes in nomes_meses:
        sublista_mes = [item for item in list_ano if item.startswith(ano + ' - ' + mes)]
        mercados_mes = {}
        for mercado in sublista_mes:
            caminho_do_csv = '/home/rias/Documentos/Felipeaaaummm/' + ano + '/' + mercado
            nome_do_mercado = os.path.splitext(mercado.replace(ano + ' - ' + mes, '').replace('.csv', '').strip())[0]

            if os.path.exists(caminho_do_csv):
                df = pd.read_csv(caminho_do_csv, index_col=[0, 1])
                all_indice = df.index.tolist()
                
                contador_nan, preco_alimentos, preco_limpeza, preco_higiene = 0, 0, 0, 0

                for nome_produto, categoria in all_indice:
                    if pd.isna(nome_produto):
                        contador_nan += 1
                    elif categoria == 'preço':
                        preco_produto = df.loc[nome_produto]['Total/Int'].iloc[1]
                        if preco_produto not in ['#DIV/0!', 'TOTAL', '#VALUE!', '#REF!', '########'] and not pd.isna(preco_produto):
                            preco_produto = converter_str_int(preco_produto)
                            if contador_nan < 2:
                                preco_alimentos += float(preco_produto)
                            elif contador_nan < 4:
                                preco_limpeza += float(preco_produto)
                            else:
                                preco_higiene += float(preco_produto)
                    elif nome_produto == 'Valor Total':
                        mercados_mes[nome_do_mercado] = {'Alimentos': round(preco_alimentos, 2), 'Limpeza':round(preco_limpeza, 2), 'Higiene':round(preco_higiene, 2)}
                        mercados_preco_por_categoria[mes] = mercados_mes
            else:
                print(f"Arquivo não encontrado: {caminho_do_csv}")
    return mercados_preco_por_categoria


def encontrar_mais_baratos_por_mes_segregado_em_tipos(dados, mercado_vende_tudo):
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
