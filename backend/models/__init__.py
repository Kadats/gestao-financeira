from models.base import Base, engine
from models.categoria import Categoria
from models.despesa import Despesa
from models.receita import Receita

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)