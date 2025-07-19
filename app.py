from src.validador.ContextoDeValidacao import ContextoDeValidacao
from src.validador.ValidadorEmail import ValidadorEmail

validador_email = ValidadorEmail()

contexto = ContextoDeValidacao(validador_email)

print(contexto.executar_validacao('jose@gmail.com'))