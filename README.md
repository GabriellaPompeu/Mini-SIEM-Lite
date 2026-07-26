# Projeto SIEM Lite - SQL + Python
## Objetivo do projeto
- Construção de uma ferramenta chamada SIEM Lite.
- SIEM significa Security Information and Event Management.

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