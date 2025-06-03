from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.base import SessionLocal
from models.categoria import Categoria
from pydantic import BaseModel

router = APIRouter(prefix="/categorias", tags=["Categorias"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class CategoriaCreate(BaseModel):
    nome: str


@router.get("/")
def listar_categorias(db: Session = Depends(get_db)):
    categorias = db.query(Categoria).all()
    return [{"id": c.id, "nome": c.nome} for c in categorias]


@router.post("/")
def adicionar_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    existente = db.query(Categoria).filter_by(nome=categoria.nome).first()
    if existente:
        raise HTTPException(status_code=400, detail="Categoria já existe.")
    
    nova = Categoria(nome=categoria.nome)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return {"id": nova.id, "nome": nova.nome}


@router.delete("/{categoria_id}")
def remover_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).get(categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada.")
    
    db.delete(categoria)
    db.commit()
    return {"message": "Categoria removida com sucesso."}
