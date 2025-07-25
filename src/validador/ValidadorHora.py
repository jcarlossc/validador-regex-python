import re
from src.validador.Validador import Validador

class ValidadorHora(Validador):
    """
    Estratégia concreta para validação do formato de horas.

    Verifica se a string corresponde aos formatos Hde hora
    """
    def validar(self, valor: str) -> bool:
        """
        Valida o formato de uma hora no padrão HH:MM ou HH:MM:SS usando uma expressão regular.

        Args:
            value (str): A hora a ser validada.

        Returns:
            bool: True se a hora for válida, False se inválida.
        """
        try:
            regex = r"^(?:2[0-3]|[01]?[0-9]):[0-5][0-9](?::[0-5][0-9])?$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação da hora falhou: {e}")
            return False 