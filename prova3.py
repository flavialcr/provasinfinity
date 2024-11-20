contador = 0 # a qtd de voltas = qtd de números inseridos no programa
soma = 0 # variavel acumuladora que retorna a soma total após o loop

while True:
   numero = int(input('Digite um número qualquer (ou 0 para sair do programa): '))
   if numero == 0:
      break
   soma += numero
   contador += 1

if contador > 1:
   print(f'Quantidade de números digitados: {contador}\nSoma total dos números: {soma}\nMédia aritmética: {soma/contador}')
else:
   print('Nenhum valor inserido no programa...')
