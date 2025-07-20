import re
from src.validador.Validador import Validador

class ValidadorCpf(Validador):
    def validar(self, valor: str) -> bool:
        try:
            regex = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
            return re.fullmatch(regex, valor) is not None
        except Exception as e:
            print(f"Erro. A validaçao de cpf falhou: {e}")
            return False