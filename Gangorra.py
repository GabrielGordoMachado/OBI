print('Declare respectivamente: O peso da criança 1, o comprimento do lado para a criança 1, o peso da criança 2 e o comprimento do lado para a criança 2.')
Peso1, Comp1, Peso2, Comp2 = map(int, input().split())

if Peso1 * Comp1 == Peso2 * Comp2:
    print('0')
elif Peso1 * Comp1 > Comp2 * Peso2:
    print('0 1')
else:
    print('0 0')