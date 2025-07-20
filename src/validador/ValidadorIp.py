import re
from src.validador.Validador import Validador

class ValidadorIp(Validador):
    """
    Estratégia concreta para validação de endereços IP no formato ipv4.

    Verifica se o valor consiste em quatro octetos numéricos separados por pontos.
    """
    def validar(self, valor: str) -> bool:
        """
        Valida um endereço ipv4 usando uma expressão regular.

        Verifica se cada octeto numérico está dentro do intervalo válido (0-255).

        Args:
            value (str): O endereço ip a ser validado.

        Returns:
            bool: True se o ip for válido, False se inválido.
        """
        try:
            regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação do IP falhou: {e}")
            return False 