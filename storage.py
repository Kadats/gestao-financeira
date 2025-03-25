import csv
import os


ROOT = os.path.join(os.getcwd(), "data") # Diretório onde o CSV será salvo

if not os.path.exists(ROOT):
    os.makedirs(ROOT) # Cria a pasta "data" se ela não existir

csv_file = os.path.join(ROOT, "despesas.csv") # Caminho completo do CSV

# Carrega o arquivo CSV
def carregar_arquivo(csv_file):
    try:
        with open(csv_file, "r", newline="", encoding="utf-8") as arquivo:
            return csv.reader(arquivo)
    except FileNotFoundError:
        print(f"Erro: O arquivo {csv_file} não foi encontrado.")
        return []
    except PermissionError:
        print(f"Erro: Sem permissão para acessar o arquivo {csv_file}.")
        return []

# Adiciona uma nova despesa ao arquivo CSV
def salvar_despesa(csv_file, descricao, categoria, valor, data_formatada):
    with open(csv_file, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([descricao, categoria, valor, data_formatada])

def listar_despesas(csv_file):
    with open(csv_file, "r", newline="", encoding="utf-8") as arquivo:
        for despesa in arquivo:
            print(despesa)
