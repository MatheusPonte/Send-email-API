from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)


EMAIL_ORIGEM = os.getenv("EMAIL_ORIGEM")
SENHA_EMAIL = os.getenv("SENHA_EMAIL")

@app.route('/enviar-email', methods=['POST'])
def enviar_email():
    data = request.get_json()

    destinatario = data.get('to') # Pra quem vai ser enviado
    assunto = data.get('subject') #Aqui fica a mensagem que irá enviar 
    corpo = data.get('content', 'Corpo padrão')

    if not destinatario:
        return jsonify({"erro": "Email do destinatário é obrigatório"}), 400

    try:
        msg = EmailMessage()
        msg['Subject'] = assunto
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = destinatario
        msg.set_content(corpo)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ORIGEM, SENHA_EMAIL)
            smtp.send_message(msg)

        return jsonify({"mensagem": "Email enviado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=7000)