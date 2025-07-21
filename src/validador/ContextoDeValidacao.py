from src.validador.Validador import Validador

class ContextoDeValidacao:
    """
    Contexto que utiliza uma estratégia de validação para executar a validação.

    Permite a troca dinâmica da estratégia de validação em tempo de execução,
    seguindo o padrão de projeto Strategy.
    """
    def __init__(self, validador: Validador):
        """
        Inicializa o contexto de validação com uma estratégia específica.

        Args:
            validator (Validator): Uma instância de uma classe que implementa
                                   a interface Validator.
        """
        self._validador = validador

    def setar_validador(self, validador: Validador):
        """
        Define ou altera a estratégia de validação atual do contexto.

        Args:
            validator (Validator): A nova instância de estratégia de validação.
        """
        self._validador = validador

    def executar_validacao(self, valor: str) -> bool:
        """
        Executa a validação do valor utilizando a estratégia de validação configurada.

        Args:
            value (str): O valor a ser validado.

        Returns:
            bool: True se o valor for válido de acordo com a estratégia , False se inválido.
        """
        try:
            return self._validador.validar(valor)
        except Exception as e:
            print(f"Erro. A validação falhou: {e}")
            return False       