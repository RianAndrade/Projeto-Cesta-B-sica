import variaveis as vr
import funcoes_de_tratamento 

nome = []
cont = 0
for x in range(0,len(vr.caminhos_2022)):
    cont = funcoes_de_tratamento.convert_download(vr.caminhos_2022[x], vr.nomes_dos_meses_2022[x], "2022", nome, cont)
print(nome)    