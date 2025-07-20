import re
from src.validador.Validador import Validador

class ValidadorMonetarioBr(Validador):
    def validar(self, valor: str) -> bool:
        try:
            regex = r"^(R\$\s)?(\d{1,3}(?:\.\d{3})*|\d{1,3}),\d{2}$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação do valor monetário do Brasil falhou: {e}")
            return False 