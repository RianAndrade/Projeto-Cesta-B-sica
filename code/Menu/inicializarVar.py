import segregacao 
import calculos
import warnings
import os

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

"""##Funções de Plot"""

"""#Chamada das funções principais para inicialização

"""

list_2022 = ['2022 - 1 Março AZEVEDO.csv', '2022 - 1 Março BH.csv', '2022 - 1 Março BOM PREÇO.csv', '2022 - 1 Março CARIBÉ.csv', '2022 - 1 Março CESTÃO DA ECONOMIA.csv', '2022 - 1 Março GORDO.csv', '2022 - 1 Março KAMILA.csv', '2022 - 1 Março MONTALVÂNIA.csv', '2022 - 1 Março NACIONAL.csv', '2022 - 1 Março PAG POUCO.csv', '2022 - 1 Março PÃO DE MEL (BH2).csv', '2022 - 1 Março PORTO.csv', '2022 - 1 Março PREÇO BAIXO.csv', '2022 - 1 Março SUPER MAAR.csv', '2022 - 1 Março UNIÃO (MEGA FEIRA).csv', '2022 - 2 Abril AZEVEDO.csv', '2022 - 2 Abril BH.csv', '2022 - 2 Abril BH RODOVIARIA.csv', '2022 - 2 Abril BOM PREÇO.csv', '2022 - 2 Abril CARIBÉ.csv', '2022 - 2 Abril CARIBÉ 2.csv', '2022 - 2 Abril CESTÃO DA ECONOMIA.csv', '2022 - 2 Abril CESTÃO BAIRRO.csv', '2022 - 2 Abril KAMILA.csv', '2022 - 2 Abril MONTALVÂNIA.csv', '2022 - 2 Abril MONTALVÂNIA 2.csv', '2022 - 2 Abril NACIONAL.csv', '2022 - 2 Abril PAG POUCO.csv', '2022 - 2 Abril PORTO.csv', '2022 - 2 Abril PREÇO BAIXO 2.csv', '2022 - 2 Abril SUPER MAAR.csv', '2022 - 2 Abril UNIÃO (MEGA FEIRA).csv', '2022 - 2 Abril PREÇO BAIXO.csv', '2022 - 2 Abril ROCHA.csv', '2022 - 3 Maio AZEVEDO.csv', '2022 - 3 Maio BH RODOVIARIA.csv', '2022 - 3 Maio CARIBÉ 2.csv', '2022 - 3 Maio CESTÃO BAIRRO.csv', '2022 - 3 Maio GORDO.csv', '2022 - 3 Maio MONTALVÂNIA 2.csv', '2022 - 3 Maio NACIONAL.csv', '2022 - 3 Maio PORTO.csv', '2022 - 3 Maio PREÇO BAIXO.csv', '2022 - 3 Maio SUPER MAAR.csv', '2022 - 4 Junho BOM PREÇO.csv', '2022 - 4 Junho PÃO DE MEL(BH2).csv', '2022 - 4 Junho CARIBÉ 2.csv', '2022 - 4 Junho CESTÃO DA ECONOMIA(BAIRRO).csv', '2022 - 4 Junho MONTALVÂNIA.csv', '2022 - 4 Junho NACIONAL.csv', '2022 - 4 Junho GORDO.csv', '2022 - 4 Junho PORTO.csv', '2022 - 4 Junho PREÇO BAIXO.csv', '2022 - 4 Junho SUPER MAAR.csv', '2022 - 5 Julho BOM PREÇO.csv', '2022 - 5 Julho PÃO DE MEL(BH2).csv', '2022 - 5 Julho CARIBÉ 2.csv', '2022 - 5 Julho CESTÃO DA ECONOMIA(BAIRRO).csv', '2022 - 5 Julho MONTALVÂNIA.csv', '2022 - 5 Julho GORDO.csv', '2022 - 5 Julho NACIONAL.csv', '2022 - 5 Julho PORTO.csv', '2022 - 5 Julho PREÇO BAIXO.csv', '2022 - 5 Julho SUPER MAAR.csv', '2022 - 6 Agosto AZEVEDO.csv', '2022 - 6 Agosto BH.csv', '2022 - 6 Agosto BH RODOVIARIA.csv', '2022 - 6 Agosto CARIBÉ.csv', '2022 - 6 Agosto CESTÃO DA ECONOMIA.csv', '2022 - 6 Agosto KAMILA .csv', '2022 - 6 Agosto MONTALVÂNIA.csv', '2022 - 6 Agosto NACIONAL.csv', '2022 - 6 Agosto PAG POUCO.csv', '2022 - 6 Agosto PORTO.csv', '2022 - 6 Agosto PREÇO BAIXO.csv', '2022 - 6 Agosto SUPER MAAR.csv', '2022 - 6 Agosto UNIÃO (MEGA FEIRA).csv', '2022 - 6 Agosto ROCHA.csv', '2022 - 7 Setembro AZEVEDO.csv', '2022 - 7 Setembro BH.csv', '2022 - 7 Setembro BH RODOVIARIA.csv', '2022 - 7 Setembro BOM PREÇO.csv', '2022 - 7 Setembro CARIBÉ.csv', '2022 - 7 Setembro CARIBÉ 2.csv', '2022 - 7 Setembro CESTÃO DA ECONOMIA.csv', '2022 - 7 Setembro CESTÃO BAIRRO.csv', '2022 - 7 Setembro GORDO.csv', '2022 - 7 Setembro KAMILA.csv', '2022 - 7 Setembro MONTALVÂNIA.csv', '2022 - 7 Setembro MONTALVÂNIA 2 .csv', '2022 - 7 Setembro NACIONAL.csv', '2022 - 7 Setembro PAG POUCO.csv', '2022 - 7 Setembro PORTO.csv', '2022 - 7 Setembro PREÇO BAIXO.csv', '2022 - 7 Setembro SUPER MAAR.csv', '2022 - 7 Setembro UNIÃO (MEGA FEIRA).csv', '2022 - 7 Setembro ROCHA.csv', '2022 - 8 Outubro AZEVEDO.csv', '2022 - 8 Outubro BH.csv', '2022 - 8 Outubro BH RODOVIARIA.csv', '2022 - 8 Outubro BOM PREÇO.csv', '2022 - 8 Outubro CARIBÉ.csv', '2022 - 8 Outubro CARIBÉ 2.csv', '2022 - 8 Outubro CESTÃO DA ECONOMIA.csv', '2022 - 8 Outubro CESTÃO BAIRRO.csv', '2022 - 8 Outubro GORDO.csv', '2022 - 8 Outubro KAMILA.csv', '2022 - 8 Outubro MONTALVÂNIA.csv', '2022 - 8 Outubro MONTALVÂNIA 2.csv', '2022 - 8 Outubro NACIONAL .csv', '2022 - 8 Outubro  PAG POUCO.csv', '2022 - 8 Outubro PORTO.csv', '2022 - 8 Outubro PREÇO BAIXO.csv', '2022 - 8 Outubro SUPER MAAR.csv', '2022 - 8 Outubro UNIÃO (MEGA FEIRA).csv', '2022 - 8 Outubro ROCHA.csv', '2022 - 9 Novembro BOM PREÇO.csv', '2022 - 9 Novembro PÃO DE MEL(BH2).csv', '2022 - 9 Novembro CARIBÉ 2.csv', '2022 - 9 Novembro CESTÃO DA ECONOMIA(BAIRRO).csv', '2022 - 9 Novembro MONTALVÂNIA.csv', '2022 - 9 Novembro GORDO.csv', '2022 - 9 Novembro NACIONAL.csv', '2022 - 9 Novembro PORTO.csv', '2022 - 9 Novembro PREÇO BAIXO.csv', '2022 - 9 Novembro SUPER MAAR.csv', '2022 - 10 Dezembro BOM PREÇO.csv', '2022 - 10 Dezembro PÃO DE MEL(BH2).csv', '2022 - 10 Dezembro CARIBÉ 2.csv', '2022 - 10 Dezembro CESTÃO DA ECONOMIA(BAIRRO).csv', '2022 - 10 Dezembro MONTALVÂNIA.csv', '2022 - 10 Dezembro GORDO.csv', '2022 - 10 Dezembro SUPER MAAR.csv', '2022 - 10 Dezembro PORTO.csv', '2022 - 10 Dezembro PREÇO BAIXO.csv', '2022 - 10 Dezembro NACIONAL .csv']
list_2023 =['2023 - 1 Janeiro BOM PREÇO.csv', '2023 - 1 Janeiro PÃO DE MEL(BH2).csv', '2023 - 1 Janeiro CARIBÉ 2.csv', '2023 - 1 Janeiro CESTÃO DA ECONOMIA(BAIRRO).csv', '2023 - 1 Janeiro MONTALVÂNIA.csv', '2023 - 1 Janeiro GORDO.csv', '2023 - 1 Janeiro SUPER MAAR.csv', '2023 - 1 Janeiro PORTO.csv', '2023 - 1 Janeiro PREÇO BAIXO.csv', '2023 - 1 Janeiro NACIONAL .csv', '2023 - 2 Fevereiro BOM PREÇO.csv', '2023 - 2 Fevereiro PÃO DE MEL(BH2).csv', '2023 - 2 Fevereiro CARIBÉ 2.csv', '2023 - 2 Fevereiro CESTÃO DA ECONOMIA(BAIRRO).csv', '2023 - 2 Fevereiro MONTALVÂNIA.csv', '2023 - 2 Fevereiro PREÇO BAIXO..csv', '2023 - 2 Fevereiro PORTO.csv', '2023 - 2 Fevereiro SUPER MAAR.csv', '2023 - 2 Fevereiro NACIONAL .csv', '2023 - 3 Março BOM PREÇO.csv', '2023 - 3 Março BH- ATACADO.csv', '2023 - 3 Março UNIÃO MEGA FEIRAA.csv', '2023 - 3 Março ROCHA.csv', '2023 - 3 Março KAMILA.csv', '2023 - 3 Março TERRA- norte.csv', '2023 - 3 Março PAG POUCO.csv', '2023 - 3 Março CARIBÉ.csv', '2023 - 3 Março AZEVEDO.csv', '2023 - 3 Março BH RODOVIARIA.csv', '2023 - 3 Março CARIBÉ 2.csv', '2023 - 3 Março CESTÃO BAIRO.csv', '2023 - 3 Março MONTALVÂNIA.csv', '2023 - 3 Março CESTÃO DA ECONOMIA.csv', '2023 - 3 Março GORDO.csv', '2023 - 3 Março SUPER MAAR.csv', '2023 - 3 Março PORTO.csv', '2023 - 3 Março NACIONAL .csv', '2023 - 3 Março PREÇO BAIXO.csv', '2023 - 4 Abril BOM PREÇO.csv', '2023 - 4 Abril ROCHA.csv', '2023 - 4 Abril BH- ATACADO.csv', '2023 - 4 Abril AZEVEDO.csv', '2023 - 4 Abril CARIBÉ.csv', '2023 - 4 Abril CESTÃO DA ECONOMIA.csv', '2023 - 4 Abril KAMILA.csv', '2023 - 4 Abril TERRA NORTE.csv', '2023 - 4 Abril PAG POUCO.csv', '2023 - 4 Abril UNIÃO MEGA FEIRA.csv', '2023 - 4 Abril PÃO DE MEL(BH2).csv', '2023 - 4 Abril CARIBÉ 2.csv', '2023 - 4 Abril CESTÃO DA ECONOMIA(BAIRRO).csv', '2023 - 4 Abril MONTALVÂNIA.csv', '2023 - 4 Abril GORDO.csv', '2023 - 4 Abril SUPER MAAR.csv', '2023 - 4 Abril PORTO.csv', '2023 - 4 Abril PREÇO BAIXO.csv', '2023 - 4 Abril NACIONAL .csv', '2023 - 5 Maio BOM PREÇO.csv', '2023 - 5 Maio BH ATACADO.csv', '2023 - 5 Maio CARIBÉ.csv', '2023 - 5 Maio CESTÃO DA ECONOMIA.csv', '2023 - 5 Maio KAMILA.csv', '2023 - 5 Maio TERRA NORTE.csv', '2023 - 5 Maio PAG POUCO.csv', '2023 - 5 Maio ROCHA.csv', '2023 - 5 Maio UNIÃO MEGA FEIRA.csv', '2023 - 5 Maio PÃO DE MEL(BH2).csv', '2023 - 5 Maio CARIBÉ 2.csv', '2023 - 5 Maio CESTÃO DA ECONOMIA(BAIRRO).csv', '2023 - 5 Maio MONTALVÂNIA.csv', '2023 - 5 Maio SUPER MAAR.csv', '2023 - 5 Maio PREÇO BAIXO.csv', '2023 - 5 Maio NACIONAL .csv', '2023 - 6 Junho BOM PREÇO.csv', '2023 - 6 Junho BH ATACADO.csv', '2023 - 6 Junho CARIBÉ.csv', '2023 - 6 Junho CESTÃO DA ECONOMIA.csv', '2023 - 6 Junho KAMILA.csv', '2023 - 6 Junho MEGA FEIRA.csv', '2023 - 6 Junho PAG POUCO.csv', '2023 - 6 Junho ROCHA.csv', '2023 - 6 Junho TERRA NORTE.csv', '2023 - 6 Junho BH 2 rodoviária.csv', '2023 - 6 Junho CARIBÉ 2.csv', '2023 - 6 Junho CESTÃO DA ECONOMIA(BAIRRO).csv', '2023 - 6 Junho MONTALVÂNIA.csv', '2023 - 6 Junho SUPER MAAR.csv', '2023 - 6 Junho PREÇO BAIXO.csv', '2023 - 6 Junho NACIONAL .csv', '2023 - 7 Julho BOM PREÇO.csv', '2023 - 7 Julho BH ATACADO.csv', '2023 - 7 Julho CARIBÉ.csv', '2023 - 7 Julho CESTÃO DA ECONOMIA.csv', '2023 - 7 Julho KAMILA.csv', '2023 - 7 Julho TERRA NORTE.csv', '2023 - 7 Julho PAG POUCO.csv', '2023 - 7 Julho ROCHA.csv', '2023 - 7 Julho UNIÃO MEGA FEIRA.csv', '2023 - 7 Julho CARIBÉ 2.csv', '2023 - 7 Julho BH 2 rodoviária.csv', '2023 - 7 Julho CESTÃO DA ECONOMIA(BAIRRO).csv', '2023 - 7 Julho MONTALVÂNIA.csv', '2023 - 7 Julho SUPER MAAR.csv', '2023 - 7 Julho PREÇO BAIXO.csv', '2023 - 7 Julho NACIONAL .csv', '2023 - 8 Agosto CESTÃO BAIRRO.csv', '2023 - 8 Agosto BH ATACADO.csv', '2023 - 8 Agosto CARIBÉ.csv', '2023 - 8 Agosto CESTÃO DA ECONOMIA.csv', '2023 - 8 Agosto KAMILA.csv', '2023 - 8 Agosto TERRA NORTE.csv', '2023 - 8 Agosto PAG POUCO.csv', '2023 - 8 Agosto ROCHA.csv', '2023 - 8 Agosto UNIÃO MEGA FEIRA.csv', '2023 - 8 Agosto BH 2 rodoviária.csv', '2023 - 8 Agosto CARIBÉ 2.csv', '2023 - 8 Agosto BOM PREÇO .csv', '2023 - 8 Agosto MONTALVÂNIA.csv', '2023 - 8 Agosto SUPER MAAR.csv', '2023 - 8 Agosto PREÇO BAIXO.csv', '2023 - 8 Agosto NACIONAL .csv', '2023 - 9 Setembro CARIBÉ.csv', '2023 - 9 Setembro TERRA NORTE.csv', '2023 - 9 Setembro CESTÃO DA ECONOMIA.csv', '2023 - 9 Setembro KAMILA.csv', '2023 - 9 Setembro PAG POUCO.csv', '2023 - 9 Setembro ROCHA.csv', '2023 - 9 Setembro UNIÃO MEGA FEIRA.csv', '2023 - 9 Setembro BH 2 rodoviária.csv', '2023 - 9 Setembro BH ATACADO.csv', '2023 - 9 Setembro CESTÃO BAIRRO.csv', '2023 - 9 Setembro CARIBÉ 2.csv', '2023 - 9 Setembro BOM PREÇO .csv', '2023 - 9 Setembro MONTALVÂNIA.csv', '2023 - 9 Setembro SUPER MAAR.csv', '2023 - 9 Setembro PREÇO BAIXO.csv', '2023 - 9 Setembro NACIONAL .csv', '2023 - 10 Outubro BH ATACADO.csv', '2023 - 10 Outubro CARIBÉ.csv', '2023 - 10 Outubro CESTÃO DA ECONOMIA.csv', '2023 - 10 Outubro KAMILA.csv', '2023 - 10 Outubro TERRA NORTE.csv', '2023 - 10 Outubro ROCHA.csv', '2023 - 10 Outubro PAG POUCO.csv', '2023 - 10 Outubro UNIÃO MEGA FEIRA.csv', '2023 - 10 Outubro CESTÃO BAIRRO.csv', '2023 - 10 Outubro BH 2 rodoviária.csv', '2023 - 10 Outubro CARIBÉ 2.csv', '2023 - 10 Outubro BOM PREÇO .csv', '2023 - 10 Outubro MONTALVÂNIA.csv', '2023 - 10 Outubro SUPER MAAR.csv', '2023 - 10 Outubro PREÇO BAIXO.csv', '2023 - 10 Outubro NACIONAL .csv', '2023 - 11 Novembro CESTÃO BAIRRO.csv', '2023 - 11 Novembro BH ATACAD0.csv', '2023 - 11 Novembro CARIBÉ.csv', '2023 - 11 Novembro CESTÃO DA ECONOMIA.csv', '2023 - 11 Novembro KAMILA.csv', '2023 - 11 Novembro TERRA NORTE.csv', '2023 - 11 Novembro PAG POUCO.csv', '2023 - 11 Novembro ROCHA.csv', '2023 - 11 Novembro UNIÃO MEGA FEIRA.csv', '2023 - 11 Novembro BH 2 rodoviária.csv', '2023 - 11 Novembro CARIBÉ 2.csv', '2023 - 11 Novembro BOM PREÇO .csv', '2023 - 11 Novembro MONTALVÂNIA.csv', '2023 - 11 Novembro SUPER MAAR.csv', '2023 - 11 Novembro PREÇO BAIXO.csv', '2023 - 11 Novembro NACIONAL .csv', '2023 - 12 Dezembro BH ATACADO.csv', '2023 - 12 Dezembro CESTÃO DA ECONOMIA .csv', '2023 - 12 Dezembro CARIBÉ .csv', '2023 - 12 Dezembro KAMILA.csv', '2023 - 12 Dezembro TERRA NORTE.csv', '2023 - 12 Dezembro PAG POUCO.csv', '2023 - 12 Dezembro ROCHA.csv', '2023 - 12 Dezembro UNIÃO MEGA FEIRA.csv', '2023 - 12 Dezembro CESTÃO BAIRRO.csv', '2023 - 12 Dezembro BH 2 rodoviária.csv', '2023 - 12 Dezembro CARIBÉ 2.csv', '2023 - 12 Dezembro BOM PREÇO .csv', '2023 - 12 Dezembro MONTALVÂNIA.csv', '2023 - 12 Dezembro SUPER MAAR.csv', '2023 - 12 Dezembro PREÇO BAIXO.csv', '2023 - 12 Dezembro NACIONAL .csv']
list_2024 = ['2024 - 1 Janeiro BH ATACADO.csv', '2024 - 1 Janeiro CESTÃO DA ECONOMIA .csv', '2024 - 1 Janeiro CARIBÉ 2.csv', '2024 - 1 Janeiro KAMILA.csv', '2024 - 1 Janeiro TERRA NORTE.csv', '2024 - 1 Janeiro BOM PREÇO.csv', '2024 - 1 Janeiro UNIÃO MEGA FEIRA.csv', '2024 - 1 Janeiro CESTÃO BAIRRO.csv', '2024 - 1 Janeiro CARIBÉ .csv', '2024 - 1 Janeiro PAG POUCO.csv', '2024 - 1 Janeiro BH VAREJO .csv', '2024 - 1 Janeiro ROCHA.csv', '2024 - 1 Janeiro SUPER MAAR.csv', '2024 - 1 Janeiro MONTALVÂNIA.csv', '2024 - 1 Janeiro PREÇO BAIXO.csv', '2024 - 1 Janeiro NACIONAL .csv', '2024 - 2 Fevereiro BH ATACADO.csv', '2024 - 2 Fevereiro CESTÃO DA ECONOMIA .csv', '2024 - 2 Fevereiro CARIBÉ .csv', '2024 - 2 Fevereiro KAMILA.csv', '2024 - 2 Fevereiro TERRA NORTE.csv', '2024 - 2 Fevereiro PAG POUCO.csv', '2024 - 2 Fevereiro ROCHA.csv', '2024 - 2 Fevereiro UNIÃO MEGA FEIRA.csv', '2024 - 2 Fevereiro CESTÃO BAIRRO.csv', '2024 - 2 Fevereiro BH VAREJO .csv', '2024 - 2 Fevereiro CARIBÉ 2.csv', '2024 - 2 Fevereiro BOM PREÇO .csv', '2024 - 2 Fevereiro MONTALVÂNIA.csv', '2024 - 2 Fevereiro SUPER MAAR.csv', '2024 - 2 Fevereiro PREÇO BAIXO.csv', '2024 - 2 Fevereiro NACIONAL .csv']


nomes_dos_meses_2022 = ['1 Março', '2 Abril', '3 Maio', '4 Junho', '5 Julho', '6 Agosto', '7 Setembro', '8 Outubro', '9 Novembro', '10 Dezembro']
nomes_dos_meses_2023 = ['1 Janeiro', '2 Fevereiro', '3 Março', '4 Abril', '5 Maio', '6 Junho', '7 Julho', '8 Agosto', '9 Setembro', '10 Outubro', '11 Novembro', '12 Dezembro']
nomes_dos_meses_2024 = ['1 Janeiro', '2 Fevereiro']



mes_a_mes_2022 = {}
mes_a_mes_2023 = {}
mes_a_mes_2024 = {}

for x in nomes_dos_meses_2022:
    mes_a_mes_2022[x] = segregacao.separamento_por_mes('2022', x, list_2022)

for x in nomes_dos_meses_2023:
    mes_a_mes_2023[x] = segregacao.separamento_por_mes('2023', x, list_2023)

for x in nomes_dos_meses_2024:
    mes_a_mes_2024[x] = segregacao.separamento_por_mes('2024', x, list_2024)


mercados_2022_vende_tudo = {}
for x in nomes_dos_meses_2022:
    mercados_2022_vende_tudo[x] = segregacao.verificar_se_vende_todos('2022', x, list_2022)

mercados_2023_vende_tudo = {}
for x in nomes_dos_meses_2023:
    mercados_2023_vende_tudo[x] = segregacao.verificar_se_vende_todos('2023', x, list_2023)

mercados_2024_vende_tudo = {}
for x in nomes_dos_meses_2024:
    mercados_2024_vende_tudo[x] = segregacao.verificar_se_vende_todos('2024', x, list_2024)


mais_baratos_2022 = segregacao.os_mercados_mais_baratos_por_mes(mes_a_mes_2022, mercados_2022_vende_tudo)
mais_baratos_2023 = segregacao.os_mercados_mais_baratos_por_mes(mes_a_mes_2023, mercados_2023_vende_tudo)
mais_baratos_2024 = segregacao.os_mercados_mais_baratos_por_mes(mes_a_mes_2024, mercados_2024_vende_tudo)



medias_por_mes_2022 = {}
medias_por_mes_2023 = {}
medias_por_mes_2024 = {}

medias_por_mes_2022 = calculos.calcular_media_acima_de_850(mes_a_mes_2022)
medias_por_mes_2023 = calculos.calcular_media_acima_de_850(mes_a_mes_2023)
medias_por_mes_2024 = calculos.calcular_media_acima_de_850(mes_a_mes_2024)


variacao_2022 = calculos.varicao_percentual_ano(medias_por_mes_2022)
variacao_2023 = calculos.varicao_percentual_ano(medias_por_mes_2023)
variacao_2024 = calculos.varicao_percentual_ano(medias_por_mes_2024)

separado_por_tipo_2022 = segregacao.separar_por_tipo('2022', list_2022, nomes_dos_meses_2022)
separado_por_tipo_2023 = segregacao.separar_por_tipo('2023', list_2023, nomes_dos_meses_2023)
separado_por_tipo_2024 = segregacao.separar_por_tipo('2024', list_2024, nomes_dos_meses_2024)

mais_baratos_no_mes_por_subcategoria_2022 = segregacao.encontrar_mais_baratos_por_mes_segregado_em_tipos(separado_por_tipo_2022, mercados_2022_vende_tudo)
mais_baratos_no_mes_por_subcategoria_2023 = segregacao.encontrar_mais_baratos_por_mes_segregado_em_tipos(separado_por_tipo_2023, mercados_2023_vende_tudo)
mais_baratos_no_mes_por_subcategoria_2024 = segregacao.encontrar_mais_baratos_por_mes_segregado_em_tipos(separado_por_tipo_2024, mercados_2024_vende_tudo)

#os.system('clear')
