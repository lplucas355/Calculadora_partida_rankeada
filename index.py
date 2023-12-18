def calcular_nivel(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif 10 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    mensagem = f"O Herói tem um saldo de {saldo_vitorias} e está no nível de {nivel}"
    return mensagem

# Solicita os valores ao usuário
vitorias = int(input("Informe a quantidade de vitórias: "))
derrotas = int(input("Informe a quantidade de derrotas: "))

# Chama a função e obtém o resultado
resultado = calcular_nivel(vitorias, derrotas)

# Exibe a mensagem de saída
print(resultado)
