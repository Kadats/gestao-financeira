from models.categoria import Categoria
from models.base import SessionLocal

def adicionar_categoria(nome: str):
    session = SessionLocal()
    nome = nome.strip()
    existente = session.query(Categoria).filter_by(nome=nome).first()
    if existente:
        print(f"⚠️ Categoria '{nome}' já existe.")
        session.close()
        return
    nova = Categoria(nome=nome)
    session.add(nova)
    session.commit()
    print(f"✅ Categoria '{nome}' adicionada com sucesso.")
    session.close()

def remover_categoria(nome: str):
    session = SessionLocal()
    categoria = session.query(Categoria).filter_by(nome=nome).first()
    if not categoria:
        print(f"⚠️ Categoria '{nome}' não encontrada.")
        session.close()
        return
    session.delete(categoria)
    session.commit()
    print(f"✅ Categoria '{nome}' removida com sucesso.")
    session.close()

def listar_categorias():
    session = SessionLocal()
    categorias = session.query(Categoria).all()
    session.close()
    if not categorias:
        print("⚠️ Nenhuma categoria cadastrada.")
    else:
        print("\n📂 Categorias cadastradas:")
        for cat in categorias:
            tipo = "(subcategoria)" if cat.categoria_pai_id else ""
            print(f"- {cat.nome} {tipo}")

def buscar_categoria_por_nome(nome: str):
    session = SessionLocal()
    categoria = session.query(Categoria).filter_by(nome=nome.strip()).first()
    session.close()
    return categoria

def adicionar_subcategoria(nome_sub: str, nome_pai: str):
    session = SessionLocal()
    pai = session.query(Categoria).filter_by(nome=nome_pai.strip()).first()
    if not pai:
        print(f"⚠️ Categoria pai '{nome_pai}' não encontrada.")
        session.close()
        return
    existente = session.query(Categoria).filter_by(nome=nome_sub.strip()).first()
    if existente:
        print(f"⚠️ Subcategoria '{nome_sub}' já existe.")
        session.close()
        return
    nova_sub = Categoria(nome=nome_sub.strip(), categoria_pai_id=pai.id)
    session.add(nova_sub)
    session.commit()
    print(f"✅ Subcategoria '{nome_sub}' adicionada à categoria '{nome_pai}'.")
    session.close()

def remover_subcategoria(nome_sub: str, nome_pai: str):
    session = SessionLocal()
    pai = session.query(Categoria).filter_by(nome=nome_pai.strip()).first()
    if not pai:
        print(f"⚠️ Categoria pai '{nome_pai}' não encontrada.")
        session.close()
        return
    sub = session.query(Categoria).filter_by(nome=nome_sub.strip(), categoria_pai_id=pai.id).first()
    if not sub:
        print(f"⚠️ Subcategoria '{nome_sub}' não encontrada ou não pertence à categoria '{nome_pai}'.")
        session.close()
        return
    session.delete(sub)
    session.commit()
    print(f"✅ Subcategoria '{nome_sub}' removida da categoria '{nome_pai}'.")
    session.close()
