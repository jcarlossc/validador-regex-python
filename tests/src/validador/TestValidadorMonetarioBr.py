import unittest
from src.validador.ValidadorMonetarioBr import ValidadorMonetarioBr

class TestValidadorMonetarioBr(unittest.TestCase):

    def setUp(self):
        self.validador = ValidadorMonetarioBr()

    def test_valores_validos(self):
        """
        Testa valores monetários válidos(formato brasileiro).
        """
        self.assertTrue(self.validador.validar('0,44'))
        self.assertTrue(self.validador.validar('1,00'))
        self.assertTrue(self.validador.validar('10,99'))
        self.assertTrue(self.validador.validar('100,99'))
        self.assertTrue(self.validador.validar('999,99'))
        self.assertTrue(self.validador.validar('1.000,00'))
        self.assertTrue(self.validador.validar('11.000,99'))
        self.assertTrue(self.validador.validar('9.199.000,99'))
        self.assertTrue(self.validador.validar('R$ 44.000,00'))
        self.assertTrue(self.validador.validar('R$ 0,44'))
        self.assertTrue(self.validador.validar('R$ 44.444.444.444,44'))

    def test_valores_invalidos(self):
        """
        Testa valores monetários inválidos(formato brasileiro).
        """
        self.assertFalse(self.validador.validar('987456321,00'))
        self.assertFalse(self.validador.validar('1.000,0'))
        self.assertFalse(self.validador.validar('1.000,000'))
        self.assertFalse(self.validador.validar('1.000.0000,00'))
        self.assertFalse(self.validador.validar('1.000.000'))
        self.assertFalse(self.validador.validar('R$1.000,45'))
        self.assertFalse(self.validador.validar('R $ 44.000,00'))
        self.assertFalse(self.validador.validar('cinco mil reais'))
        self.assertFalse(self.validador.validar(''))
        self.assertFalse(self.validador.validar(None))

if __name__ == "__main__":
    unittest.main()
