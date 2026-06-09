"""
Tests básicos para Nemotron Superior
"""
import pytest
from src.domain.value_objects import PromptId, UserId
from src.shared.result import ok, err, is_ok, is_err


class TestBasicFunctionality:
    """Pruebas básicas de la infraestructura"""
    
    def test_prompt_id_creation(self):
        """Verificar que PromptId se crea correctamente"""
        import uuid
        test_uuid = uuid.uuid4()
        prompt_id = PromptId(test_uuid)
        assert str(prompt_id) == str(test_uuid)
    
    def test_user_id_creation(self):
        """Verificar que UserId se crea correctamente"""
        import uuid
        test_uuid = uuid.uuid4()
        user_id = UserId(test_uuid)
        assert str(user_id) == str(test_uuid)
    
    def test_result_ok(self):
        """Verificar Result pattern - caso exitoso"""
        result = ok(42)
        assert is_ok(result)
        assert not is_err(result)
        assert result.value == 42
    
    def test_result_err(self):
        """Verificar Result pattern - caso error"""
        result = err("error message")
        assert is_err(result)
        assert not is_ok(result)
        assert result.error == "error message"
    
    def test_python_version(self):
        """Verificar versión de Python"""
        import sys
        assert sys.version_info.major >= 3
        assert sys.version_info.minor >= 9
