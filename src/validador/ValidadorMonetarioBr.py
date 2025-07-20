import re
from src.validador.Validador import Validador

class ValidadorMonetarioBr(Validador):
    """
    Estratégia concreta para validação de valores monetários no formato brasileiro.

    Aceita valores com vírgula para decimais e ponto para milhares.
    """
    def validar(self, valor: str) -> bool:
        """
        Valida um valor monetário no formato brasileiro específico usando regex.

        Exemplos de formatos válidos: "0,23", "1,23", "10,23", "100,23",
        "1.235,20", "10.235,23", "R$ 1.235,20".

        Args:
            value (str): O valor monetário a ser validado.

        Returns:
            bool: True se o valor for válido, False se inválido.
        """
        try:
            regex = r"^(R\$\s)?(\d{1,3}(?:\.\d{3})*|\d{1,3}),\d{2}$"
            return re.fullmatch(regex, valor) is not None
        except (TypeError, re.error) as e:
            print(f"Erro. A validação do valor monetário do Brasil falhou: {e}")
            return False 