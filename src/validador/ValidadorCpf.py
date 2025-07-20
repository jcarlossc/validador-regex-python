import re
from src.validador.Validador import Validador

class ValidadorCpf(Validador):
    """
    Estratégia concreta para validação do formato de CPF.

    Verifica se o valor segue o padrão de 11 dígitos, com ou sem pontos e hífen.
    """
    def validar(self, valor: str) -> bool:
        """
        Valida o formato de um cpf usando uma expressão regular.

        Aceita formatos como '123.456.789-00' ou '12345678900'.

        Args:
            value (str): O cpf a ser validado.

        Returns:
            bool: True se o cpf for válido, False se inválido.
        """
        try:
            regex = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação do cpf falhou: {e}")
            return False 