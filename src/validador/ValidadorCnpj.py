import re
from src.validador.Validador import Validador

class ValidadorCnpj(Validador):
    def validar(self, valor: str) -> bool:
        regex = r"^\d{2}\.?\d{3}\.?\d{3}\/?\d{4}-?\d{2}$"
        if not re.fullmatch(regex, valor):
            return False
        return True