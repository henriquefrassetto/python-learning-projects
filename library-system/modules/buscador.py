# Busca os livros

def funcao(livros_cadastrados):
    livro_buscar = input("Digite qual livro gostaria de procurar: ")
    if livro_buscar in livros_cadastrados:
        print(f'O livro esta cadastrado e tem {livros_cadastrados[livro_buscar]} unidade(s)')
    else:
        print('O livro nao foi encontrado')