from fastapi import FastAPI

from routes import categorias, receitas, despesas, relatorios

app = FastAPI(tittle="Gestão Financeira API")

# Incluir rotas
app.include_router(categorias.router)
app.include_router(receitas.router)
app.include_router(despesas.router)
app.include_router(relatorios.router)

@app.get("/")
def raiz():
    return {"message": "API de Gestão Financeira está no ar!"}
