import unittest
from abc import ABC, abstractmethod

class Validador(ABC):
    """
    Classe abstrata(Inteface).
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
        Tentativa de instanciar a classe abstrata.
        """
        with self.assertRaises(TypeError):
            validador = Validador()

    def test_validador_mock(self):
        """
        Usa uma implementação concreta de Validador.
        """
        validador = ValidadorMock()
        self.assertTrue(validador.validar("testando"))
        self.assertFalse(validador.validar("outro"))

if __name__ == '__main__':
    unittest.main()
