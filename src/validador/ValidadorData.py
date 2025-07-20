import re
from src.validador.Validador import Validador

class ValidadorData(Validador):
    def validar(self, valor: str) -> bool:
        regex = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        if not re.fullmatch(regex, valor):
            return False
        return True