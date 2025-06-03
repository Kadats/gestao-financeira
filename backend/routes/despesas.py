from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.base import SessionLocal
from models.despesa import Despesa
from models.categoria import Categoria
from pydantic import BaseModel
from datetime import date
from decimal import Decimal

router = APIRouter(prefix="/despesas", tags=["Despesas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DespesaCreate(BaseModel):
    descricao: str
    valor: Decimal
    data: date
    categoria_nome: str


@router.get("/")
def listar_despesas(db: Session = Depends(get_db)):
    despesas = db.query(Despesa).all()
    return [
        {
            "id": d.id,
            "descricao": d.descricao,
            "valor": float(d.valor),
            "data": d.data,
            "categoria": d.categoria.nome if d.categoria else None
        }
        for d in despesas
    ]


@router.post("/")
def adicionar_despesa(despesa: DespesaCreate, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter_by(nome=despesa.categoria_nome).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada.")
    
    nova = Despesa(
        descricao=despesa.descricao,
        valor=despesa.valor,
        data=despesa.data,
        categoria_id=categoria.id
    )
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return {"id": nova.id, "descricao": nova.descricao}


@router.delete("/{despesa_id}")
def remover_despesa(despesa_id: int, db: Session = Depends(get_db)):
    despesa = db.query(Despesa).get(despesa_id)
    if not despesa:
        raise HTTPException(status_code=404, detail="Despesa não encontrada.")
    
    db.delete(despesa)
    db.commit()
    return {"message": "Despesa removida com sucesso."}
