# Modelo da tabela Despesa

from sqlalchemy import Column, Integer, Numeric, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base import Base

class Despesa(Base):
    __tablename__ = "despesas"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    data = Column(Date, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)

    categoria = relationship("Categoria")
