from sqlalchemy.orm import joinedload
from datetime import datetime

from models.base import SessionLocal
from models.receita import Receita
from models.despesa import Despesa

def exibir_saldo():
    session = SessionLocal()
    total_receitas = session.query(Receita).with_entities(Receita.valor).all()
    total_despesas = session.query(Despesa).with_entities(Despesa.valor).all()
    session.close()

    soma_receitas = sum(r.valor for r in total_receitas)
    soma_despesas = sum(d.valor for d in total_despesas)
    saldo = soma_receitas - soma_despesas

    print("\n💰 Saldo Atual:")
    print(f"Receitas: R$ {soma_receitas:.2f}")
    print(f"Despesas: R$ {soma_despesas:.2f}")
    print(f"Saldo: R$ {saldo:.2f}")
    if saldo < 0:
        print("⚠️ Você está no negativo!")
    elif saldo == 0:
        print("🔄 Seu saldo está zerado.")
    else:
        print("✅ Você está no positivo!")


def exibir_movimentacoes():
    session = SessionLocal()
    receitas = session.query(Receita).all()
    despesas = session.query(Despesa).all()
    session.close()

    # Cria uma lista única com todos os registros e tipo
    movimentacoes = [
        {"data": r.data, "tipo": "Receita", "valor": r.valor, "descricao": r.descricao}
        for r in receitas
    ] + [
        {"data": d.data, "tipo": "Despesa", "valor": d.valor, "descricao": d.descricao}
        for d in despesas
    ]

    # Ordena por data
    movimentacoes.sort(key=lambda x: x["data"])

    print("\n🧾 Movimentações financeiras:")
    for m in movimentacoes:
        print(f"{m['data']} | {m['tipo']:<8} | R$ {m['valor']:.2f} | {m['descricao']}")


def gastos_por_categoria():
    session = SessionLocal()
    despesas = session.query(Despesa).options(joinedload(Despesa.categoria)).all()
    session.close()

    gastos_categoria = {}

    for despesa in despesas:
        nome_categoria = despesa.categoria.nome if despesa.categoria else "Sem categoria"
        if nome_categoria not in gastos_categoria:
            gastos_categoria[nome_categoria] = 0
        gastos_categoria[nome_categoria] += despesa.valor

    print("\n📊 Gastos por Categoria:")
    for categoria, total in gastos_categoria.items():
        print(f"- {categoria}: R$ {total:.2f}")


def listar_movimentacoes_por_periodo(data_inicio_str, data_fim_str):
    session = SessionLocal()
    try:
        data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y").date()
        data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y").date()
    except ValueError:
        print("❌ Formato de data inválido. Use DD/MM/AAAA.")
        return

    receitas = session.query(Receita).filter(Receita.data.between(data_inicio, data_fim)).all()
    despesas = session.query(Despesa).filter(Despesa.data.between(data_inicio, data_fim)).all()
    session.close()

    movimentacoes = [
        {"data": r.data, "tipo": "Receita", "valor": r.valor, "descricao": r.descricao}
        for r in receitas
    ] + [
        {"data": d.data, "tipo": "Despesa", "valor": d.valor, "descricao": d.descricao}
        for d in despesas
    ]

    movimentacoes.sort(key=lambda x: x["data"])

    print(f"\n📆 Movimentações de {data_inicio.strftime('%d/%m/%Y')} a {data_fim.strftime('%d/%m/%Y')}:")
    if not movimentacoes:
        print("⚠️ Nenhuma movimentação encontrada nesse período.")
    for m in movimentacoes:
        print(f"{m['data'].strftime('%d/%m/%Y')} | {m['tipo']:<8} | R$ {m['valor']:.2f} | {m['descricao']}")

