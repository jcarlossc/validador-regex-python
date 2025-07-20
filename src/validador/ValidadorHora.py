import re
from src.validador.Validador import Validador

class ValidadorHora(Validador):
    def validar(self, valor: str) -> bool:
        regex = r"^(?:2[0-3]|[01]?[0-9]):[0-5][0-9](?::[0-5][0-9])?$"
        if not re.fullmatch(regex, valor):
            return False
        return True