from biblioteca.livro import Livro
from biblioteca.acervo import Acervo

def test_adicionar_e_total_livros():
    acervo = Acervo("Biblioteca Municipal")
    livro = Livro("Dom Casmurro", "Machado de Assis", "111")
    acervo.adicionar_livro(livro)
    assert acervo.total_livros() == 1

def test_buscar_por_titulo():
    acervo = Acervo("Biblioteca")
    livro1 = Livro("O Senhor dos Aneis", "Tolkien", "222")
    acervo.adicionar_livro(livro1)
    resultados = acervo.buscar_por_titulo("senhor")
    assert len(resultados) == 1
    assert resultados[0].titulo == "O Senhor dos Aneis"

def test_buscar_por_autor():
    acervo = Acervo("Biblioteca")
    livro1 = Livro("O Hobbit", "Tolkien", "333")
    acervo.adicionar_livro(livro1)
    resultados = acervo.buscar_por_autor("Tolkien")
    assert len(resultados) == 1

def test_livros_disponiveis_e_emprestados():
    acervo = Acervo("Biblioteca")
    livro1 = Livro("Livro A", "Autor A", "1")
    livro2 = Livro("Livro B", "Autor B", "2")
    acervo.adicionar_livro(livro1)
    acervo.adicionar_livro(livro2)

    livro1.emprestar()

    assert len(acervo.livros_disponiveis()) == 1
    assert len(acervo.livros_emprestados()) == 1