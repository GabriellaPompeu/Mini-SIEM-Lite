# Projeto SIEM Lite - SQL + Python
## Objetivo do projeto
- Construção de uma ferramenta chamada SIEM Lite.
- SIEM significa Security Information and Event Management.
- Também desenvolvi um gerador de logs que simula tráfego normal e diversos ataques (brute force, SQL Injection, path traversal, enumeração de diretórios e acessos administrativos). Assim consigo gerar conjuntos de dados reproduzíveis para validar cada detector do SIEM.

## Execução:
- Rode no terminal: python main.py access.log

## Fluxo do programa:
          access.log
               │
               ▼
         parser.py
               │
               ▼
        Evento Python
               │
               ▼
       database.py
               │
               ▼
          SQLite
               │
               ▼
        detector.py
               │
               ▼
         report.py
               │
               ▼
         Relatório final