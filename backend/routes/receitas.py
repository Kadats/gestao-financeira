from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.base import SessionLocal
from models.receita import Receita
from models.categoria import Categoria
from pydantic import BaseModel
from datetime import date
from decimal import Decimal

router = APIRouter(prefix="/receitas", tags=["Receitas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ReceitaCreate(BaseModel):
    descricao: str
    valor: Decimal
    data: date
    categoria_nome: str


@router.get("/")
def listar_receitas(db: Session = Depends(get_db)):
    receitas = db.query(Receita).all()
    return [
        {
            "id": r.id,
            "descricao": r.descricao,
            "valor": float(r.valor),
            "data": r.data,
            "categoria": r.categoria.nome if r.categoria else None
        }
        for r in receitas
    ]


@router.post("/")
def adicionar_receita(receita: ReceitaCreate, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter_by(nome=receita.categoria_nome).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada.")
    
    nova = Receita(
        descricao=receita.descricao,
        valor=receita.valor,
        data=receita.data,
        categoria=categoria
    )
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return {"id": nova.id, "descricao": nova.descricao}


@router.delete("/{receita_id}")
def remover_receita(receita_id: int, db: Session = Depends(get_db)):
    receita = db.query(Receita).get(receita_id)
    if not receita:
        raise HTTPException(status_code=404, detail="Receita não encontrada.")
    
    db.delete(receita)
    db.commit()
    return {"message": "Receita removida com sucesso."}
