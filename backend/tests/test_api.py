from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_criar_categoria():
    response = client.post("/categorias/", json={"nome": "TesteCategoria"})
    assert response.status_code == 200 or response.status_code == 400

def test_criar_receita():
    client.post("/categorias/", json={"nome": "Salário"})
    response = client.post("/receitas/", json={
        "descricao": "Salário Maio",
        "valor": 3000.00,
        "data": "2025-05-01",
        "categoria_nome": "Salário"
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_criar_despesa():
    client.post("/categorias/", json={"nome": "Alimentação"})
    response = client.post("/despesas/", json={
        "descricao": "Compra no mercado",
        "valor": 150.00,
        "data": "2025-05-02",
        "categoria_nome": "Alimentação"
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_receitas():
    response = client.get("/receitas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_despesas():
    response = client.get("/despesas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_categorias():
    response = client.get("/categorias/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_saldo():
    response = client.get("/relatorios/saldo")
    assert response.status_code == 200
    data = response.json()
    assert "receitas" in data
    assert "despesas" in data
    assert "saldo" in data

def test_get_gastos_por_categoria():
    response = client.get("/relatorios/gastos-categoria")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_movimentacoes_por_periodo():
    response = client.get("/relatorios/movimentacoes-periodo", params={
        "inicio": "2025-05-01",
        "fim": "2025-05-10"
    })
    assert response.status_code == 200
    assert isinstance(response.json(), list)
