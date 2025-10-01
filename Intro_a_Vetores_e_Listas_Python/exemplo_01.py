# Criar um programa que lê as notas de uma turma de N alunos, e indica o número de alunos acima da média, utilizando o método append(...).

alunos = int(input("Quantos alunos há na turma:\n"))
notas = []
soma = count = 0

for i in range(0, alunos):
    nota = float(input(f"Digite a nota do {i + 1}º aluno:\n"))
    soma += nota
    notas.append(nota)

media = soma / alunos
print(f"A média da turma é {media :.2f}")
for j in range(0, alunos):
    if notas[j] > media:
        count += 1
print(f"{count} alunos que estão acima da média.")
