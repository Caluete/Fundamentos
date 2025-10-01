frase = input("Digite algo:\n")
caracteres_usados = " " #Cria uma string vazia para armazenar os caracteres já verificados

for i in frase: # O iterador vai ler a string frase percorrendo índice por índice
    if i not in caracteres_usados: # Se o caractere não estiver na string caracteres_usados
        caracteres_usados += i # Somar o caractere na string caracteres_usados
        print(f"Caracter - {i} aparece {frase.count(i)} vezes.") # Usar o método count() para contar quantos caracteres há na string frase e colocar direttamanete na saída.