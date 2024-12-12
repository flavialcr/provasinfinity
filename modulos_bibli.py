class Livro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.emprestimos = {}

    def adicionar_livro(self, titulo, autor, copias):
        novo_livro = Livro(titulo, autor, copias)
        self.livros.append(novo_livro)
        print(f'Livro "{titulo}" adicionado à biblioteca.')

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro disponível na biblioteca.")
        else:
            for livro in self.livros:
                print(f'Título: {livro.titulo}, Autor: {livro.autor}, Cópias disponíveis: {livro.copias}')

    def emprestar_livro(self, titulo, usuario):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.copias > 0:
                    livro.copias -= 1
                    if usuario in self.emprestimos:
                        self.emprestimos[usuario].append(titulo)
                    else:
                        self.emprestimos[usuario] = [titulo]
                    print(f'Livro "{titulo}" emprestado para {usuario}.')
                    return
                else:
                    print(f'Livro "{titulo}" não está disponível para empréstimo.')
                    return
        print(f'Livro "{titulo}" não encontrado na biblioteca.')

    def devolver_livro(self, titulo, usuario):
        if usuario in self.emprestimos and titulo in self.emprestimos[usuario]:
            for livro in self.livros:
                if livro.titulo == titulo:
                    livro.copias += 1
                    self.emprestimos[usuario].remove(titulo)
                    if not self.emprestimos[usuario]:
                        del self.emprestimos[usuario]
                    print(f'Livro "{titulo}" devolvido por {usuario}.')
                    return
        print(f'Usuário {usuario} não possui o livro "{titulo}" emprestado.')

    def verificar_disponibilidade(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                print(f'Título: {livro.titulo}, Autor: {livro.autor}, Cópias disponíveis: {livro.copias}')
                return
        print(f'Livro "{titulo}" não encontrado na biblioteca.')

    def mostrar_livros_emprestados(self, usuario):
        if usuario in self.emprestimos:
            print(f'Livros emprestados por {usuario}: {", ".join(self.emprestimos[usuario])}')
        else:
            print(f'Usuário {usuario} não possui livros emprestados.')

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Listar Todos os Livros")
        print("3. Empréstimo de Livro")
        print("4. Devolução de Livro")
        print("5. Verificar Disponibilidade de um Livro")
        print("6. Mostrar Livros Emprestados a um Usuário")
        print("7. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            copias = int(input("Número de cópias disponíveis: "))
            biblioteca.adicionar_livro(titulo, autor, copias)
        elif escolha == "2":
            biblioteca.listar_livros()
        elif escolha == "3":
            titulo = input("Título do livro: ")
            usuario = input("Nome do usuário: ")
            biblioteca.emprestar_livro(titulo, usuario)
        elif escolha == "4":
            titulo = input("Título do livro: ")
            usuario = input("Nome do usuário: ")
            biblioteca.devolver_livro(titulo, usuario)
        elif escolha == "5":
            titulo = input("Título do livro: ")
            biblioteca.verificar_disponibilidade(titulo)
        elif escolha == "6":
            usuario = input("Nome do usuário: ")
            biblioteca.mostrar_livros_emprestados(usuario)
        elif escolha == "7":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
