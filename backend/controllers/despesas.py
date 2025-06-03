from models.despesa import Despesa
from models.base import SessionLocal
from controllers.categorias import buscar_categoria_por_nome

from datetime import datetime
from decimal import Decimal

def adicionar_despesa(descricao, valor, data_str, nome_categoria):
    session = SessionLocal()
    data = datetime.strptime(data_str, "%d/%m/%Y").date()
    valor = Decimal(valor.replace(',', '.'))
    categoria = buscar_categoria_por_nome(nome_categoria)
    if not categoria:
        print("⚠️ Categoria não encontrada.")
        session.close()
        return
    nova = Despesa(descricao=descricao, valor=valor, data=data, categoria_id=categoria.id)
    session.add(nova)
    session.commit()
    print("✅ Despesa adicionada com sucesso.")
    session.close()

def remover_despesa(id_despesa):
    session = SessionLocal()
    despesa = session.get(Despesa, id_despesa)
    if not despesa:
        print("⚠️ Despesa não encontrada.")
        session.close()
        return
    session.delete(despesa)
    session.commit()
    print("✅ Despesa removida com sucesso.")
    session.close()

def listar_despesas():
    session = SessionLocal()
    despesas = session.query(Despesa).all()
    session.close()
    if not despesas:
        print("⚠️ Nenhuma despesa cadastrada.")
    else:
        print("\n📉 Despesas cadastradas:")
        for d in despesas:
            print(f"- {d.data} | R$ {d.valor:.2f} | {d.descricao} | Categoria ID: {d.categoria_id}")


def listar_despesas_json():
    session = SessionLocal()
    lista = session.query(Despesa).all()
    session.close()
    return [
        {
            "id": d.id,
            "descricao": d.descricao,
            "valor": float(d.valor),
            "data": d.data.strftime("%d/%m/%Y"),
            "categoria_id": d.categoria_id
        }
        for d in lista
    ]
