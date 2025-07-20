import re
from src.validador.Validador import Validador

class ValidadorHora(Validador):
    def validar(self, valor: str) -> bool:
        try:
            regex = r"^(?:2[0-3]|[01]?[0-9]):[0-5][0-9](?::[0-5][0-9])?$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação da hora falhou: {e}")
            return False 