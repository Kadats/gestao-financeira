from controllers import categorias, despesas, receitas, relatorios
from utils.validacoes import validar_data, validar_valor, confirmar_operacao, validar_id
from utils.mensagens import msg_confirmar_remocao, msg_operacao_cancelada, msg_categoria_nao_encontrada

def menu():
    while True:
        print("\n" + "=" * 30)
        print("==== MENU PRINCIPAL ====")
        print("=" * 30)
        print("1. Menu de Categorias")
        print("2. Menu de Despesas")
        print("3. Menu de Receitas")
        print("4. Menu de Relatórios")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_categorias()
        elif opcao == "2":
            menu_despesas()
        elif opcao == "3":
            menu_receitas()
        elif opcao == "4":
            menu_relatorios()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


def menu_categorias():
    while True:
        print("\n" + "=" * 30)
        print("==== MENU CATEGORIAS ====")
        print("=" * 30)
        print("1. Adicionar Categoria")
        print("2. Remover Categoria")
        print("3. Adicionar Subcategoria")
        print("4. Remover Subcategoria")
        print("5. Listar Categorias")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da categoria: ")
            categorias.adicionar_categoria(nome)

        elif opcao == "2":
            nome = input("Nome da categoria: ")
            if confirmar_operacao(msg_confirmar_remocao("categoria", nome)):
                categorias.remover_categoria(nome)
            else:
                print(msg_operacao_cancelada())

        elif opcao == "3":
            nome_pai = input("Nome da categoria pai: ")
            nome_sub = input("Nome da subcategoria: ")
            categorias.adicionar_subcategoria(nome_sub, nome_pai)
            print(f"Subcategoria '{nome_sub}' adicionada à categoria '{nome_pai}'.")

        elif opcao == "4":
            nome_pai = input("Nome da categoria pai: ")
            nome_sub = input("Nome da subcategoria a remover: ")
            if confirmar_operacao(msg_confirmar_remocao("subcategoria", nome_sub)):
                categorias.remover_subcategoria(nome_sub, nome_pai)
            else:
                print(msg_operacao_cancelada())

        elif opcao == "5":
            categorias.listar_categorias()

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def menu_despesas():
    while True:
        print("\n" + "=" * 30)
        print("==== MENU DESPESAS ====")
        print("=" * 30)
        print("1. Adicionar Despesa")
        print("2. Remover Despesa")
        print("3. Listar Despesas")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição: ")
            
            valor = None
            while valor is None:
                valor_str = input("Valor: ")
                valor = validar_valor(valor_str)

            data = None
            while data is None:
                data_str = input("Data (DD/MM/AAAA): ")
                data = validar_data(data_str)

            categoria = None
            while categoria is None:
                categoria = input("Categoria: ")
                if not categorias.buscar_categoria_por_nome(categoria):
                    print(msg_categoria_nao_encontrada(categoria))
                    resposta = input("Deseja criar uma nova categoria? (s/n): ").strip().lower()
                    if resposta == 's':
                        categorias.adicionar_categoria(categoria)
                        print(f"Categoria '{categoria}' criada.")
                        break
                    else:
                        categoria = None
                        print("Operação cancelada.")
                        continue

            despesas.adicionar_despesa(descricao, valor, data, categoria)
        
        elif opcao == "2":
            id_valido = None
            while id_valido is None:
                id_str = input("ID da despesa: ")
                id_valido = validar_id(id_str)
            if id_valido is not None:
                if confirmar_operacao(msg_confirmar_remocao("despesa", id_valido)):
                    despesas.remover_despesa(id_valido)
                else:
                    print(msg_operacao_cancelada())
        
        elif opcao == "3":
            despesas.listar_despesas()
        
        elif opcao == "0":
            break
        
        else:
            print("Opção inválida.")


def menu_receitas():
    while True:
        print("\n" + "=" * 30)
        print("==== MENU RECEITAS ====")
        print("=" * 30)
        print("1. Adicionar Receita")
        print("2. Remover Receita")
        print("3. Listar Receitas")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição: ")
            
            valor = None
            while valor is None:
                valor_str = input("Valor: ")
                valor = validar_valor(valor_str)
            
            data = None
            while data is None:
                data_str = input("Data (DD/MM/AAAA): ")
                data = validar_data(data_str)

            categoria = input("Categoria: ")
            if not categorias.buscar_categoria_por_nome(categoria):
                print(f"⚠️ Categoria '{categoria}' não encontrada. Deseja criar uma nova? (s/n)")
                resposta = input().strip().lower()
                if resposta == 's':
                    categorias.adicionar_categoria(categoria)
                else:
                    print("Operação cancelada.")
                    continue

            receitas.adicionar_receita(descricao, valor, data, categoria)

        elif opcao == "2":
            id_valido = None
            while id_valido is None:
                id_str = input("ID da receita: ")
                id_valido = validar_id(id_str)
            if id_valido is not None:
                if confirmar_operacao(msg_confirmar_remocao("receita", id_valido)):
                    receitas.remover_receita(id_valido)
                else:
                    print(msg_operacao_cancelada())

        elif opcao == "3":
            receitas.listar_receitas()

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_relatorios():
    while True:
        print("\n" + "=" * 30)
        print("==== MENU RELATÓRIOS ====")
        print("=" * 30)
        print("1. Exibir Saldo")
        print("2. Exibir Movimentações")
        print("3. Gastos por Categoria")
        print("4. Listar Movimentações por Período")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relatorios.exibir_saldo()

        elif opcao == "2":
            relatorios.exibir_movimentacoes()

        elif opcao == "3":
            relatorios.gastos_por_categoria()

        elif opcao == "4":
            data_inicio = None
            while data_inicio is None:
                data_inicio_str = input("Data de início (DD/MM/AAAA): ")
                data_inicio = validar_data(data_inicio_str)

            data_fim = None
            while data_fim is None:
                data_fim_str = input("Data de fim (DD/MM/AAAA): ")
                data_fim = validar_data(data_fim_str)
            
            if data_inicio > data_fim:
                print("⚠️ Data de início não pode ser maior que a data de fim.")
                continue
            relatorios.listar_movimentacoes_por_periodo(data_inicio, data_fim)

        elif opcao == "0":
            break
        
        else:
            print("Opção inválida.")
