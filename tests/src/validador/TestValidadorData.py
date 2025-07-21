import unittest
from src.validador.ValidadorData import ValidadorData

class TestValidadorData(unittest.TestCase):

    def setUp(self):
        self.validador = ValidadorData()

    def test_datas_validas(self):
        """
        Testa datas com formatos válidos(DD/MM/AAAA).
        """
        self.assertTrue(self.validador.validar('01/01/2000'))
        self.assertTrue(self.validador.validar('31/12/2023'))
        self.assertTrue(self.validador.validar('29/02/2020'))
        self.assertTrue(self.validador.validar('15/08/1999'))

    def test_datas_invalidas(self):
        """
        Testa datas inválidas por formato incorreto.
        """
        self.assertFalse(self.validador.validar('32/01/2020'))
        self.assertFalse(self.validador.validar('00/01/2020'))
        self.assertFalse(self.validador.validar('15/13/2020'))
        self.assertFalse(self.validador.validar('15/00/2020'))
        self.assertFalse(self.validador.validar('15-08-2020'))
        self.assertFalse(self.validador.validar('2020/08/15'))
        self.assertFalse(self.validador.validar('15/8/2020'))
        self.assertFalse(self.validador.validar('1/08/2020'))
        self.assertFalse(self.validador.validar(''))
        self.assertFalse(self.validador.validar(None))

if __name__ == "__main__":
    unittest.main()