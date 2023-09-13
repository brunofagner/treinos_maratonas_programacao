i, f = map(int, input().split())
if i == f: print('O JOGO DUROU 24 HORA(S)')
elif i > f: print('O JOGO DUROU {} HORA(S)'.format(24 - i + f))
else: print('O JOGO DUROU {} HORA(S)'.format(f - i))