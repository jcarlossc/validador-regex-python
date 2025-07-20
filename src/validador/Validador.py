from abc import ABC, abstractmethod

class Validador(ABC):
    """
    Interface abstrata para todas as estratégias de validação.
    """
    @abstractmethod
    def validar(self, valor: str) -> bool:
        """
        Método abstrato para validar um valor.
        Deverá ser implementado por todas as estratégias concretas.
        """
        pass