import unittest
from abc import ABC, abstractmethod

class Validador(ABC):
    """
    Interface abstrata (Estratégia).
    """
    @abstractmethod
    def validar(self, valor: str) -> bool:
        pass

class ValidadorMock(Validador):
    """
    Classe concreta para teste(Mock).
    """
    def validar(self, valor: str) -> bool:
        return valor == "testando"

class TestValidador(unittest.TestCase):

    def test_validador_abstrato_nao_instanciavel(self):
        """
        Tentará instanciar a classe abstrata(que sendo uma interface,
        não pode ser instanciada).
        """
        with self.assertRaises(TypeError):
            validador = Validador()

    def test_validador_mock(self):
        """
        Implementação concreta de Validador.
        """
        validador = ValidadorMock()
        self.assertTrue(validador.validar("testando"))
        self.assertFalse(validador.validar("outro_teste"))

if __name__ == '__main__':
    unittest.main()
