#  Escreva um algoritmo em Python que peça ao usuário uma palavra e mostre a mesma palavra, mas com todas as letras "u" minúsculas substituídas por #.

frase = input("Digite uma frase:\n")
frase_nova = ""

for i in frase:
    if i == "u":
        frase_nova += "#"
    else:
        frase_nova += i

print(frase_nova)