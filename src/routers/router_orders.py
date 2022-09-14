from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.schemas import Pedido
from src.infra.sqlalchemy.repository.repo_orders import RepositorioPedido
from src.infra.sqlalchemy.config.configs import get_db
from src.routers.router_auth import obter_usuario_logado


router = APIRouter()


@router.get("/pedidos")
def listar_pedidos(session: Session = Depends(get_db)):
    listar = RepositorioPedido(session).listar_pedidos()
    return listar

@router.post("/pedidos")
def criar_novo_pedido(pedido: Pedido, session: Session = Depends(get_db)):
    criar = RepositorioPedido(session).criar_novo_pedido(pedido)
    return criar

@router.get("/vendas/{usuario_id}")
def listar_vendas(usuario_id: int, pedido = Depends(obter_usuario_logado), session: Session = Depends(get_db)):
    vendas = RepositorioPedido(session).procurar_vendas(usuario_id)
    return vendas
