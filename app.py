from src.validador.ContextoDeValidacao import ContextoDeValidacao
from src.validador.ValidadorCnpj import ValidadorCnpj
from src.validador.ValidadorCpf import ValidadorCpf
from src.validador.ValidadorEmail import ValidadorEmail
from src.validador.ValidadorUrl import ValidadorUrl

# Instâncias das estratégias de validação.
validador_email = ValidadorEmail()
validador_cpf = ValidadorCpf()
validador_cnpj = ValidadorCnpj()
validador_url = ValidadorUrl()

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

print("\n--- Validação de CNPJ ---")
contexto.setar_validador(validador_cnpj)
print(f"'11.222.333/0001-44' é um cnpj válido? {contexto.executar_validacao('11.222.333/0001-44')}")
print(f"'11222333000144' é um cnpj válido? {contexto.executar_validacao('11222333000144')}")
print(f"'11.222.333/0001-444' é um cnpj válido? {contexto.executar_validacao('11.222.333/0001-444')}")
print(f"'11.222.333/0001.44' é um cnpj válido? {contexto.executar_validacao('11.222.333/0001.44')}")

print("\n--- Validação de URL ---")
contexto.setar_validador(validador_url)
print(f"'https://www.google.com' é uma url válida? {contexto.executar_validacao('https://www.google.com')}")
print(f"'http://localhost:8080/' é uma url válida? {contexto.executar_validacao('http://localhost:8080/')}")
print(f"'www.invalida' é uma url válida? {contexto.executar_validacao('www.invalid')}")