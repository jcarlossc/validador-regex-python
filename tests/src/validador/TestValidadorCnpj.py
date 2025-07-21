import unittest
from src.validador.ValidadorCnpj import ValidadorCnpj

class TestValidadorCnpj(unittest.TestCase):

    def setUp(self):
        self.validador = ValidadorCnpj()

    def test_cnpjs_validos(self):
        """
        Testa CNPJs com formatos válidos.
        """
        self.assertTrue(self.validador.validar('11.222.333/0001-44'))
        self.assertTrue(self.validador.validar('11222333000144'))
        self.assertTrue(self.validador.validar('11.222333000144'))
        self.assertTrue(self.validador.validar('11222.333/0001-44'))

    def test_cnpjs_invalidos(self):
        """
        Testa CNPJs inválidos por formato incorreto.
        """
        self.assertFalse(self.validador.validar('11.222.333/0001'))
        self.assertFalse(self.validador.validar('11.222.333/0001-444'))
        self.assertFalse(self.validador.validar('112223330001'))
        self.assertFalse(self.validador.validar('abcd2233000144'))
        self.assertFalse(self.validador.validar(''))
        self.assertFalse(self.validador.validar(None))

if __name__ == "__main__":
    unittest.main()
