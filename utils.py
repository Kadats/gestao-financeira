import csv
from storage import csv_file


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
            escritor.writerow(["Descrição", "Categoria", "Valor", "Data"]) # Cabeçalho do CSV
