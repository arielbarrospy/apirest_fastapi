from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from src.infra.sqlalchemy.repository.repo_user import RepositorioUsuario
from src.infra.sqlalchemy.config.configs import get_db
from src.infra.providers import token_provider
from sqlalchemy.orm import Session


oauth_teste = OAuth2PasswordBearer(tokenUrl='token')

def obter_usuario_logado(token: str = Depends(oauth_teste), session: Session = Depends(get_db)):
    email = token_provider.verificar_token(token)
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Sem Altorização!!!')

    usuario = RepositorioUsuario(session).procurar_usuario_por_email(email)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Sem Altorização!!!')

    return usuario

