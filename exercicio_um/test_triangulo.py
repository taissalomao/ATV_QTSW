import pytest
from triangulo import Triangulo

def test_triangulo_com_zero():
    # Um valor zero
    with pytest.raises(ValueError):
        Triangulo(0, 3, 4).tipo_triangulo()
    with pytest.raises(ValueError):
        Triangulo(3, 0, 4).tipo_triangulo()
    with pytest.raises(ValueError):
        Triangulo(3, 4, 0).tipo_triangulo()

def test_triangulo_com_negativo():
    # Um valor negativo
    with pytest.raises(ValueError):
        Triangulo(-1, 3, 4).tipo_triangulo()
    with pytest.raises(ValueError):
        Triangulo(3, -1, 4).tipo_triangulo()
    with pytest.raises(ValueError):
        Triangulo(3, 4, -1).tipo_triangulo()

def test_triangulo_com_lados_invalidos():
    # Casos em que a soma de 2 lados é igual ou menor que o terceiro lado
    with pytest.raises(ValueError):
        Triangulo(1, 2, 3).tipo_triangulo()
    with pytest.raises(ValueError):
        Triangulo(3, 1, 2).tipo_triangulo()
    with pytest.raises(ValueError):
        Triangulo(2, 3, 5).tipo_triangulo()
    with pytest.raises(ValueError):
        Triangulo(1, 1, 2).tipo_triangulo()
    with pytest.raises(ValueError):
        Triangulo(2, 2, 4).tipo_triangulo()

def test_triangulo_todos_lados_zero():
    # Todos os lados iguais a zero
    with pytest.raises(ValueError):
        Triangulo(0, 0, 0).tipo_triangulo()

def test_triangulo_equilatero():
    # Triângulo equilátero válido com diferentes tamanhos de lados
    assert Triangulo(5, 5, 5).tipo_triangulo() == "Equilátero"
    assert Triangulo(10, 10, 10).tipo_triangulo() == "Equilátero"

def test_triangulo_isosceles():
    # Triângulo isósceles válido com diferentes tamanhos de lados
    assert Triangulo(3, 3, 5).tipo_triangulo() == "Isósceles"
    assert Triangulo(4, 6, 4).tipo_triangulo() == "Isósceles"
    assert Triangulo(5, 4, 5).tipo_triangulo() == "Isósceles"

def test_triangulo_escaleno():
    # Triângulo escaleno válido com diferentes tamanhos de lados
    assert Triangulo(3, 4, 5).tipo_triangulo() == "Escaleno"
    assert Triangulo(5, 12, 13).tipo_triangulo() == "Escaleno"
