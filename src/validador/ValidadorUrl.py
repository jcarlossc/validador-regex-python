import re
from src.validador.Validador import Validador

class ValidadorUrl(Validador):
    def validar(self, valor: str) -> bool:
        try:
            regex = r"^(https?://)?([\da-z\.-]+)\.([a-z\.]{2,6})([/\w \.-]*)*\/?$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação da url falhou: {e}")
            return False 