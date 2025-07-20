import re
from src.validador.Validador import Validador

class ValidadorCnpj(Validador):
    def validar(self, valor: str) -> bool:
        try:
            regex = r"^\d{2}\.?\d{3}\.?\d{3}\/?\d{4}-?\d{2}$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação do cpf falhou: {e}")
            return False 