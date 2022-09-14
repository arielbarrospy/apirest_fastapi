from typing import List, Optional
from pydantic import BaseModel



class Usuario(BaseModel):
    id: Optional[int]
    nome: str
    telefone: str
    email: str
    senha: str

    class Config:
        orm_mode = True




class Produto(BaseModel):
    id: Optional[int]
    nome: str
    detalhes: str
    preco: float
    disponivel: bool
    usuario_id: Optional[int]

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[int]
    quantidade: int
    local_entrega: str
    tipo_entrega: str
    observacao: Optional[str]
    produto_id: Optional[int]
    usuario_id: Optional[int]
    class Config:
        orm_mode = True


class LoginData(BaseModel):
    email: str
    senha: str






class UsuarioSimples(BaseModel):
    id: Optional[int]
    nome: str
    telefone: str
    email: str
    produto: List[Produto]
    pedido: List[Pedido]

    class Config:
        orm_mode = True