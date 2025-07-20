import re
from src.validador.Validador import Validador

class validadorIp(Validador):
    def validar(self, valor: str) -> bool:
        regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        if not re.fullmatch(regex, valor):
            return False
        return True