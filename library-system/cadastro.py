# Cadastro de livros

# livros_cadastrados = {}

def funcao(livros_cadastrados):
    while True:
        try:
            cadastro, quantidade = input("Digite o livro que gostaria de cadastrar e a quantidade a ser cadastrada: ").split(',')
            quantidade = int(quantidade)
            livros_cadastrados[cadastro.lower()] = quantidade

            print("Cadastro realizado com sucesso!")

            proxima_acao = input("Gostaria de cadastrar mais algum? ")

            if proxima_acao == 'sim':
                continue
            else:
                break
        except ValueError:
            print('Necessário inserir o valor')