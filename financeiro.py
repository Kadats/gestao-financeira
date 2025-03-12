import csv
from decimal import Decimal
from utils import csv_file, formatar_data, validar_data


def adicionar_despesas(csv_file, descricao, valor, data):
    with open(csv_file, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([descricao, valor, data])  # Adiciona uma nova despesa
    
    controle = True
    while controle:
        descricao = input("Descrição da despesa: ")
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
