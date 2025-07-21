import unittest
from src.validador.ValidadorCpf import ValidadorCpf

class TestValidadorCpf(unittest.TestCase):

    def setUp(self):
        self.validador = ValidadorCpf()

    def test_cpfs_validos(self):
        """
        Testa CPFs com formatos válidos.
        """
        self.assertTrue(self.validador.validar('12345678912'))
        self.assertTrue(self.validador.validar('123.456.789-12'))
        self.assertTrue(self.validador.validar('123.45678912'))
        self.assertTrue(self.validador.validar('123456.789-12'))

    def test_cpfs_invalidos(self):
        """
        Testa CPFs inválidos por formato incorreto.
        """
        self.assertFalse(self.validador.validar('1234567891'))
        self.assertFalse(self.validador.validar('123-456-789-12'))
        self.assertFalse(self.validador.validar('123-456-789-123'))
        self.assertFalse(self.validador.validar('abc.def.ghi-jk'))
        self.assertFalse(self.validador.validar(''))
        self.assertFalse(self.validador.validar(None))

if __name__ == "__main__":
    unittest.main()