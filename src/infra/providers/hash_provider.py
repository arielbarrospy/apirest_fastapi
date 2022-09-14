from passlib.context import CryptContext


pwd = CryptContext(schemes=['bcrypt'])


def criar_hash(text):
    return pwd.hash(text)


def verificar_hash(text, text_hashed):
    return pwd.verify(text, text_hashed)