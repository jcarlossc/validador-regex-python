import unittest
from src.validador.ValidadorEmail import ValidadorEmail

class TestValidadorEmail(unittest.TestCase):

    def setUp(self):
        self.validador = ValidadorEmail()

    def test_emails_validos(self):
        """
        Testa endereços de e-mail com formatos válidos.
        """
        self.assertTrue(self.validador.validar('carlos@gmail.com'))
        self.assertTrue(self.validador.validar('carlos123@gmail.net'))
        self.assertTrue(self.validador.validar('carlos.costa+jose@gmail.org'))
        self.assertTrue(self.validador.validar('carlos_costa.jose@gmail.org'))
        self.assertTrue(self.validador.validar('jose@gmail.com.br'))

    def test_emails_invalidos(self):
        """
        Testa endereços de e-mail com formatos inválidos.
        """
        self.assertFalse(self.validador.validar('carlos@.com'))
        self.assertFalse(self.validador.validar('@gmail.net'))
        self.assertFalse(self.validador.validar('carlos@'))
        self.assertFalse(self.validador.validar('carlos'))
        self.assertFalse(self.validador.validar('carlos@gmail'))
        self.assertFalse(self.validador.validar('carlos@@gmail'))
        self.assertFalse(self.validador.validar('josé@gmail.com'))
        self.assertFalse(self.validador.validar('jose carlos@gmail.com'))
        self.assertFalse(self.validador.validar(''))
        self.assertFalse(self.validador.validar(None))

if __name__ == "__main__":
    unittest.main()
