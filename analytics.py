import pandas as pd
from storage import csv_file


def carregar_dados():
    """Carrega os dados do CSV para um DataFrame do pandas"""
    df = pd.read_csv(csv_file, parse_dates=["Data"]) # Carrega o CSV normalmente
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce") # Converte valores para float, ignorando inválidos
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y") # Converte a coluna Data para datetime
    df.dropna(subset=["Valor"], inplace=True) # Remove linhas onde a conversão falhou
    return df

def total_despesas(df):
    return df["Valor"].sum()

def maior_despesa(df):
    return df["Valor"].max()

def menor_despesa(df):
    return df["Valor"].min()

def media_mensal(df):
    df["Ano-Mês"] = df["Data"].dt.to_period("M")
    return df.groupby("Ano-Mês")["Valor"].mean()
