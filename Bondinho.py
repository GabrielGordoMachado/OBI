print('Quantos alunos irão para a excursão?')
Alunos = int(input())

print('Qual será a quantidade de monitores?')
Monitores = int(input())

import math

Total = Monitores + Alunos

if Total <= 50:
    print('Todos podem subir juntos!')

elif Total > 50:
    viagens = Total / 50
    print("São necessárias {0} viagens para levar todos vocês!".format(math.ceil(viagens)))