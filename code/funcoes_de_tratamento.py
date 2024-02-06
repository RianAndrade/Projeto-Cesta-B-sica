import pandas as pd

pd.options.display.max_rows = None
pd.options.display.max_columns = None

def tratamento_tabela(df):
    # Trocar os nomes das colunas e colocar o nome "ign" nas que devem ser removidas
    novos_nomes = {'Unnamed: 0': 'ign', 'Unnamed: 1': 'Produto',
                'Unnamed: 2': 'ign', 'Unnamed: 3': 'Marca1/Preço1',
                'Unnamed: 4': 'Marca2/Preço2', 'Unnamed: 5': 'Marca3/Preço3',
                'Unnamed: 6': 'Total', 'Unnamed: 7': 'Media', 'Unnamed: 8': 'ign',
                'Unnamed: 9': 'Quantidade/Int', 'Unnamed: 10': 'ign', 'Unnamed: 11': 'Total/Int'}
    df.rename(columns=novos_nomes, inplace=True)

    # Remover as colunas nomeadas com "ign", e a linha 0 do índice, pois era um "ign"
    colunas_para_remover = ['ign']
    indices_para_remover = [74, 75, 76]
    df = df.drop(columns=colunas_para_remover)
    df = df.drop(indices_para_remover)
    df.at[78, 'Produto'] = 'Valor Total'
    df = df.drop(0)
    df.reset_index(inplace=True)

    # Chamar a função sub_produto
    y = 0
    while(True):
        df.iloc[y + 1, 0] = df.iloc[y, 0]
        df.iloc[y, 4] = "Total"
        df.iloc[y, 5] = "Media"
        df.iloc[y, 6] = "Quantidade"
        df.iloc[y, 7] = "TOTAL"
        y = y + 2
        if y == len(df.index)-1:
            break

    df.set_index(['Produto', df.groupby('Produto').cumcount()], inplace=True)
    df.index = df.index.set_levels(['marca', 'preço'], level=1)
    df.index.names = ['Produto', 'Tipo']
    return df

def convert_download(caminho_dos_caminhos, nomes_dos_meses, ano, nome_lista, contador):
    df_all = pd.ExcelFile(caminho_dos_caminhos)
    contador = contador + 1 
    nome_das_abas = df_all.sheet_names
    for aba in nome_das_abas:
        nome = f"{ano} - {contador} {nomes_dos_meses} {aba}.csv"
        df_aux = pd.read_excel(df_all, sheet_name=aba)
        if df_aux.shape[0] > 70:
            print(nome)
            df_aux = tratamento_tabela(df_aux)
            nome_lista.append(nome)
            df_aux.to_csv(nome, index=True)
    return contador

