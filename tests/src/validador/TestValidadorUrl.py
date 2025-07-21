import unittest
from src.validador.ValidadorUrl import ValidadorUrl

class TestValidadorUrl(unittest.TestCase):

    def setUp(self):
        self.validador = ValidadorUrl()

    def test_urls_validas(self):
        """
        Testa URLs válidas com e sem protocolo.
        """
        self.assertTrue(self.validador.validar('www.carlos.com.br'))
        self.assertTrue(self.validador.validar('https://carlos.com.br/caminho/arquivo.txt'))
        self.assertTrue(self.validador.validar('https://soares.com.br/'))
        self.assertTrue(self.validador.validar('https://carlos.com/pagina.html'))
        self.assertTrue(self.validador.validar('https://teste.com/um/dois/'))
        self.assertTrue(self.validador.validar('https://teste.com.br/pagina'))
        self.assertTrue(self.validador.validar('teste.com'))
        self.assertTrue(self.validador.validar('http://teste.com'))

    def test_urls_invalidas(self):
        """
        Testa URLs com formatação incorreta.
        """
        self.assertFalse(self.validador.validar('://exemplo.com'))
        self.assertFalse(self.validador.validar('http://com.'))
        self.assertFalse(self.validador.validar('http://.com'))
        self.assertFalse(self.validador.validar('https://.com'))
        self.assertFalse(self.validador.validar('teste'))
        self.assertFalse(self.validador.validar('htp://exemplo.com'))
        self.assertFalse(self.validador.validar('http:/teste.com'))
        self.assertFalse(self.validador.validar('http//exemplo.com'))

if __name__ == "__main__":
    unittest.main()
