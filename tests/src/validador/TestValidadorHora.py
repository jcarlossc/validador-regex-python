import unittest
from src.validador.ValidadorHora import ValidadorHora

class TestValidadorHora(unittest.TestCase):

    def setUp(self):
        self.validador = ValidadorHora()

    def test_horas_validas(self):
        """
        Testa horas válidas(HH:MM e HH:MM:SS).
        """
        self.assertTrue(self.validador.validar('00:00'))
        self.assertTrue(self.validador.validar('09:30'))
        self.assertTrue(self.validador.validar('23:59'))
        self.assertTrue(self.validador.validar('00:00:00'))
        self.assertTrue(self.validador.validar('12:30:40'))
        self.assertTrue(self.validador.validar('23:59:59'))

    def test_horas_invalidas(self):
        """
        Testa horas formatos inválidos.
        """
        self.assertFalse(self.validador.validar('24:00'))
        self.assertFalse(self.validador.validar('12:60'))
        self.assertFalse(self.validador.validar('12:12:60'))
        self.assertFalse(self.validador.validar('99:99'))
        self.assertFalse(self.validador.validar('125:50'))
        self.assertFalse(self.validador.validar('12:580'))
        self.assertFalse(self.validador.validar('12:30:5'))
        self.assertFalse(self.validador.validar('12:30:'))
        self.assertFalse(self.validador.validar('hora'))
        self.assertFalse(self.validador.validar(''))
        self.assertFalse(self.validador.validar(None))

if __name__ == "__main__":
    unittest.main()
