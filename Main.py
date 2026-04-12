from service import criarLabirinto, exibirTabelaComparacao
from buscaLargura import buscaLargura
from buscaProfundidade import buscaProfundidade
from buscaGulosa import buscaGulosa
from buscaA import buscaA

tamanho = int(input('Tamanho de linha e coluna = '))
parede = int(input('Quantidade de paredes = '))
lama = int(5)
grama = int(2)
print('Entrada total', tamanho*tamanho, 'Valores')

mapa = criarLabirinto(tamanho, parede)

buscaLargura(tamanho, mapa) 

buscaProfundidade(tamanho, mapa)

buscaGulosa(tamanho, mapa)

buscaA(tamanho, mapa)

exibirTabelaComparacao()





