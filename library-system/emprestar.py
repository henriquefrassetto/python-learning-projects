# Emprestar livros

def funcao(livros_cadastrados):
    livro_emprestar = input("Digite qual livro voce gostaria de emprestar: ")
    if livro_emprestar not in livros_cadastrados:
        print('Livro nao cadastrado')
    elif livros_cadastrados[livro_emprestar] == 0:
        print('O livro nao esta disponível')
    else:
        livros_cadastrados[livro_emprestar] -= 1
        print('Livro emprestado com sucesso')