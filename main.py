from pathlib import Path
from database import create_table, insert_log, clear_logs
from parser import parse_log_line
from detector import top_ip, brute_force
from report import generate_report

LOGS_PATH = Path("logs") / "access.log"

def main():
    create_table()
    clear_logs()
    print("Inicializando SIEM...")

    count = 0

    with open(LOGS_PATH) as arquivo:
        for line in arquivo:
            event = parse_log_line(line.strip())

            if event is not None:
                insert_log(event)
                count += 1

    print(f'{count} eventos importados')

    generate_report()
    

if __name__ == "__main__":
    main()