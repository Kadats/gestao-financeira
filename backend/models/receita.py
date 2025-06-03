# Modelo da tabela Receita

from sqlalchemy import Column, ForeignKey, Integer, Numeric, Date, String
from sqlalchemy.orm import relationship
from models.base import Base

class Receita(Base):
    __tablename__ = "receitas"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    data = Column(Date, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=True)

    categoria = relationship("Categoria")
