import re
from src.validador.Validador import Validador

class ValidadorEmail(Validador):
    """
    Estratégia concreta para validação de endereços de e-mail.

    Utiliza uma expressão regular para verificar o formato de e-mail.
    """
    def validar(self, valor: str) -> bool:
        """
        Valida um endereço de e-mail usando uma expressão regular.

        A regex utilizada é simples e cobre a maioria dos formatos.

        Args:
            value (str): O endereço de e-mail a ser validado.

        Returns:
            bool: True se o email for válido, False se inválido.
        """
        try:
            regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação do email falhou: {e}")
            return False 