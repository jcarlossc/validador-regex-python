from abc import ABC, abstractmethod

class Validador(ABC):
    """
    Interface abstrata (Estratégia).

    Define o contrato que todas as estratégias de validação concretas devem seguir.
    """
    @abstractmethod
    def validar(self, valor: str) -> bool:
        """
        Método abstrato para validar um determinado valor.

        Este método deve ser implementado por cada estratégia de validação concreta.

        Args:
            value (str): O valor a ser validado.

        Returns:
            bool: True se o valor for válido, False se inválido.
        """
        pass