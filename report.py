from detector import top_ip, brute_force

def generate_report():
    print('=' * 40)
    print('         SIEM LITE REPORT')
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
            print(f'{ip} - {tentativas} tentativas')
    else:
        print('Nenhum brute force detectado')

