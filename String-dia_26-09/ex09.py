#  Peça ao usuário uma string e exiba uma nova versão onde cada caractere aparece duplicado. Exemplo: "python" → "ppyytthhoonn".

palavra = input("Digite uma palavra:\n")
nova_palavra = ""

for i in palavra:
    nova_palavra += i * 2

print(nova_palavra)