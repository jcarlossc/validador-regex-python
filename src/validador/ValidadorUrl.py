import re
from src.validador.Validador import Validador

class ValidadorUrl(Validador):
    def validar(self, valor: str) -> bool:
        regex = r"^(https?://)?([\da-z\.-]+)\.([a-z\.]{2,6})([/\w \.-]*)*\/?$"
        if not re.fullmatch(regex, valor):
            return False
        return True