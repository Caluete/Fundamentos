# Escreva um algoritmo em Python que peça ao usuário uma palavra e mostre a mesma palavra com todas as letras maiúsculas transformadas em minúsculas.

frase = input(" Digite uma frase:\n")
nova_frase = ""

for i in range(0, len(frase)):
    if frase[i].isupper():
        nova_frase += frase[i].lower()
    else:
        nova_frase += frase[i]

print(nova_frase)