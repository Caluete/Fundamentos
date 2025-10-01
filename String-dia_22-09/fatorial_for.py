numero = int(input("Entre com um número inteiro para calcularmos seu fatorial: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial = fatorial * i

print(f"O fatorial é {fatorial}")