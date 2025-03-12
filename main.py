from utils import csv_file, criar_cabecalho
from analytics import carregar_dados
from menu import executar_menu

criar_cabecalho(csv_file) # Garante que o cabeçalho seja criado

df = carregar_dados() # Carrega os dados antes de iniciar o menu

if __name__ == "__main__":
    executar_menu(df) # Passa o df para o menu
