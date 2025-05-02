# API Flask de Envio de E-mails

Essa é uma API simples feita com Flask, que permite enviar e-mails para um destinatário especificado. Ela usa o servidor SMTP do Gmail para enviar os e-mails. A API recebe requisições em JSON com o endereço de e-mail, o assunto e a mensagem a ser enviada.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `Flask`
  - `python-dotenv`

Se ainda não tiver essas bibliotecas instaladas, siga as instruções abaixo.

## Como rodar a API

### 1. Clone o repositório

```bash
git clone https://seu_repositorio.git
cd nome_do_repositorio
```
### 2. Crie e ative um ambiente virtual 

python -m venv venv
source venv/bin/activate   # Para Linux/Mac
venv\Scripts\activate      # Para Windows

### 3. Instale as dependências

pip install -r requirements.txt

### 4. Crie o arquivo .env
EMAIL_ORIGEM=seu_email@gmail.com
SENHA_EMAIL=sua_senha_ou_senha_de_app

### 5. Execute o servidor Flask
python main.py


### 6. Testando a API
Agora que o servidor está rodando, você pode enviar uma requisição POST para o endpoint /enviar-email usando qualquer ferramenta de requisições HTTP, como o Postman ou curl.

Exemplo de requisição POST:

URL: http://127.0.0.1:7000/enviar-email
Método: POST
Cabeçalhos:

Content-Type: application/json

Corpo (JSON):

```
{
  "email": "destinatario@exemplo.com",
  "assunto": "Assunto do email",
  "mensagem": "Conteúdo do email"
}
```






