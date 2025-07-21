import unittest
from src.validador.ValidadorIp import ValidadorIp

class TestValidadorIp(unittest.TestCase):

    def setUp(self):
        self.validador = ValidadorIp()

    def test_ips_validos(self):
        """
        Testa endereços IP válidos(IPv4).
        """
        self.assertTrue(self.validador.validar('192.168.0.1'))
        self.assertTrue(self.validador.validar('127.0.0.1'))
        self.assertTrue(self.validador.validar('10.0.0.255'))
        self.assertTrue(self.validador.validar('255.255.255.255'))
        self.assertTrue(self.validador.validar('0.0.0.0'))
        self.assertTrue(self.validador.validar('1.2.3.4'))

    def test_ips_invalidos(self):
        """
        Testa endereços IP inválidos com formatos ou valores incorretos.
        """
        self.assertFalse(self.validador.validar('256.100.100.100'))
        self.assertFalse(self.validador.validar('192.168.0.256'))
        self.assertFalse(self.validador.validar('123.456.78.90'))
        self.assertFalse(self.validador.validar('192.168.1'))
        self.assertFalse(self.validador.validar('192.168.1.1.1'))
        self.assertFalse(self.validador.validar('192.168..1'))
        self.assertFalse(self.validador.validar('abc.def.ghi.jkl'))
        self.assertFalse(self.validador.validar('192.168.1.-1'))
        self.assertFalse(self.validador.validar('192.168.1.01 '))
        self.assertFalse(self.validador.validar(''))
        self.assertFalse(self.validador.validar(None))

if __name__ == "__main__":
    unittest.main()
