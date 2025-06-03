from models.base import engine, Base, SessionLocal
from models import Receita, Despesa, Categoria, Base
from datetime import date

def init_db():
    Base.metadata.create_all(bind=engine)

def main():
    # Inicializa o banco de dados (cria tabelas se não existirem)
    init_db()

    # Cria uma sessão para interagir com o banco
    db = SessionLocal()

    # Criando Categorias de exemplo
    moradia = Categoria(nome="Moradia")
    lazer = Categoria(nome="Lazer")
    estudo = Categoria(nome="Estudo")
    investimentos = Categoria(nome="Investimentos")

    db.add_all([moradia, lazer, estudo, investimentos])
    db.commit()

    # Criando Subcategorias de exemplo para Investimentos
    curto_prazo = Categoria(nome="Curto Prazo", categoria_pai_id=investimentos.id)
    medio_prazo = Categoria(nome="Médio Prazo", categoria_pai_id=investimentos.id)
    longo_prazo = Categoria(nome="Longo Prazo", categoria_pai_id=investimentos.id)

    db.add_all([curto_prazo, medio_prazo, longo_prazo])
    db.commit()

    # Inserindo uma Receita de exemplo
    receita_salario = Receita(
        descricao="Salário de Abril",
        valor=5000.00,
        data=date.today()
    )

    db.add(receita_salario)
    db.commit()

    # Inserindo uma Despesa de exemplo
    despesa_aluguel = Despesa(
        descricao="Aluguel de Abril",
        valor=1500.00,
        data=date.today(),
        categoria_id=moradia.id
    )

    db.add(despesa_aluguel)
    db.commit()

    # Fecha a sessão
    db.close()


def resetar_banco():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("✅ Banco resetado com sucesso!")

