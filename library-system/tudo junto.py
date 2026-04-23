# Cadastrar livros
# Listar livros
# Buscar por títulos
# Emprestar livros
# Devolver livros
# Sair

print('Bem vindo!')

livros_cadastrados = {}

# Cadastro de livros------------------------------------------------------------------------------------------------

def cadastro(livros_cadastrados):
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

# Listar os livros e quantidades--------------------------------------------------------------------------------------

def listar_livros(livros_cadastrados):
    if not livros_cadastrados:
        print('Nenhum livro cadastrado')
    else:
        for k, v in livros_cadastrados.items():
            if v == 0:
                print(f'o livro {k} nao esta disponível')
            else:
                print(f"O livro {k} tem {v} unidade(s);")

# Busca os livros----------------------------------------------------------------------------------------------------

def buscador(livros_cadastrados):
    livro_buscar = input("Digite qual livro gostaria de procurar: ")
    if livro_buscar in livros_cadastrados:
        print(f'O livro esta cadastrado e tem {livros_cadastrados[livro_buscar]} unidade(s)')
    else:
        print('O livro nao foi encontrado')

# Emprestar livros---------------------------------------------------------------------------------------------------

def emprestar(livros_cadastrados):
    livro_emprestar = input("Digite qual livro voce gostaria de emprestar: ")
    if livro_emprestar not in livros_cadastrados:
        print('Livro nao cadastrado')
    elif livros_cadastrados[livro_emprestar] == 0:
        print('O livro nao esta disponível')
    else:
        livros_cadastrados[livro_emprestar] -= 1
        print('Livro emprestado com sucesso')

# Devolver livro-----------------------------------------------------------------------------------------------------

def devolver_livro(livros_cadastrados):
    livro_devolver = input("Digite qual livro voce gostaria de devolver: ")
    if livro_devolver not in livros_cadastrados:
        print('Livro nao cadastrado')
    else:
        livros_cadastrados[livro_devolver] += 1
        print('Livro devolvido com sucesso')

# Chamar as funções------------------------------------------------------------------------------------------------

lista_acoes = {
    'Sair':0,
    'Cadastra livros': 1,
    'Listar livros': 2,
    'Buscar livros': 3,
    'Emprestar livros': 4,
    'Devolver livros': 5,
}

arquivos = {
    1:cadastro,
    2:listar_livros,
    3:buscador,
    4:emprestar,
    5:devolver_livro
}

while True:
    try:
        for k, v in lista_acoes.items():
            print(f'Digite {v} para {k}')
        acao = int(input('Digite aqui: '))
        if acao == 0:
            print('Ate logo!')
            break
        else:
            arquivos[acao](livros_cadastrados)
            continue
    except KeyError:
        print('Ação invalida, digite números de 1 a 5')
    except ValueError:
        print('Digite apenas números')