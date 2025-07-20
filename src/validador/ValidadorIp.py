import re
from src.validador.Validador import Validador

class ValidadorIp(Validador):
    def validar(self, valor: str) -> bool:
        try:
            regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação do IP falhou: {e}")
            return False 