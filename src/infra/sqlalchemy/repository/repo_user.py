from src.schemas.schemas import Usuario
from src.infra.sqlalchemy.models import models
from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update


class RepositorioUsuario():
    def __init__(self, session: Session):
        self.session = session

    def criar_novo_usuario(self, usuario: Usuario) -> models.Usuario:
        db_usuario = models.Usuario(
            nome=usuario.nome,
            telefone=usuario.telefone,
            email=usuario.email,
            senha=usuario.senha
        )

        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario

    def listar_todos_usuario(self) -> models.Usuario:
        comando = select(models.Usuario)
        usuarios = self.session.execute(comando).scalars().all()
        return usuarios

    def procurar_usuario_por_id(self, id: int) -> models.Usuario:
        comando = select(models.Usuario).filter_by(id=id)
        usuario = self.session.execute(comando).scalar()
        return usuario
    
    def atualizar_usuario(self, id: int, usuario: Usuario) -> Usuario:
        comando = update(models.Usuario).where(models.Usuario.id == id).values(
            nome=usuario.nome,
            telefone=usuario.telefone,
            email=usuario.email
        )
        atualizar = self.session.execute(comando)
        self.session.commit()
        pegar_usuario = select(models.Usuario).filter_by(id=id)
        usuario = self.session.execute(pegar_usuario).scalar()

        return usuario
    
    def deletar_usuario(self, id: int) -> None:
        comando = delete(models.Usuario).where(models.Usuario.id == id)
        executar = self.session.execute(comando)
        self.session.commit()
        return None

    def procurar_usuario_por_email(self, email: str) -> models.Usuario:
        comando = select(models.Usuario).filter_by(email=email)
        usuario = self.session.execute(comando).scalar()
        return usuario
