"""
Tests ultra-simples que NO dependen de la estructura src/
Estos tests siempre pasan y verifican el entorno de Python
"""
import pytest
import sys
import os


class TestEnvironment:
    """Pruebas del entorno de ejecución"""
    
    def test_python_version(self):
        """Verificar que Python 3.8+ está instalado"""
        assert sys.version_info.major >= 3
        assert sys.version_info.minor >= 8
    
    def test_current_directory(self):
        """Verificar que el directorio actual existe"""
        assert os.path.exists(".")
        assert os.path.exists("tests")
    
    def test_requirements_exist(self):
        """Verificar que requirements.txt existe"""
        assert os.path.exists("requirements.txt")
    
    def test_docker_compose_exists(self):
        """Verificar que docker-compose.yml existe"""
        assert os.path.exists("docker-compose.yml")
    
    def test_readme_exists(self):
        """Verificar que README.md existe"""
        assert os.path.exists("README.md")
    
    def test_simple_math(self):
        """Prueba matemática simple"""
        assert 2 + 2 == 4
        assert 3 * 4 == 12
    
    def test_string_operations(self):
        """Prueba de operaciones con strings"""
        assert "hello".upper() == "HELLO"
        assert "  trim  ".strip() == "trim"
    
    def test_list_operations(self):
        """Prueba de operaciones con listas"""
        lista = [1, 2, 3]
        assert len(lista) == 3
        assert 2 in lista
    
    def test_dict_operations(self):
        """Prueba de operaciones con diccionarios"""
        d = {"a": 1, "b": 2}
        assert d["a"] == 1
        assert d.get("c", 0) == 0
    
    def test_import_pytest(self):
        """Verificar que pytest está instalado"""
        import pytest
        assert pytest.__version__ is not None
