from src.validador.Validador import Validador

class ContextoDeValidacao:
    def __init__(self, validador: Validador):
        self._validador = validador

    def setar_validador(self, validador: Validador):
        self._validador = validador

    def executar_validacao(self, valor: str) -> bool:
        try:
            return self._validador.validar(valor)        
        except Exception as e:
            print(f"Erro. A validação falhou: {e}")
            return False