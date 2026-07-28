from detector import top_ip, brute_force, top_endpoints

def generate_report():
    print('=' * 40)
    print('           SIEM LITE REPORT')
    print('=' * 40)
    print()

    resultado = top_ip()

    if resultado:
        ip, total = resultado
        print(f'Top IP: {ip} - {total} acessos\n')

    ataques = brute_force()

    if ataques:
        print('Brute Force Detectado')
        for ip, tentativas in ataques:
            print(f'{ip:<20} {tentativas} tentativas')
    else:
        print('Nenhum brute force detectado')

    resultado = top_endpoints()

    if resultado:
        print('\nTop Endpoints:')
        for endpoint, total in resultado:
            print(f'{endpoint:<20} {total} acessos')

