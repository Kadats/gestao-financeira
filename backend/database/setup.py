from models.base import Base, engine
from models.categoria import Categoria
from models.despesa import Despesa
from models.receita import Receita

def criar_tabelas():
    Base.metadata.create_all(bind=engine)

def resetar_tabelas():
    print("⚠️  Resetando banco de dados...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("✅ Banco resetado com sucesso.")
