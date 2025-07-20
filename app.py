from src.validador.ContextoDeValidacao import ContextoDeValidacao
from src.validador.ValidadorCnpj import ValidadorCnpj
from src.validador.ValidadorCpf import ValidadorCpf
from src.validador.ValidadorData import ValidadorData
from src.validador.ValidadorEmail import ValidadorEmail
from src.validador.ValidadorHora import ValidadorHora
from src.validador.ValidadorMonetarioBr import ValidadorMonetarioBr
from src.validador.ValidadorUrl import ValidadorUrl
from src.validador.ValidadorIp import ValidadorIp

# Instâncias das estratégias de validação.
validador_email = ValidadorEmail()
validador_cpf = ValidadorCpf()
validador_cnpj = ValidadorCnpj()
validador_url = ValidadorUrl()
validador_ip = ValidadorIp()
validador_monetario_br = ValidadorMonetarioBr()
validador_data = ValidadorData()
validador_hora = ValidadorHora()

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

print("\n--- Validação de IP ---")
contexto.setar_validador(validador_ip)
print(f"'192.168.1.1' é um ip válido? {contexto.executar_validacao('192.168.1.1')}")
print(f"'255.255.255.255' é um ip válido? {contexto.executar_validacao('255.255.255.255')}")
print(f"'256.0.0.1' é um ipválido? {contexto.executar_validacao('256.0.0.1')}")

print("\n--- Validação de Valores Monetários ---")
contexto.setar_validador(validador_monetario_br)
print(f"'R$ 1.234,56' é um valor válido? {contexto.executar_validacao('R$ 1.234,56')}")
print(f"'1234.56' é um valor válido? {contexto.executar_validacao('1234.56')}")
print(f"'50,00' é um valor válido? {contexto.executar_validacao('50,00')}")
print(f"'R$ 1,234.56' é um valor válido? {contexto.executar_validacao('R$ 1,234.56')}")

print("\n--- Validação de Data ---")
contexto.setar_validador(validador_data)
print(f"'19/07/2025' é uma data válida? {contexto.executar_validacao('19/07/2025')}")
print(f"'01/01/1900' é uma data válida? {contexto.executar_validacao('01/01/1900')}")
print(f"'32/01/2025' é uma data válida? {contexto.executar_validacao('32/01/2025')}") 
print(f"'01-01-2023' é uma data válida? {contexto.executar_validacao('01-01-2023')}")

print("\n--- Validação de Hora ---")
contexto.setar_validador(validador_hora)
print(f"'14:30' é válido? {contexto.executar_validacao('14:30')}")
print(f"'23:59:59' é válido? {contexto.executar_validacao('23:59:59')}")
print(f"'25:00' é válido? {contexto.executar_validacao('25:00')}")
print(f"'10:65' é válido? {contexto.executar_validacao('10:65')}")