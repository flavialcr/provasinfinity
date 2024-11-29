numero = int(input('Digite um número de 1 a 10 para ver a sua tabuada: '))

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
