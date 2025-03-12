import csv
from datetime import datetime
import os


ROOT = os.path.join(os.getcwd(), "data") # Diretório onde o CSV será salvo

if not os.path.exists(ROOT):
    os.makedirs(ROOT) # Cria a pasta "data" se ela não existir

csv_file = os.path.join(ROOT, "despesas.csv") # Caminho completo do CSV

def verificar_cabecalho(csv_file):
    try:
        with open(csv_file, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            primeira_linha = next(leitor, None) # Lê a primeira linha (se ela existir)
            return primeira_linha is not None # Retorna True se a primeira linha tiver cabeçalho
    except FileNotFoundError:
        return False # Se o arquivo não existir, significa que o cabeçalho ainda não existe
    
def criar_cabecalho(csv_file):
    if not verificar_cabecalho(csv_file): # Só cria o cabeçalho se ele não existir
        with open(csv_file, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Descrição", "Valor", "Data"]) # Cabeçalho do CSV

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
