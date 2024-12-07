# Funções para as operações matemáticas

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Não é possível dividir por zero.Comece novamente."
    else:
        return x / y

# Função para exibir o menu
def exibir_menu():
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

# Função principal para controlar o fluxo do programa
def calculadora():
    while True:
        exibir_menu()  # Exibe o menu
        escolha = input("Digite o número da operação (1/2/3/4/5): ")
        
        # Verifica se o usuário escolheu sair
        if escolha == '5':
            print("Saindo do programa...")
            break
        
        # Solicita os números para a operação
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira números válidos.")
            continue
        
        # Realiza a operação conforme a escolha do usuário
        if escolha == '1':
            print(f"{num1} + {num2} = {soma(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
        elif escolha == '4':
            if num2 == 0:  # Verifica divisão por zero antes de realizar a operação
                print("Erro! Não é possível dividir por zero.")
            else:
                print(f"{num1} / {num2} = {divisao(num1, num2)}")
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 5.")

# Chama a função principal para iniciar o programa
calculadora()

