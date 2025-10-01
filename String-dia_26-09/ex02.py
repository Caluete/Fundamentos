# Escreva um algoritmo em Python que peça ao usuário uma palavra e mostre a mesma palavra, mas com todas as letras "e" minúsculas substituídas por 3.


frase = input("Digite uma frase:\n")

frase_nova = ""

for i in frase:
    if i == "e" or i == "ê" or i == "é":
        frase_nova += "3"
    else:
        frase_nova += i

print(frase_nova)