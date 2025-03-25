import csv
import datetime
from decimal import Decimal, InvalidOperation
from storage import salvar_despesa, csv_file

# Verifica se o cabeçalho já existe no arquivo CSV
def verificar_cabecalho(csv_file):
    try:
        with open(csv_file, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            primeira_linha = next(leitor, None) # Lê a primeira linha (se ela existir)
            return primeira_linha is not None # Retorna True se a primeira linha tiver cabeçalho
    except FileNotFoundError:
        return False # Se o arquivo não existir, significa que o cabeçalho ainda não existe

# Cria o cabeçalho do arquivo CSV    
def criar_cabecalho(csv_file):
    if not verificar_cabecalho(csv_file): # Só cria o cabeçalho se ele não existir
        with open(csv_file, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Descrição", "Categoria", "Valor", "Data"]) # Cabeçalho do CSV

# Melhora mensagens de erro e sucesso
def exibir_mensagem(tipo, mensagem):
    simbolos = {"erro": "❌", "sucesso": "✅", "aviso": "⚠️"}
    print(f"{simbolos.get(tipo, 'ℹ️')} {mensagem}")

# Verifica se a categoria já existe na primeira linha do arquivo, se não existir, cria uma nova
def verificar_categoria(categoria): 
    with open(csv_file, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        linhas = list(leitor)
    
    cabecalho = linhas[0] if linhas else ["Descrição", "Categoria", "Valor", "Data"]
    
    if categoria not in cabecalho:
        cabecalho.append(categoria)
        linhas[0] = cabecalho
        
        with open(csv_file, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(linhas)
    
    return categoria in cabecalho

# Valida a data e retorna no formato YYYY-MM-DD
def validar_data(data):
    try:
        data_formatada = datetime.datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
        
        if data_formatada > datetime.datetime.now().strftime("%Y-%m-%d"):
            exibir_mensagem("erro: Data futura inválida.")
            return None

        return data_formatada
    except ValueError:
        return None

# Validação de valores monetários
def validar_valor(valor):
    try:
        return valor > 0
    except InvalidOperation:
        print("erro: Valor inválido. Use apenas números.")
        return False

# Converte valores para Decimal
def converter_valor(valor):
    try:
        return Decimal(valor)
    except InvalidOperation:
        print("erro: Valor inválido. Use apenas números.")
        return None

# Validação de categorias
categorias = {"Alimentação", "Transporte", "Moradia", "Educação", "Saúde", "Lazer", "Investimento"}
def validar_categoria(categoria):
    return categoria in categorias

# Formulário para adicionar despesas    
def adicionar_despesa(csv_file):
    while True:
        data = input("Informe a data da despesa (DD/MM/AAAA): ")
        if not validar_data(data):
            exibir_mensagem("erro", "Formato de data inválido. Tente novamente.")
            continue

        valor = input("Informe o valor da despesa: ")
        valor = valor.replace(",", ".") # Substitui vírgula por ponto para aceitar valores decimais
        valor = converter_valor(valor)
        if not validar_valor(valor):
            exibir_mensagem("erro", "Valor inválido. Use apenas números positivos.")
            continue

        categoria = input("Informe a categoria: ")
        if not validar_categoria(categoria):
            exibir_mensagem("aviso", "Categoria não cadastrada. Deseja adicionar? (S/N)")
            opcao = input().strip().upper()
            if opcao == "S":
                categorias.add(categoria)
            else:
                continue
            
        descricao = input("Informe a descrição: ")

        salvar_despesa(csv_file, descricao, categoria, valor, data)
        
        # Interrompe o loop caso o usuário digite algo diferente de "S"
        if input("Deseja adicionar mais despesas? (S/N): ").strip().upper() != "S":
            break
        exibir_mensagem("sucesso", "Despesa adicionada com sucesso!")

