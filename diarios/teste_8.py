def countStudents(students, sandwiches):
    counts = [0, 0]
    for student in students:
        counts[student] += 1
    remaining = len(sandwiches)
    for sandwich in sandwiches:
        if counts[sandwich] == 0:
            break
        if remaining == 0:
            break
        counts[sandwich] -= 1
        remaining -= 1

    return remaining


print(countStudents([1, 1, 0, 0], [0, 1, 0, 1]))
print(countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))


# O refeitório da escola oferece sanduíches circulares e quadrados no intervalo do almoço, denominados por números 0e 1respectivamente. Todos os alunos ficam em fila. Cada aluno prefere sanduíches quadrados ou circulares.

# O número de sanduíches no refeitório é igual ao número de alunos. Os sanduíches são empilhados . Em cada etapa:

# Se o aluno que está na frente da fila preferir o sanduíche que está no topo da pilha, ele o pegará e sairá da fila.
# Caso contrário, eles sairão e irão para o final da fila.
# Isso continua até que nenhum dos alunos da fila queira pegar o sanduíche de cima e, portanto, não consiga comer.

# São fornecidas duas matrizes de inteiros studentse sandwichesonde sandwiches[i]está o tipo do sanduíche na pilha ( é o topo da pilha) e é a preferência do aluno na fila inicial ( é o início da fila). Retorne o número de alunos que não conseguem comer.i​​​​​​thi = 0students[j]j​​​​​​thj = 0


# Exemplo 1:

# Entrada: alunos = [1,1,0,0], sanduíches = [0,1,0,1]
#  Saída: 0
# Explicação:
# - Aluno da frente sai do sanduíche de cima e volta para o final da fila fazendo alunos = [1,0,0,1].
# - Aluno da frente sai do sanduíche de cima e volta para o final da fila fazendo alunos = [0,0,1,1].
# - Aluno da frente pega o sanduíche de cima e sai da fila fazendo alunos = [0,1,1] e sanduíches = [1,0,1].
# - Aluno da frente sai do sanduíche de cima e volta para o final da fila fazendo alunos = [1,1,0].
# - Aluno da frente pega o sanduíche de cima e sai da fila fazendo alunos = [1,0] e sanduíches = [0,1].
# - Aluno da frente sai do sanduíche de cima e volta para o final da fila fazendo alunos = [0,1].
# - Aluno da frente pega o sanduíche de cima e sai da fila fazendo alunos = [1] e sanduíches = [1].
# - Aluno da frente pega o sanduíche de cima e sai da fila fazendo alunos = [] e sanduíches = [].
# Assim, todos os alunos podem comer.
# Exemplo 2:

# Entrada: alunos = [1,1,1,0,0,1], sanduíches = [1,0,0,0,1,1]
#  Saída: 3


# Restrições:

# 1 <= students.length, sandwiches.length <= 100
# students.length == sandwiches.length
# sandwiches[i]é 0ou 1.
# students[i]é 0ou 1.
