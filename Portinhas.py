#Fliper(OBI2014)#

print('Sabendo que (1) equivale a direita, (0) a esquerda, em qual posição pretende deixar as portinhas (P) e (R), respectivamente:')
PortinhaP, PortinhaR = map(int, input().split())

if PortinhaP == 0:
    print('A bolinha caiu no buraco C')

elif PortinhaP != 0 and PortinhaR ==0:
    print('A bolinha caiu no buraco B')
else:
    print('A bolinha caiu no buraco A')
    