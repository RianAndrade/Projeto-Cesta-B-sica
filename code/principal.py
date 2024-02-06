import variaveis as vr
import funcoes_de_tratamento 

nome = []
cont = 0
for x in range(0,len(vr.caminhos_2023)):
    cont = funcoes_de_tratamento.convert_download(vr.caminhos_2023[x], vr.nomes_dos_meses_2023[x], "2023", nome, cont)

print(nome)    