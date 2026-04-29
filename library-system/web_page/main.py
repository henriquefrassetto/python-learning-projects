import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

livros_cadastrados = {
    "Dom Casmurro": 3,
    "O Pequeno Príncipe": 5,
    "1984": 4,
    "Harry Potter e a Pedra Filosofal": 2,
    "Senhor dos Anéis": 1,
    "A Revolução dos Bichos": 6,
    "Clean Code": 2,
    "Python para Iniciantes": 7,
    "Engenharia Mecânica Aplicada": 3,
    "Matemática para Engenharia": 4
}

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request = request,
        name = 'index.html',
        context = {}
    )

@app.post("/cadastro")
def cadastro(nome: str, quantidade: int):
    livros_cadastrados[nome] = quantidade
    return {'msg': 'Cadastro realizado com sucesso!'}

@app.get("/livros")
def listar_livros():
    cadastros = []
    if not livros_cadastrados:
        return {'msg': 'Nenhum livro cadastrado'}
    for nome, quantidade in livros_cadastrados.items():
        if quantidade == 0:
            cadastros.append(f'O livro {nome} nao esta disponível')
        if quantidade == 1:
            cadastros.append(f'{nome}, {quantidade} unidade')
        else:
            cadastros.append(f'{nome}, {quantidade} unidades')
    return cadastros

@app.get("/buscar")
def buscar(nome: str):
    if nome not in livros_cadastrados:
        return {'msg': 'Livro nao encontrado'}
    if livros_cadastrados[nome] == 0:
        return {'msg': 'Livro indisponível'}
    return {'msg': f'O livro {nome} possui {livros_cadastrados[nome]} unidade(s)'}

@app.post("/emprestar")
def emprestar(nome: str):
    if nome not in livros_cadastrados:
        return {'msg': 'Livro nao encontrado'}
    if livros_cadastrados[nome] == 0:
        return {'msg': 'Livro nao esta disponível'}
    livros_cadastrados[nome] -= 1
    return {'msg': f'Livro {nome} emprestado!'}

@app.post("/devolver")
def devolver(nome: str):
    if nome not in livros_cadastrados:
        return {'msg': 'Livro nao encontrado'}
    livros_cadastrados[nome] += 1
    return {'msg': f'Livro {nome} devolvido!'}

@app.delete("/remover")
def remover(nome: str):
    if nome not in livros_cadastrados:
        return {'msg': 'Livro nao encontrado'}
    del livros_cadastrados[nome]
    return {'msg': f'Livro {nome} removido!'}

# uvicorn main:app --reload
# uvicorn main:app --reload --reload-include "*.html" --reload-include "*.yaml"