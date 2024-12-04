# Você está responsável por gerenciar os resultados de uma competição esportiva. 
# Para isso, você tem uma lista de tuplas onde cada tupla representa uma equipe e suas respectivas pontuações em 
# diferentes rodadas. O formato de cada tupla é:

# ('nome_da_equipe', [lista_de_pontuacoes]).

# Calcular a média das pontuações: Para cada equipe, calcule a média de suas pontuações e armazene 
# esses valores em uma nova lista chamada medias. Cada média deve corresponder à equipe respectiva.

equipes = [
    ('equipe1', [5,5,7,8,10]),
    ('equipe2', [10,8,8,3,3]),
    ('equipe3', [6,6,5,6,5])
]

media_equipe1 = sum(equipes[0][1]) / 5
media_equipe2 = sum(equipes[1][1]) / 5
media_equipe3 = sum(equipes[2][1]) / 5

print(f'1 - {media_equipe1}\n2 - {media_equipe2}\n3 - {media_equipe3}')

# Ordenar as médias: Organize a lista medias em ordem decrescente, de modo que a equipe com a 
# maior média apareça primeiro.

medias = [media_equipe3, media_equipe2, media_equipe1]
medias.sort(reverse=True)
print(medias)

# Criar uma lista de classificação: Crie uma nova lista chamada classificacao, que contenha tuplas. 
# Cada tupla deverá ter o nome da equipe e sua média de pontuações, seguindo a ordem decrescente da média.

podio = [
    ('Equipe 1', medias[0]),
    ('Equipe 2', medias[1]),
    ('Equipe 3', medias[2]),
]

# Exibir a classificação final: Mostre na tela a classificação final das equipes, exibindo o nome da equipe e sua média, 
# da equipe com a maior média para a menor.

posicao = 1
for equipe in podio:
    print(f'{posicao}º lugar: {equipe[0]} - Pontuação: {equipe[1]}')
    posicao += 1
