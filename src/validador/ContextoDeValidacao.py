from src.validador.Validador import Validador

class ContextoDeValidacao:
    def __init__(self, validador: Validador):
        self._validador = validador

    def setar_validador(self, validador: Validador):
        self._validador = validador

    def executar_validacao(self, valor: str) -> bool:
        return self._validador.validar(valor)        