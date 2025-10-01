# Escreva um algoritmo em Python que peça ao usuário uma palavra e mostre a mesma palavra, mas com todas as letras "o" minúsculas substituídas por 0.

frase = input("Digite uma frase:\n")

frase_nova = ""

for i in frase:
    if i == "o":
        frase_nova += "0"
    else:
        frase_nova += i

print(frase_nova)