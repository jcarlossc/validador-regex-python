import re
from src.validador.Validador import Validador

class ValidadorEmail(Validador):
    def validar(self, valor: str) -> bool:
        regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.fullmatch(regex, valor) is not None