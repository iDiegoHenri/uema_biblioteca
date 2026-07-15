import pytest
from biblioteca.livro import Livro

def test_criar_livro():
    livro = Livro("1984", "George Orwell", "12345")
    assert livro.titulo == "1984"
    assert livro.disponivel is True

def test_emprestar_livro_disponivel():
    livro = Livro("1984", "George Orwell", "12345")
    livro.emprestar()
    assert livro.disponivel is False

def test_emprestar_livro_ja_emprestado_levanta_erro():
    livro = Livro("1984", "George Orwell", "12345")
    livro.emprestar()
    with pytest.raises(ValueError):
        livro.emprestar()

# --- Novos testes adicionados para o método devolver() ---

def test_devolver_livro_emprestado():
    # Testa se um livro emprestado pode ser devolvido
    livro = Livro("1984", "George Orwell", "12345")
    livro.emprestar()
    livro.devolver()
    assert livro.disponivel is True

def test_devolver_livro_ja_disponivel_levanta_erro():
    # Testa se tentar devolver um livro que já está disponível gera um erro
    livro = Livro("1984", "George Orwell", "12345")
    with pytest.raises(ValueError):
        livro.devolver()