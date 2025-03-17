
# Gestão Financeira Pessoal

Uma aplicação simples de gestão financeira pessoal desenvolvida em Python.  
Permite o registro de despesas com categorias, análise dos gastos mensais e médias, exibindo os resultados diretamente no terminal.

## Funcionalidades

- Registro de despesas com data, valor e categoria.
- Análise total das despesas.
- Média mensal de gastos.
- Filtragem de despesas por categoria.
- Interface de menu no terminal.
  
## Estrutura do Projeto

```
gestao-financeira/
├── analytics.py        # Funções de análise dos dados financeiros
├── menu.py             # Menu principal para interação com o usuário
├── utils.py            # Funções auxiliares (validação, formatação, etc.)
├── main.py             # Arquivo principal para iniciar o programa
├── dados.csv           # Arquivo CSV onde as despesas são armazenadas
└── README.md           # Documentação do projeto
```

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/Kadats/gestao-financeira.git
```

2. Navegue até o diretório:
```bash
cd gestao-financeira
```

3. Execute o programa:
```bash
python main.py
```

## Requisitos

- Python 3.11 ou superior
- Bibliotecas:
  - `pandas`
  - `colorama`
  
Instale as dependências:
```bash
pip install pandas colorama
```

## Próximos Passos

- Desenvolver uma interface gráfica (HUD) para substituir o terminal.
- Adicionar autenticação de usuários.
- Exportação de relatórios financeiros.
- Integração com web (HTML, CSS, JS).
- Planejamento futuro para integração com Blockchain.

---

**Licença:** Este projeto é livre para uso pessoal e educacional.
