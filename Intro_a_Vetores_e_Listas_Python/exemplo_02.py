# Criar um programa para acrescentar um elemento em uma lista se for digitado a letra 'A', remover se 'R', imprimir se 'I' e sair se 'F'.

print('''Opções:
      A - Adicionar um elemento; 
      R - Remover um elemento; 
      I - Imprimir a Lista; 
      F - Sair do programa): ''')

Lista = []

while True:
    opcao = input("Digite a opção desejada: ").upper()

    if opcao == "A":
        elemento = input('Digite o elemento a ser adicionado: \n')
        Lista.append(elemento)
        print(f"Elemento {elemento} adicionado")
        print(Lista)

    elif opcao == "R":
        if Lista:
            print(Lista)
            elemento = input('Digite o elemento que deseja remover: \n')
            if elemento in Lista:
                Lista.remove(elemento)
                print(f"Elelemtno {elemento} removido")
                print(Lista)
            else:
                print(f"Elemento {elemento} não encontrado na Lista")
                print(Lista)
        else:
            print(Lista)
            print("Esse Elemento não se encontra na Lista")
    
    elif opcao == "I":
        print("Lista atual: ", Lista if Lista else "Lista vazia")
    
    elif opcao == "S":
        print(Lista)
        print("Finalizando o programa...")
        break

    else:
        print("Opção inválida, tente novamente.")


