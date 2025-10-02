# Peça ao usuário que insira uma lista com 5 números inteiros e calcule a soma de todos os elementos, usando um loop for.

numero = [int(n) for n in input("Digite 5 números  inteiros:\n").split(',')]
soma = 0

for i in numero:
    soma += i

print(f"Sua lista de números é {numero}")
print(f"A soma dos numeros é: {soma}")
