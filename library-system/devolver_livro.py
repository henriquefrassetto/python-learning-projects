# Devolver livro

def funcao(livros_cadastrados):
    livro_devolver = input("Digite qual livro voce gostaria de devolver: ")
    if livro_devolver not in livros_cadastrados:
        print('Livro nao cadastrado')
    else:
        livros_cadastrados[livro_devolver] += 1
        print('Livro devolvido com sucesso')