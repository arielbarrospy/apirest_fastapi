from src.schemas.schemas import Produto
from src.infra.sqlalchemy.models import models
from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update


class RepositorioProduto():
    def __init__(self, session: Session):
        self.session = session

    def criar_produto(self, produto: Produto):
        db_produto = models.Produto(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponivel=produto.disponivel,
            usuario_id=produto.usuario_id
        )
        
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto
    

    def listar_produtos(self):
        comando = select(models.Produto)
        produtos = self.session.execute(comando).scalars().all()
        return produtos


    def procurar_produto_por_id(self, id:int):
        comando = select(models.Produto).filter_by(id=id)
        produto = self.session.execute(comando).scalar()
        return produto
    
    def procurar_produto_por_id_usuario(self, id:id):
        comando = select(models.Produto).where(models.Produto.usuario_id == id)
        produtos = self.session.execute(comando)
        return produtos
    
    