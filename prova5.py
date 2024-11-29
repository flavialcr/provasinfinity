# loop que vai rodar ate o usuario pedir pra parar (nao sabemos quando ele vai parar)
# salvar informações (nome do produto mais barato, nome dos produtos que custam + 1000, valor total)
# dentro do loop -> perguntar nome e valor dos produtos, fazer as logicas das informaçoes

valor_total = 0 # valor total da compra
nome_produtos_caros = [] # nome dos produtos maiores que 1000$
nome_produto_mais_barato = "produto qualquer" # produto mais barato
valor_produto_mais_barato = 0

while True:
    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o valor do produto : ').replace(",", "."))
    valor_total += preco
    if preco >= 1000:
        nome_produtos_caros.append(nome)
    if preco < valor_produto_mais_barato or valor_produto_mais_barato == 0:
        valor_produto_mais_barato = preco
        nome_produto_mais_barato = nome
    decisao = input('Deseja continuar inserindo produtos? [S/N]').lower()
    if decisao == 'n':
        break

print(f'Muito obrigada pela compra! Aqui estão algumas informações:\nValor total da compra: {valor_total:.2f}\nProduto mais barato: {nome_produto_mais_barato} - {valor_produto_mais_barato}')
print(f'Produtos com preços superiores a R$1000,00: ')
for i in nome_produtos_caros:
    print(i)
