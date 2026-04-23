# Cadastrar livros
# Listar livros
# Buscar por títulos
# Emprestar livros
# Devolver livros
# Sair

import importlib

print('Bem vindo!')

livros_cadastrados = {}

lista_acoes = {
    'Sair':0,
    'Cadastra livros': 1,
    'Listar livros': 2,
    'Buscar livros': 3,
    'Emprestar livros': 4,
    'Devolver livros': 5,
}
arquivos = {
    1:'cadastro',
    2:'listar_livros',
    3:'buscador',
    4:'emprestar',
    5:'devolver_livro',
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
            modulo = importlib.import_module(arquivos[acao])
            modulo.funcao(livros_cadastrados)
            continue
    except KeyError:
        print('Ação invalida, digite números de 1 a 5')
    except ValueError:
        print('Digite apenas números')
