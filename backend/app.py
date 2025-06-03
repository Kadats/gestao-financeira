from utils.menu import menu
from database.setup import criar_tabelas

# Função principal para criar tabelas e iniciar o menu
def main():
    # Cria as tabelas no banco de dados
    criar_tabelas()

    # Inicia o menu
    menu()

if __name__ == "__main__":
    menu()
