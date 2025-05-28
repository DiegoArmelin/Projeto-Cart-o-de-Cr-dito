# Aplicação simples para identificar a bandeira de um cartão de crédito pelo número

def identificar_bandeira(numero_cartao):
    """
    Identifica a bandeira do cartão de crédito com base no número informado.
    Parâmetro:
        numero_cartao (str): Número do cartão de crédito como string
    Retorna:
        str: Nome da bandeira ou 'Desconhecida'
    """

    # Remove espaços e traços do número do cartão
    numero_cartao = numero_cartao.replace(' ', '').replace('-', '')

    # Verifica se o número contém apenas dígitos
    if not numero_cartao.isdigit():
        return 'Número inválido'

    # Visa: começa com 4, 13 ou 16 dígitos
    if numero_cartao.startswith('4') and len(numero_cartao) in [13, 16, 19]:
        return 'Visa'

    # MasterCard: começa com 51-55 ou 2221-2720, 16 dígitos
    dois_digitos = int(numero_cartao[:2])
    quatro_digitos = int(numero_cartao[:4])
    seis_digitos = int(numero_cartao[:6])
    if len(numero_cartao) == 16:
        if 51 <= dois_digitos <= 55:
            return 'MasterCard'
        if 2221 <= quatro_digitos <= 2720:
            return 'MasterCard'

    # American Express: começa com 34 ou 37, 15 dígitos
    if numero_cartao.startswith(('34', '37')) and len(numero_cartao) == 15:
        return 'American Express'

    # Elo: vários intervalos, exemplo comum começa com 636368, 438935, 504175, 451416, 636297, 5067, 4576, 4011
    if numero_cartao.startswith(('636368', '438935', '504175', '451416', '636297', '5067', '4576', '4011')):
        return 'Elo'

    # Hipercard: começa com 606282 ou 3841, 16 dígitos
    if numero_cartao.startswith(('606282', '3841')) and len(numero_cartao) == 16:
        return 'Hipercard'

    # Diners Club: começa com 300-305, 36, 38, 39, 14 dígitos
    if len(numero_cartao) == 14:
        if 300 <= int(numero_cartao[:3]) <= 305 or numero_cartao.startswith(('36', '38', '39')):
            return 'Diners Club'

    # Discover: começa com 6011, 622126-622925, 644-649, 65, 16 dígitos
    if len(numero_cartao) == 16:
        if numero_cartao.startswith('6011') or numero_cartao.startswith('65'):
            return 'Discover'
        if 644 <= int(numero_cartao[:3]) <= 649:
            return 'Discover'
        if 622126 <= int(numero_cartao[:6]) <= 622925:
            return 'Discover'

    # Caso não identifique a bandeira
    return 'Desconhecida'


# Exemplo de uso
if __name__ == "__main__":
    numero = input("Digite o número do cartão de crédito: ")
    bandeira = identificar_bandeira(numero)
    print(f"Bandeira identificada: {bandeira}")
