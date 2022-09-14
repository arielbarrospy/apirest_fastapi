from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.configs import get_db
from src.schemas.schemas import Produto
from fastapi import APIRouter, Depends, status, HTTPException
from src.infra.sqlalchemy.repository.repo_product import RepositorioProduto



router = APIRouter()


@router.get("/produtos")
def listar_produtos(session: Session = Depends(get_db)):
    listar = RepositorioProduto(session).listar_produtos()
    return listar


@router.post("/produtos")
def criar_produto(produto: Produto, session: Session = Depends(get_db)):
    criar = RepositorioProduto(session).criar_produto(produto)
    return criar