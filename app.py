from src.validador.ContextoDeValidacao import ContextoDeValidacao
from src.validador.ValidadorCpf import ValidadorCpf
from src.validador.ValidadorEmail import ValidadorEmail

# Instâncias das estratégias de validação.
validador_email = ValidadorEmail()
validador_cpf = ValidadorCpf()

# Contexto de validação.
contexto = ContextoDeValidacao(validador_email)

print("\n--- Validação de E-mail ---")
print(f"'carlos@gmail.com' é um email válido? {contexto.executar_validacao('jose@gmail.com')}")
print(f"'carlos@.com' é um email válido? {contexto.executar_validacao('carlos@.com')}")

print("\n--- Validação de CPF ---")
contexto.setar_validador(validador_cpf)
print(f"'123.456.789-00' é um cpf válido? {contexto.executar_validacao('123.456.789-00')}")
print(f"'12345678900' é um cpf válido? {contexto.executar_validacao('12345678900')}")
print(f"'123.456.789.00' é um cpf válido? {contexto.executar_validacao('123.456.789.00')}")
print(f"'123.456.789-000' é um cpf válido? {contexto.executar_validacao('123.456.789-000')}")

