## Projeto: Aplicação de Gestão Financeira Pessoal

### Objetivo Geral
Desenvolver uma aplicação de gestão financeira pessoal que registre receitas e despesas, exibindo tabelas e gráficos para análise da distribuição do dinheiro. O foco é substituir uma planilha tradicional, criando um sistema com maior automação e potencial de expansão.

### Status Atual

- **Leitura e Escrita de Dados**: Implementada com arquivos CSV usando `pandas`.
- **Funções Básicas**: Inclusão de despesas e receitas, carregamento e salvamento de dados.
- **Análise de Dados**: Média mensal, somatório dos últimos 30 dias e agrupamento por categorias.
- **Estrutura Modularizada**: Separação do código em módulos como `main.py`, `analytics.py`, `utils.py`, `menu.py`.
- **Controle de Tipos**: Utilização de `Decimal` para precisão nos valores monetários.
- **Criação de Categorias**: Sistema permite inclusão de categorias personalizadas.
- **Integração com GitHub**: Projeto versionado com Git, hospedado no repositório [[link](https://github.com/Kadats/gestao-financeira)].
- **Documentação Inicial**: README criado explicando o projeto, requisitos e instruções de execução.

### Próximos Passos (MVP)

1. **Validação de Entradas**
   - Garantir formatos corretos para datas e valores.
2. **Refino da Interface no Terminal**
   - Melhorar clareza e usabilidade do menu.
3. **Exportação de Relatórios**
   - Geração de relatórios financeiros em CSV ou PDF.
4. **Testes Unitários**
   - Implementação de testes básicos para garantir robustez.
5. **Preparação para HUD futura**
   - Código limpo e desacoplado para facilitar integração com uma interface gráfica futura.

### Visão de Longo Prazo

- **Interface Gráfica (HUD)**: Planejada para substituir o terminal no futuro.
- **Multi-Plataforma (Web e Mobile)**: Potencial expansão para diferentes plataformas, começando com web.
- **Integração com Blockchain**: Embora não para registro de despesas, o hub pretende propagar conceitos ligados à blockchain e criptomoedas.

---

### Objetivo Pessoal do Usuário
Aprender programação de forma prática, com foco em desenvolvimento de projetos reais, visando futura atuação no mercado de tecnologia. Todo o processo tem caráter educativo e exploratório, buscando não só funcionalidade mas também boas práticas.

### Tecnologias Utilizadas

- **Python 3**
- **pandas**
- **decimal**
- **Git/GitHub**

### Organização Atual do Repositório

- `main.py`: Ponto de entrada do programa.
- `menu.py`: Gerenciamento do menu e interação do usuário.
- `analytics.py`: Funções de análise de dados.
- `utils.py`: Funções auxiliares (formatação, validações, etc.).
- `README.md`: Documentação inicial.

---

**Observação**: Toda evolução do projeto está alinhada com o objetivo primário de aprendizado, sendo feita sempre com explicações detalhadas e acompanhamento próximo.

