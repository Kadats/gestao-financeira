from analytics import (
    total_despesas,
    media_mensal,
    carregar_dados
)
from colorama import Fore, Style
from storage import csv_file, listar_despesas
from utils import adicionar_despesa

def imprimir_menu():
    """Exibe o menu formatado."""
    print(Fore.CYAN + "\n" + "=" * 40)
    print("        GERENCIADOR FINANCEIRO        ")
    print("Bem-vindo ao Sistema de Gestão Financeira Pessoal")
    print("Escolha uma das opções abaixo:")
    print("=" * 40 + Style.RESET_ALL)
    print(Fore.YELLOW + "1 - Adicionar nova despesa")
    print("2 - Exibir todas as despesas")
    print("3 - Analisar despesas (totais e médias)")
    print("0 - Sair" + Style.RESET_ALL)
    print("-" * 40)

def executar_menu(df):
    while True:
        imprimir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao.isdigit():
            opcao = int(opcao)
            df = carregar_dados()  # Carrega os dados atualizados

            if opcao == 1:
                adicionar_despesa(csv_file)
                print(Fore.GREEN + f"\n✅[SUCESSO]: Despesa adicionada com sucesso!" + Style.RESET_ALL)
            elif opcao == 2:
                print(Fore.RED + f"\n📋[INFO]: Aqui estão suas despesas registradas:" + Style.RESET_ALL)
                listar_despesas(csv_file)
            elif opcao == 3:
                print(f"\ninfo: Suas despesas somam: R$ {total_despesas(df):.2f}")
                print(f"\ninfo: A média de gastos nos últimos 30 dias foram de: R$ {media_mensal(df)}")
                print(Fore.BLUE + f"\n📊 Análise concluída." + Style.RESET_ALL)
            elif opcao == 0:
                print(Fore.CYAN + "Obrigado por utilizar nosso sistema! Até mais. 👋" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "erro: Opção inválida! Escolha um número entre 0 e 3." + Style.RESET_ALL)
        else:
            print(Fore.RED + "erro: Entrada inválida! Digite um número." + Style.RESET_ALL)
