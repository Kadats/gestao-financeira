from datetime import datetime

def validar_data(data_str):
    """
    Valida uma data no formato dd/mm/aaaa.
    Retorna um objeto datetime.date se for válida, ou None se inválida.
    """
    try:
        return datetime.strptime(data_str, "%d/%m/%Y").date()
    except ValueError:
        print("❌ Data inválida. Use o formato DD/MM/AAAA.")
        return None

def validar_valor(valor_str):
    """
    Tenta converter um valor para float.
    Retorna o valor em float se possível, ou None se inválido.
    """
    try:
        return float(valor_str.replace(',', '.'))
    except ValueError:
        print("❌ Valor inválido. Digite um número.")
        return None

def validar_id(id_str):
    """
    Verifica se o ID é um número inteiro positivo.
    """
    if id_str.isdigit():
        return int(id_str)
    print("❌ ID inválido. Digite um número inteiro positivo.")
    return None

def confirmar_operacao(mensagem):
    """
    Pergunta ao usuário se deseja continuar. Retorna True/False.
    """
    resp = input(f"{mensagem} (s/n): ").strip().lower()
    return resp == 's'
