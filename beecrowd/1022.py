#https://www.beecrowd.com.br/judge/pt/problems/view/1022
"""Resolvido por bruno_fagner"""
from fractions import Fraction

# Criar frações
frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

# Realizar operações sem simplificação
soma = frac1.numerator * frac2.denominator + frac2.numerator * frac1.denominator, frac1.denominator * frac2.denominator
subtracao = frac1.numerator * frac2.denominator - frac2.numerator * frac1.denominator, frac1.denominator * frac2.denominator
multiplicacao = frac1.numerator * frac2.numerator, frac1.denominator * frac2.denominator
divisao = frac1.numerator * frac2.denominator, frac1.denominator * frac2.numerator

# Exibir resultados
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
soma = frac1 + frac2
subtracao = frac1 - frac2
multiplicacao = frac1 * frac2
divisao = frac1 / frac2
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)