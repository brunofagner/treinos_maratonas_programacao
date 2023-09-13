l = sorted(map(float, input().split()), reverse=True)
if l[0] >= l[1] + l[2]:
    print('NAO FORMA TRIANGULO')
    exit()
if l[0]**2 == l[1]**2 + l[2]**2:
    print('TRIANGULO RETANGULO')
if l[0]**2 > l[1]**2 + l[2]**2:
    print('TRIANGULO OBTUSANGULO')
if l[0]**2 < l[1]**2 + l[2]**2:
    print('TRIANGULO ACUTANGULO')
if l[0] == l[1] == l[2]:
    print('TRIANGULO EQUILATERO')
if l[0] == l[1] != l[2] or l[0] == l[2] != l[1] or l[1] == l[2] != l[0]:
    print('TRIANGULO ISOSCELES')
