from abc import ABC, abstractmethod

class Validador(ABC):
    @abstractmethod
    def validar(self, valor: str) -> bool:
        pass