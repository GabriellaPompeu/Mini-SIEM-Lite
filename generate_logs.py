import random
from datetime import datetime, timedelta
from pathlib import Path

LOG_FILE = Path('logs') / 'access.log'

METHODS = ['GET', 'POST', 'PUT', 'DELETE']

ENDPOINTS = ["/", "/index.html", "/login", "/logout", "/dashboard", "/products", "/contact", "/about", "/api/users", "/api/orders", "/profile", "/cart"]

STATUS = [200, 200, 200, 200, 200, 201, 204, 301, 302, 400, 401, 403, 404, 500]

PROTOCOLS = ["HTTP/1.0", "HTTP/1.1", "HTTP/2"]

IPS = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30",
    "10.0.0.15",
    "172.16.0.12",
    "203.0.113.8",
    "198.51.100.25",
    "185.199.108.50",
    "91.198.174.192",
    "45.33.32.156"
]

def create_date():
    ano = 2026
    inicio = datetime(ano, 1, 1, 0, 0, 0)
    fim = datetime(ano, 12, 31, 23, 59, 59)

    intervalo = int((fim - inicio).total_seconds())

    data = inicio + timedelta(seconds=random.randint(0, intervalo))

    return f'{data.strftime("%d/%b/%Y:%H:%M:%S")}'

def build_logs(ip, data, metodo, endpoint, protocolo, status, tamanho):
    # 192.168.1.10 - - [26/Jul/2026:20:15:43] "GET /login HTTP/1.1" 200 512
    return f'{ip} - - [{data}] "{metodo} {endpoint} {protocolo}" {status} {tamanho}'

def generate_normal_log():
    ip = random.choice(IPS)
    data = create_date()
    metodo = random.choice(METHODS)
    endpoint = random.choice(ENDPOINTS)
    protocolo = random.choice(PROTOCOLS)
    status = random.choice(STATUS)
    tamanho = random.randint(100, 2600)

    return build_logs(ip, data, metodo, endpoint, protocolo, status, tamanho)

def generate_bruteforce_logs():
    logs = []

    atacante = random.choice(IPS)

    for _ in range(7):
        ip = atacante
        metodo = "POST"
        endpoint = "/login"
        status = '401'
        protocolo = 'HTTP/1.1'
        tamanho = random.randint(250, 800)
        data = create_date()
        logs.append(build_logs(ip, data, metodo, endpoint, protocolo, status, tamanho))

    logs.append(build_logs(ip, data, metodo, endpoint, protocolo, '200', tamanho))

    return logs

def generate_scan_logs():
    ...

def main():
    logs = []

    for _ in range(220):
        logs.append(generate_normal_log())

    logs.extend(generate_bruteforce_logs())

    random.shuffle(logs)

    with open(LOG_FILE, 'w') as arquivo:
        for log in logs:
            arquivo.write(log + '\n')

if __name__ == '__main__':
    main()