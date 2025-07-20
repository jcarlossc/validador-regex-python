import re
from src.validador.Validador import Validador

class ValidadorCnpj(Validador):
    """
    Estratégia concreta para validação do formato de CNPJ.

    Verifica se o valor segue o padrão de 14 dígitos, com ou sem pontos, barras e hífen.
    """
    def validar(self, valor: str) -> bool:
        """
        Valida o formato de um CNPJ usando uma expressão regular.

        Aceita formatos como '11.222.333/0001-44' ou '11222333000144'.

        Args:
            value (str): O CNPJ a ser validado.

        Returns:
            bool: True se o cnpj for válido, False se inválido.
        """
        try:
            regex = r"^\d{2}\.?\d{3}\.?\d{3}\/?\d{4}-?\d{2}$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação do cpf falhou: {e}")
            return False 