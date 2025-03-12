import csv
from decimal import Decimal
import os


ROOT = os.path.join(os.getcwd(), "data") # Diretório onde o CSV será salvo

if not os.path.exists(ROOT):
    os.makedirs(ROOT) # Cria a pasta "data" se ela não existir

csv_file = os.path.join(ROOT, "despesas.csv") # Caminho completo do CSV

def formatar_data(data):
    # Formata a entrada para DD/MM/AAAA se o usuário digitar apenas números
    if len(data) == 8 and data.isdigit(): # Verifica se são exatamente 8 dígitos
        return f"{data[:2]}/{data[2:4]}/{data[4:]}" # Adiciona as barras autamaticamente
    return data # Se não for 8 números, retorna como está

def validar_data(data):
    try:
        # Tenta converter a entrada para o formato padrão (usuário digita DD/MM/AAAA)
        data_formatada = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
        return data_formatada # Retorna a data formatada como YYYY-MM-DD
    except ValueError:
        print("Formato de data inválido. Use DD/MM/AAAA.")
        return None # Retorna None para indicar erro


def adicionar_despesas(csv_file, descricao, categoria, valor, data):
    with open(csv_file, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([descricao, categoria, valor, data])  # Adiciona uma nova despesa
    
    controle = True
    while controle:
        descricao = input("Descrição da despesa: ")
        categoria = input("Categoria: ")
        valor = Decimal(input("Valor: "))
        while True:
            data = input("Data (DD/MM/AAAA): ")
            data = formatar_data(data)
            data_formatada = validar_data(data)
            if data_formatada:
                break

        adicionar_despesas(csv_file, descricao, valor, data)

        controle = input("Deseja adicionar outra despesa? (s/n) ").lower() == "s"

    print("\nDespesas registradas com sucesso!")

def listar_despesas(csv_file):
    with open(csv_file, "r", newline="", encoding="utf-8") as arquivo:
        for despesa in arquivo:
            print(despesa)
