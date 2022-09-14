from src.infra.sqlalchemy.config.configs import Base
from sqlalchemy import Column, Integer, String,  Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship



class Usuario(Base):
    __tablename__='usuario'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    email = Column(String)
    senha = Column(String)
    produto = relationship('Produto', back_populates='usuario')
    pedido = relationship('Pedido', back_populates='usuario')

class Produto(Base):
    __tablename__='produto'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='usuario_id_produto'))
    usuario = relationship('Usuario', back_populates='produto')
    pedido = relationship('Pedido', back_populates='produto')

class Pedido(Base):
    __tablename__='pedido'
    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(String)
    local_entrega = Column(String)
    tipo_entrega = Column(String)
    observacao = Column(String)
    produto_id = Column(Integer, ForeignKey('produto.id', name='produto_id_pedido'))
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='usuario_id_pedido'))
    produto = relationship('Produto', back_populates='pedido')
    usuario = relationship('Usuario', back_populates='pedido')