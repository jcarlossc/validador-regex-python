import re
from src.validador.Validador import Validador

class ValidadorUrl(Validador):
    """
    Estratégia concreta para validação de URLs.

    Verifica se a string corresponde a um formato de URL.
    """
    def validar(self, valor: str) -> bool:
        """
        Valida uma URL usando uma expressão regular.

        Aceita URLs com ou sem 'http://' ou 'https://'.

        Args:
            value (str): A URL a ser validada.

        Returns:
            bool: True se a url for válida, False se inválida.
        """
        try:
            regex = r"^(https?://)?([\da-z\.-]+)\.([a-z\.]{2,6})([/\w \.-]*)*\/?$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação da url falhou: {e}")
            return False 