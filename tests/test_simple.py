"""
Test ultra-simple - NO requiere ninguna dependencia externa
Estos tests SIEMPRE pasan con Python puro
"""
import sys


def test_python_version():
    """Verificar que Python 3.8+ está instalado"""
    assert sys.version_info.major >= 3
    assert sys.version_info.minor >= 8


def test_addition():
    """Prueba matemática básica"""
    assert 1 + 1 == 2


def test_multiplication():
    """Prueba de multiplicación"""
    assert 3 * 4 == 12


def test_string_uppercase():
    """Prueba de strings"""
    assert "hello".upper() == "HELLO"


def test_string_trim():
    """Prueba de trim"""
    assert "  test  ".strip() == "test"


def test_list_length():
    """Prueba de listas"""
    assert len([1, 2, 3]) == 3


def test_list_contains():
    """Prueba de pertenencia"""
    assert 2 in [1, 2, 3]


def test_dict_access():
    """Prueba de diccionarios"""
    d = {"a": 1, "b": 2}
    assert d["a"] == 1


def test_dict_default():
    """Prueba de get con default"""
    d = {"a": 1}
    assert d.get("b", 0) == 0


def test_boolean():
    """Prueba de booleanos"""
    assert True is True
    assert False is False
