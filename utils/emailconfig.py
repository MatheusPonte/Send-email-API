from flask_mail import Message
import os

def enviar_email_reset(email_destino, token, mail):
    frontend_url = os.getenv('FRONTEND_RESET_URL')
    link = f"{frontend_url}?token={token}"

    msg = Message("Recuperação de Senha", recipients=[email_destino])
    msg.body = f"""
    Olá!

    Clique no link abaixo para redefinir sua senha:

    {link}

    Se não foi você, apenas ignore este e-mail.
    """
    mail.send(msg)
