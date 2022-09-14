from jose import jwt
from datetime import datetime, timedelta

EXPIRATE = 3000
SECRET_KEY = ""
ALGORITHM = "HS256"

def criar_token(data: dict):
    dados = data.copy()

    expirate = datetime.utcnow() + timedelta(EXPIRATE)

    dados.update({"exp": expirate})

    token = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get('sub')

