#https://www.beecrowd.com.br/judge/pt/problems/view/1028
"""Resolvido por bruno_fagner"""
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    while b != 0:
        a,b = b,a%b
    print(a)