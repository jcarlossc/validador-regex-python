import unittest
from src.validador.ContextoDeValidacao import ContextoDeValidacao
from src.validador.ValidadorCpf import ValidadorCpf
from src.validador.ValidadorEmail import ValidadorEmail
from src.validador.ValidadorCnpj import ValidadorCnpj
from src.validador.ValidadorData import ValidadorData
from src.validador.ValidadorHora import ValidadorHora
from src.validador.ValidadorUrl import ValidadorUrl
from src.validador.ValidadorIp import ValidadorIp
from src.validador.ValidadorMonetarioBr import ValidadorMonetarioBr

class TestContextoDeValidacao(unittest.TestCase):

    def test_validacao_com_ip_valido(self):
        contexto = ContextoDeValidacao(ValidadorIp())
        self.assertTrue(contexto.executar_validacao("255.255.255.255"))

    def test_validacao_com_hora_valida(self):
        contexto = ContextoDeValidacao(ValidadorHora())
        self.assertTrue(contexto.executar_validacao("12:44"))

    def test_validacao_com_cpf_valido(self):
        contexto = ContextoDeValidacao(ValidadorCpf())
        self.assertTrue(contexto.executar_validacao("123.456.789-00"))

    def test_validacao_com_email_valido(self):
        contexto = ContextoDeValidacao(ValidadorEmail())
        self.assertTrue(contexto.executar_validacao("teste@exemplo.com"))
        
    # Testes de troca de contexto em tempo de execução.
    def test_trocar_estrategia_para_cnpj(self):
        contexto = ContextoDeValidacao(ValidadorCpf())
        contexto.setar_validador(ValidadorCnpj())
        self.assertTrue(contexto.executar_validacao("12.345.678/0001-90"))

    def test_trocar_estrategia_para_valor_monetario(self):
        contexto = ContextoDeValidacao(ValidadorIp())
        contexto.setar_validador(ValidadorMonetarioBr())
        self.assertTrue(contexto.executar_validacao("4.444,00"))

    def test_trocar_estrategia_para_data(self):
        contexto = ContextoDeValidacao(ValidadorEmail())
        contexto.setar_validador(ValidadorData())
        self.assertTrue(contexto.executar_validacao("15/08/2023"))

    def test_trocar_estrategia_para_url(self):
        contexto = ContextoDeValidacao(ValidadorHora())
        contexto.setar_validador(ValidadorUrl())
        self.assertTrue(contexto.executar_validacao("www.teste.com"))    

    # Testes inválidos.
    def test_valor_invalido_retorna_false_email(self):
        contexto = ContextoDeValidacao(ValidadorEmail())
        self.assertFalse(contexto.executar_validacao("teste@.com"))

    def test_valor_invalido_retorna_false_cpf(self):
        contexto = ContextoDeValidacao(ValidadorCpf())
        self.assertFalse(contexto.executar_validacao("123456789-2"))

    def test_valor_invalido_retorna_false_cnpj(self):
        contexto = ContextoDeValidacao(ValidadorCnpj())
        self.assertFalse(contexto.executar_validacao("12345678923"))

    def test_valor_invalido_retorna_false_ip(self):
        contexto = ContextoDeValidacao(ValidadorIp())
        self.assertFalse(contexto.executar_validacao("789.0.0.14"))

    def test_valor_invalido_retorna_false_url(self):
        contexto = ContextoDeValidacao(ValidadorUrl())
        self.assertFalse(contexto.executar_validacao("htt:teste.com"))

    def test_valor_invalido_retorna_false_data(self):
        contexto = ContextoDeValidacao(ValidadorData())
        self.assertFalse(contexto.executar_validacao("45/12/2025"))

    def test_valor_invalido_retorna_false_valor_monetario(self):
        contexto = ContextoDeValidacao(ValidadorMonetarioBr())
        self.assertFalse(contexto.executar_validacao("123456,1"))

    def test_valor_invalido_retorna_false_hora(self):
        contexto = ContextoDeValidacao(ValidadorHora())
        self.assertFalse(contexto.executar_validacao("12:98:14"))

    def test_erro_na_estrategia_retorna_false(self):
        class ValidadorQueLancaErro:
            def validar(self, valor: str):
                raise ValueError("Erro simulado")

        contexto = ContextoDeValidacao(ValidadorQueLancaErro())
        self.assertFalse(contexto.executar_validacao("teste"))

if __name__ == "__main__":
    unittest.main()