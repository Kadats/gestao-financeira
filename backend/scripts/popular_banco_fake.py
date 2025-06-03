import random
from datetime import datetime, timedelta
from decimal import Decimal
from faker import Faker

from models.base import SessionLocal
from models.categoria import Categoria
from models.receita import Receita
from models.despesa import Despesa

fake = Faker("pt_BR")
session = SessionLocal()

# Limpa dados anteriores (opcional)
session.query(Receita).delete()
session.query(Despesa).delete()
session.query(Categoria).delete()
session.commit()

# Cria categorias e subcategorias
nomes_categorias = {
    "Salário": [],
    "Freelancer": [],
    "Lazer": ["Cinema", "Viagem"],
    "Contas": ["Luz", "Internet", "Água"],
    "Alimentação": ["Mercado", "Restaurante"],
}

categorias = {}
for pai, subs in nomes_categorias.items():
    cat_pai = Categoria(nome=pai)
    session.add(cat_pai)
    session.commit()
    categorias[pai] = cat_pai
    for sub in subs:
        cat_sub = Categoria(nome=sub, categoria_pai_id=cat_pai.id)
        session.add(cat_sub)
        session.commit()
        categorias[sub] = cat_sub

# Função auxiliar para gerar datas aleatórias no mês atual
def data_aleatoria():
    inicio = datetime(datetime.today().year, datetime.today().month, 1)
    fim = inicio + timedelta(days=30)
    return fake.date_between(start_date=inicio, end_date=fim)

# Gera receitas aleatórias
for _ in range(10):
    categoria = random.choice(["Salário", "Freelancer"])
    receita = Receita(
        descricao=fake.sentence(nb_words=3),
        valor=Decimal(random.uniform(1000, 5000)).quantize(Decimal("0.01")),
        data=data_aleatoria(),
        categoria_id=categorias[categoria].id,
    )
    session.add(receita)

# Gera despesas aleatórias
for _ in range(20):
    categoria = random.choice(list(categorias.keys()))
    despesa = Despesa(
        descricao=fake.sentence(nb_words=4),
        valor=Decimal(random.uniform(20, 500)).quantize(Decimal("0.01")),
        data=data_aleatoria(),
        categoria_id=categorias[categoria].id,
    )
    session.add(despesa)

session.commit()
session.close()

print("✅ Banco populado com dados aleatórios de teste.")
