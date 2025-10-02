# Peça ao usuário que insira uma lista de números, conte quantos deles são maiores que 10.

numeros = [int(n) for n in input("Digite uma lista de números:\n").split(',')]

contador = 0

for i in numeros:
    if i > 10:
        contador += 1
    
print(f"Sua lista de numeros maiores que 10 é {contador}")