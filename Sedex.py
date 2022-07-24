#Sedex(OBI2010)
print('Qual o diâmetro da bola de boliche?')
Diam = int(input())

print('Qual a altura, a largura e a profundidade da caixa?')
A, L, P = map(int, input().split())

if Diam > A or L or P:
    print('N')
else:
    print('S')