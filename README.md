# Validador Regex Python

Estudo sobre orientação a objetos com linguagem de programação Python e módulo re para validação, implementado com base no padrão de projeto comportamental Estratégia(Strategy).

---

## Funcionalidades

- Validação de:
- Cnpj 
- Cpf
- Datas
- Email
- Hora
- Ip
- Valor monetário brasileiro
- Url

---

## Ferramentas utilizadas

- Python 3.9.13
- Ambiente virtual `venv`
- Módulo `re`
- `unittest` para testes
- Git/GitHub
- Visual Studio Code
- Sistema operacional Windows 10

---

## Requisitos

- Python 3.x
- Módulo `re`

---

## Como utilizar

```bash
# Clone o repositório
git clone https://github.com/jcarlossc/validador-regex-python

# Acesse o diretório
cd validador-regex-python

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate           # Windows
source venv/bin/activate        # Linux/macOS

# Instale as dependências. Obs: este projeto não tem módulos externos
pip install -r requirements.txt

# Execute a aplicação
python app.py

# Para sair do ambiente virtual
deactivate
```
---

## Contribuição:

Se quiser contribuir para este projeto, fique à vontade para enviar um pull request ou relatar problemas na seção de issues.

---

## Licença:

Este projeto é licenciado sob a Licença MIT.

---

## Comandos importantes:

```bash
python -m venv venv               # Cria um ambiente virtual
venv\Scripts\activate             # Ativa o ambiente no Windows
source venv/bin/activate          # Ativa o ambiente no Linux/macOS
deactivate                        # Encerra o ambiente virtual

pip install nome-pacote           # Instala um pacote
pip uninstall nome-pacote         # Remove um pacote
pip freeze > requirements.txt     # Gera (ou atualiza) o arquivo de dependências
pip install -r requirements.txt   # Instala pacotes listados no requirements.txt
pip list                          # Lista pacotes instalados
pip show nome-pacote              # Exibe detalhes de um pacote
```