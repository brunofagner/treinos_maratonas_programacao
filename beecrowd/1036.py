A, B, C = map(float, input().split())
raiz = (B**2) - (4*A*C)
if A == 0 or raiz < 0:
    print("Impossivel calcular")
else:
    x1 = (-B + raiz**(1/2))/(2*A)
    x2 = (-B - raiz**(1/2))/(2*A)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")