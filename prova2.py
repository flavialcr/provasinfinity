
velocidade = float(input('Qual a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade-80)*20                
    print(f' Você foi multado em R${multa}')
else:
    print('Você está dentro do limite da via')
