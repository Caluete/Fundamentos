# Crie um programa que solicite ao usuário uma string e exiba a quantidade de vezes que cada caractere aparece.

frase = input("Digite algo:\n")
caracteres_usados = " "

for i in range(0, len(frase)): # Um iterador i vai ler a string frase percorrendo índice por índice
    if frase[i].lower() not in caracteres_usados: # Se o caractere (em minúsculo para evitar duplicidade) não etiver na string caracteres_usados
        v = frase[i].lower() # Armazena o caractere em minúsculo na variável v criada agora
        caracteres_usados += v # Somar o caractere v na string caracteres_usados

        contador= 0 # Cria um contador zerado
        for j in frase: # Percorre a string frase novamente
            if j.lower() == v: # Se o caractere (em maiúsculo para evitar dplicidade) for igual ao caractere v
                contador += 1 # incrementa o contador em 1
        print(f"O caractere {v} aparece {contador} vezes.")