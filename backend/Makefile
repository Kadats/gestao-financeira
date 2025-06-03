run:
	uvicorn main:app --reload

test:
	PYTHONPATH=. pytest -v

test-api:
	PYTHONPATH=. pytest -v tests/test_api.py

freeze:
	pip freeze > requirements.txt

reset-db:
	python -c "from database.setup import resetar_tabelas; resetar_tabelas()"

popular-db:
	PYTHONPATH=. python scripts/popular_banco_fake.py

