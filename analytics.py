from decimal import Decimal
import pandas as pd
from storage import csv_file


def carregar_dados():
    """Carrega os dados do CSV para um DataFrame do pandas"""
    df = pd.read_csv(csv_file, parse_dates=["Data"]) # Carrega o CSV normalmente
    df["Valor"] = df["Valor"].apply(lambda x: Decimal(x))
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y") # Converte a coluna Data para datetime
    df.dropna(subset=["Valor"], inplace=True) # Remove linhas onde a conversão falhou
    return df

def relatorio_por_categoria(df):
    if df.empty:
        print("\n🚨 Nenhuma despesa registrada ainda!\n")
        return
    
    gastos_por_categoria = df.groupby("Categoria")["Valor"].sum()

    print("\n📊 Relatório de despesas por categoria:\n")
    for categoria, valor in gastos_por_categoria.items():
        print(f"🛒 {categoria}: R$ {valor:.2f}")

    print("\n")

# Calcula a média dos valores e previne divisão por zero
def calcular_media(df):
    try:
        return df["Valor"].mean()
    except ZeroDivisionError:
        print("Erro: Não é possível calcular a média de uma lista vazia.")
        return None

def total_despesas(df):
    return df["Valor"].sum()

def maior_despesa(df):
    return df["Valor"].max()

def menor_despesa(df):
    return df["Valor"].min()

def media_mensal(df):
    df["Ano-Mês"] = df["Data"].dt.to_period("M")
    return df.groupby("Ano-Mês")["Valor"].mean()
