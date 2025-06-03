from models.receita import Receita
from models.base import SessionLocal
from datetime import datetime
from controllers.categorias import buscar_categoria_por_nome

# Adiciona uma receita
def adicionar_receita(descricao, valor, data, nome_categoria):
    session = SessionLocal()
    valor = valor.replace(',', '.')
    data = datetime.strptime(data, "%d/%m/%Y").date()
    categoria = buscar_categoria_por_nome(nome_categoria)
    if not categoria:
        print("⚠️ Categoria não encontrada.")
        session.close()
        return
    nova = Receita(descricao=descricao, valor=valor, data=data, categoria_id=categoria.id)
    session.add(nova)
    session.commit()
    print("✅ Receita adicionada com sucesso.")
    session.close()

# Remove uma receita pelo ID
def remover_receita(id_receita):
    session = SessionLocal()
    receita = session.get(Receita, id_receita)
    if not receita:
        print("⚠️ Receita não encontrada.")
        session.close()
        return

    session.delete(receita)
    session.commit()
    print("✅ Receita removida com sucesso.")
    session.close()

# Lista todas as receitas
def listar_receitas():
    session = SessionLocal()
    receitas = session.query(Receita).all()
    session.close()

    if not receitas:
        print("⚠️ Nenhuma receita cadastrada.")
    else:
        print("\n📈 Receitas cadastradas:")
        for r in receitas:
            print(f"- {r.data} | R$ {r.valor:.2f} | {r.descricao} | Categoria ID: {r.categoria_id}")


def listar_receitas_json():
    session = SessionLocal()
    lista = session.query(Receita).all()
    session.close()
    return [
        {
            "id": receita.id,
            "descricao": receita.descricao,
            "valor": float(receita.valor),
            "data": receita.data.strftime("%d/%m/%Y"),
            "categoria_id": receita.categoria_id
        }
        for receita in lista
    ]
