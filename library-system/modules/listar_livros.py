# Listar os livros e quantidades

def funcao(livros_cadastrados):
    if not livros_cadastrados:
        print('Nenhum livro cadastrado')
    else:
        for k, v in livros_cadastrados.items():
            if v == 0:
                print(f'o livro {k} nao esta disponível')
            else:
                print(f"O livro {k} tem {v} unidade(s);")