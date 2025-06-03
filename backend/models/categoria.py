from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    categoria_pai_id = Column(Integer, ForeignKey('categorias.id'), nullable=True)

    subcategorias = relationship("Categoria", remote_side=[id])
