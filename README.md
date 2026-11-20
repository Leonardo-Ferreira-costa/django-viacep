# Consulta de CEP

Uma aplicação web simples e elegante feita com **Django**, criada para consultar endereços brasileiros a partir do CEP.

Digite um CEP com ou sem hífen, consulte os dados em tempo real pela API pública ViaCEP e receba respostas claras para CEPs inválidos ou não encontrados.

## Funcionalidades

- Consulta de CEP em uma interface limpa e responsiva
- Aceita CEP com ou sem hífen
- Validação de formato antes da requisição
- Exibição de logradouro, bairro, cidade e UF
- Tratamento de CEP inexistente
- Tratamento de falhas de conexão
- Proteção contra CSRF no formulário

## Tecnologias

- Python 3.15
- Django 6.1.3
- Requests
- SQLite
- HTML e CSS
- API ViaCEP

## Como executar

### 1. Clone ou acesse o projeto

```bash
cd C:\Users\Leonardo\Downloads\teste
```

### 2. Crie um ambiente virtual

```powershell
python -m venv env
```

### 3. Ative o ambiente virtual

**Windows PowerShell**

```powershell
.\env\Scripts\Activate.ps1
```

**Prompt de Comando**

```bat
env\Scripts\activate.bat
```

### 4. Instale as dependências

```bash
python -m pip install --upgrade pip
python -m pip install -r requeriments.txt
```

### 5. Prepare o banco de dados

```bash
python manage.py migrate
```

### 6. Inicie o servidor

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/cep/

## Como usar

1. Abra a página de consulta.
2. Informe um CEP válido, por exemplo: `01001-000`.
3. Clique em **Buscar CEP**.
4. Visualize os dados do endereço encontrados pela API.

## Estrutura do projeto

```text
teste/
├── app/
│   ├── migrations/
│   ├── templates/
│   │   └── cep.html
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── sistemas/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── requeriments.txt
```

## Rota disponível

| Método | Caminho | Descrição |
|---|---|---|
| `GET` | `/cep/` | Exibe o formulário de consulta |
| `POST` | `/cep/` | Consulta o CEP informado na API ViaCEP |
| `GET` | `/admin/` | Área administrativa do Django |

## Validações

A consulta exige exatamente oito dígitos numéricos após remover hífens e espaços.

Exemplos válidos:

- `01001-000`
- `01001000`

A aplicação pode informar:

- `CEP inválido. Digite 8 números.`
- `CEP não encontrado.`
- `Erro ao conectar com o serviço do ViaCEP. Tente novamente.`

## Testes

Execute os testes do projeto com:

```bash
python manage.py test
```

## Observações

- É necessária conexão com a internet para consultar o ViaCEP.
- O projeto utiliza o banco SQLite local `db.sqlite3`.
- O arquivo de dependências possui o nome `requeriments.txt`.
- Este projeto é destinado a estudos e pode ser usado como base para versões com histórico de consultas, cache ou interface mais avançada.

## Licença

Este projeto não possui uma licença definida. Caso queira distribuir ou reutilizar o código publicamente, adicione uma licença adequada ao repositório.
