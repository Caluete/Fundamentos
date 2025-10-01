numero = int(input("Digite um número para calcularmos o fatorial: "))

fatorial = 1

while numero > 0:
    fatorial = fatorial * numero
    numero -= 1

print(f"O fatorial é {fatorial}")
