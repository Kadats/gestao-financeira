from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.base import SessionLocal
from models.receita import Receita
from models.despesa import Despesa
from models.categoria import Categoria
from datetime import date

router = APIRouter(prefix="/relatorios", tags=["Relatórios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/saldo")
def exibir_saldo(db: Session = Depends(get_db)):
    receitas = db.query(Receita).all()
    despesas = db.query(Despesa).all()
    
    total_receitas = sum(r.valor for r in receitas)
    total_despesas = sum(d.valor for d in despesas)
    saldo = total_receitas - total_despesas

    return {
        "receitas": float(total_receitas),
        "despesas": float(total_despesas),
        "saldo": float(saldo)
    }


@router.get("/gastos-categoria")
def gastos_por_categoria(db: Session = Depends(get_db)):
    despesas = db.query(Despesa).all()
    relatorio = {}
    for d in despesas:
        nome_categoria = d.categoria.nome if d.categoria else "Sem categoria"
        relatorio[nome_categoria] = relatorio.get(nome_categoria, 0) + float(d.valor)
    return relatorio


@router.get("/movimentacoes-periodo")
def listar_movimentacoes_por_periodo(inicio: date, fim: date, db: Session = Depends(get_db)):
    receitas = db.query(Receita).filter(Receita.data >= inicio, Receita.data <= fim).all()
    despesas = db.query(Despesa).filter(Despesa.data >= inicio, Despesa.data <= fim).all()
    
    movimentacoes = [
        {
            "data": r.data,
            "tipo": "Receita",
            "descricao": r.descricao,
            "valor": float(r.valor)
        } for r in receitas
    ] + [
        {
            "data": d.data,
            "tipo": "Despesa",
            "descricao": d.descricao,
            "valor": float(d.valor)
        } for d in despesas
    ]

    movimentacoes.sort(key=lambda x: x["data"])
    return movimentacoes
