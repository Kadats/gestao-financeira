from storage import csv_file
from analytics import carregar_dados
from menu import executar_menu
from utils import criar_cabecalho

criar_cabecalho(csv_file)

df = carregar_dados() # Carrega os dados antes de iniciar o menu

if __name__ == "__main__":
    executar_menu(df) # Passa o df para o menu
