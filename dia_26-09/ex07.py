# Escreva um algoritmo em Python que peça ao usuário uma palavra e mostre a mesma palavra com todas as letras minúsculas transformadas em maiúsculas.

frase = input("Digite uma frase:\n")
frase_nova = ""

for i in frase:
    if i.islower():
        frase_nova += i.upper()
    else:
        frase_nova += i

print(frase_nova)