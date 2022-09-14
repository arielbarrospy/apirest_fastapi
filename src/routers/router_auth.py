from fastapi import APIRouter, Depends, status, HTTPException
from src.routers.router_utils import obter_usuario_logado
from src.infra.sqlalchemy.config.configs import get_db
from src.schemas.schemas import Usuario, LoginData, UsuarioSimples
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repository.repo_user import RepositorioUsuario
from typing import List
from src.infra.providers import hash_provider, token_provider


router = APIRouter()

@router.get("/usuarios", status_code=status.HTTP_200_OK, response_model=List[UsuarioSimples])
def listar_todos_usuario(session: Session = Depends(get_db)):
    listar = RepositorioUsuario(session).listar_todos_usuario()
    return listar

@router.post("/usuarios", status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    verificar = RepositorioUsuario(session).procurar_usuario_por_email(usuario.email)
    if verificar:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Email Já Existente !!!')
    usuario.senha = hash_provider.criar_hash(usuario.senha)
    criar = RepositorioUsuario(session).criar_novo_usuario(usuario)
    return criar

@router.get("/usuarios/{id}", status_code=status.HTTP_200_OK ,response_model=Usuario)
def procurar_usuario_por_id(id:int, session: Session = Depends(get_db)):
    procurar = RepositorioUsuario(session).procurar_usuario_por_id(id)
    return procurar

@router.put("/usuarios/{id}", status_code=status.HTTP_200_OK , response_model=Usuario)
def atualizar_usuario(id:int, usuario: Usuario, session: Session = Depends(get_db)):
    atualizar = RepositorioUsuario(session).atualizar_usuario(id, usuario)
    return atualizar

@router.delete("/usuarios/{id}",status_code=status.HTTP_202_ACCEPTED ,response_model=None)
def deletar_usuario(id: int, session: Session = Depends(get_db)):
    atualizar = RepositorioUsuario(session).deletar_usuario(id)
    return atualizar


@router.post("/token")
def logar_usuario(login: LoginData, session: Session = Depends(get_db)):
    print(login)
    email = login.email
    senha = login.senha
    usuario = RepositorioUsuario(session).procurar_usuario_por_email(email)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuario Não Cadastrado !!!')
    verificar_senha = hash_provider.verificar_hash(senha, usuario.senha)
    if not verificar_senha:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuario Ou Senha Invalídos !!!')
    token = token_provider.criar_token({"sub": usuario.email})
    return {"usuario": usuario, "token": token}

@router.get("/me")
def listar_usuario(usuario: Usuario = Depends(obter_usuario_logado)):
    return usuario