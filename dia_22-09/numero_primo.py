numero = int(input("Digite um número inteiro: "))

primo = True

for i in range(2, numero):
    if numero % i == 0:
        primo = False
if primo:
    print(f"O número {numero} é primo")
else:
    print("O número não é primo")