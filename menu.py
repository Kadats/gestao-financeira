from analytics import (
    total_despesas,
    maior_despesa,
    menor_despesa,
    media_mensal,
    carregar_dados
)
from colorama import Fore, Style

def imprimir_menu():
    """Exibe o menu formatado."""
    print(Fore.CYAN + "\n" + "=" * 40)
    print("        GERENCIADOR FINANCEIRO        ")
    print("=" * 40 + Style.RESET_ALL)
    print(Fore.YELLOW + "1 - Mostrar total de despesas")
    print("2 - Mostrar maior despesa")
    print("3 - Mostrar menor despesa")
    print("4 - Mostrar média mensal")
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
                print(Fore.GREEN + f"\n🔹 Total de despesas: R$ {total_despesas(df):.2f}" + Style.RESET_ALL)
            elif opcao == 2:
                print(Fore.RED + f"\n🔺 Maior despesa: R$ {maior_despesa(df):.2f}" + Style.RESET_ALL)
            elif opcao == 3:
                print(Fore.BLUE + f"\n🔻 Menor despesa: R$ {menor_despesa(df):.2f}" + Style.RESET_ALL)
            elif opcao == 4:
                print(Fore.MAGENTA + "\n📊 Média de gastos mensais:" + Style.RESET_ALL)
                print(media_mensal(df))
            elif opcao == 0:
                print(Fore.CYAN + "Saindo do programa... Até mais! 👋" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Opção inválida! Escolha um número entre 0 e 4." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Entrada inválida! Digite um número." + Style.RESET_ALL)
