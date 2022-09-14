from src.schemas.schemas import Pedido
from src.infra.sqlalchemy.models import models
from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update



class RepositorioPedido():
    def __init__(self, session: Session):
        self.session = session

    def criar_novo_pedido(self, pedido: Pedido):
        db_pedido = models.Pedido(
            quantidade=pedido.quantidade,
            local_entrega=pedido.local_entrega,
            tipo_entrega=pedido.tipo_entrega,
            observacao=pedido.observacao,
            produto_id=pedido.produto_id,
            usuario_id=pedido.usuario_id
        )
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido

    def listar_pedidos(self):
        comando = select(models.Pedido)
        pedidos = self.session.execute(comando).scalars().all()
        return pedidos

    def procurar_vendas(self, usuario_id: int):
        comando = select(models.Pedido).join_from(models.Pedido, models.Produto).where(models.Produto.usuario_id == usuario_id)
        vendas = self.session.execute(comando).scalars().all()
        return vendas