# Cadastro de Alunos:

# Para cada aluno, as seguintes informações devem ser coletadas:
# Nome: O nome do aluno.
# Idade: A idade do aluno.
# Notas: As notas em três disciplinas: Matemática, Ciências e História.

qtd = int(input('Quantos alunos você deseja cadastrar no sistema? '))
alunos = []

for n in range(1,qtd+1):
    aluno = {
    'nome' : input(f'Digite o nome do {n}º aluno: '),
    'idade': input(f'Digite a idade do {n}º aluno: '),
    'notas': {
        'Matemática': float(input('Digite a nota em matemática: ')),
        'Ciências': float(input('Digite a nota em ciências: ')),
        'História': float(input('Digite a nota em história: '))
        }
    }
    alunos.append(aluno)

# Visualização de Alunos:
# O programa deve permitir que o usuário visualize a lista de todos os alunos cadastrados.
# Para cada aluno, o programa deve exibir:
# O nome
# A idade
# As notas em cada disciplina

contador = 1
for aluno in alunos:
    print(f'-------------Aluno {contador}---------------')
    print(f'Nome: {aluno['nome']}\nIdade: {aluno['idade']}\nNotas: {aluno['notas']}')
    contador += 1

# Cálculo da Média de Notas:
# O programa deve calcular a média das notas para cada aluno.
# A média deve ser exibida junto com as informações de cada aluno.

contador = 1
for aluno in alunos:
    aluno['media'] = sum(aluno['notas']) / 3
    print(f'-------------Aluno {contador}---------------')
    print(f'Nome: {aluno['nome']}\nIdade: {aluno['idade']}\nNotas: {aluno['notas']}\nMédia: {aluno['media']}')
    contador += 1

# Aluno com a Melhor Média:
# O programa deve identificar e exibir o aluno que tem a melhor média de notas entre todos os alunos cadastrados.

melhor_media = None
aluno_vencedor = ''
for aluno in alunos: 
    media = aluno['media']
    nome = aluno['nome']
    if melhor_media < media or melhor_media == None:
        melhor_media = media
        aluno_vencedor = nome
print(f'A melhor média entre os alunos foi {melhor_media}, aluno(a) - {aluno_vencedor}')
