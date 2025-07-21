import re
from src.validador.Validador import Validador

class ValidadorData(Validador):
    """
    Estratégia concreta para validação do formato de datas.

    Verifica se a string corresponde ao formato DD/MM/AAAA.
    """
    def validar(self, valor: str) -> bool:
        """
        Valida o formato de uma data no padrão DD/MM/AAAA usando uma expressão regular.

        Args:
            value (str): A data a ser validada.

        Returns:
            bool: True se a data for válida, False se inválida.
        """
        try:
            regex = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação da data falhou: {e}")
            return False 