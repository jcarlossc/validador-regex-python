import re
from src.validador.Validador import Validador

class ValidadorMonetarioBr(Validador):
    def validar(self, valor: str) -> bool:
        regex = r"^(R\$\s)?(\d{1,3}(?:\.\d{3})*|\d{1,3}),\d{2}$"
        if not re.fullmatch(regex, valor):
            return False
        return True