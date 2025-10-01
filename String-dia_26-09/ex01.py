# Escreva um algoritmo em Python que peça ao usuário uma palavra e mostre a mesma palavra, mas com todas as letras "a" minúsculas substituídas por @.


frase = input("Digite uma frase:\n")

frase_nova = ""

for i in frase:
    if i == "a" or i == "ã":
        frase_nova += "@"
    else:
        frase_nova += i

print(frase_nova)