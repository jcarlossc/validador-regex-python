import re
from src.validador.Validador import Validador

class ValidadorData(Validador):
    def validar(self, valor: str) -> bool:
        try:
            regex = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação da data falhou: {e}")
            return False 