# Escreva um algoritmo em Python que peça ao usuário uma palavra e mostre a mesma palavra, mas com todas as letras "i" minúsculas substituídas por 1.

frase = input("Digite uma frase:\n")

frase_nova = ""

for j in frase:
    if j == "i" or j == "í":
        frase_nova += "1"
    else:
        frase_nova += j

print(frase_nova)