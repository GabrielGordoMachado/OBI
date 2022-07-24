print('Dê os pesos das bolas, respectivamente A, B, C e D:')
PesoA, PesoB, PesoC, PesoD = map(int, input().split())
SomaBCD = PesoB + PesoC + PesoD
SomaBC = PesoB + PesoC

if PesoA != SomaBCD or PesoD != SomaBC or PesoB != PesoC:
    print('N')
else:
    print('S')