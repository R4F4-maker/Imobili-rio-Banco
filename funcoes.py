# funcoes.py

import random

def jogar_dado():

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    return dado1, dado2

def decidir_compra(tipo, dinheiro, preco):

    if tipo == "louco":

        return dinheiro >= preco

    elif tipo == "investidor":

        return preco >= 150

    elif tipo == "aleatorio":

        return random.choice([True, False])

    elif tipo == "equilibrado":

        return dinheiro - preco >= 150

    return False

def mostrar_placar(
    nome,
    dinheiro,
    bots,
    dinheiro_bots,
    propriedades
):
    print("\n===== PLACAR =====")

    print(f"{nome}: ${dinheiro}")

    falidos = []

    for j in range(len(bots)):

        if dinheiro_bots[j] <= 0:

            falidos.append(bots[j])

            for nome_prop in propriedades:

                if propriedades[nome_prop]["dono"] == bots[j]:
                    propriedades[nome_prop]["dono"] = None

            dinheiro_bots[j] = -999999

        else:

            print(
                f"{bots[j]}: "
                f"${dinheiro_bots[j]}"
            )

    for bot in falidos:
        print(f"{bot}: FALIU!")

    print("==================")

def carta_sorte(dinheiro, cartas_sorte):
    texto, valor = random.choice(cartas_sorte)

    print("\nCARTA SORTE:")
    print(texto)

    dinheiro += valor

    print(f"Novo saldo: ${dinheiro}")

    return dinheiro

def carta_cofre(dinheiro, cartas_cofre):
    texto, valor = random.choice(cartas_cofre)

    print("\nCARTA COFRE:")
    print(texto)

    dinheiro += valor

    print(f"Novo saldo: ${dinheiro}")

    return dinheiro

def cobrar_taxa(dinheiro, valor, nome_taxa):
    dinheiro -= valor

    print(
        f"\nVocê pagou "
        f"${valor} de {nome_taxa}!"
    )

    print(
        f"Novo saldo: "
        f"${dinheiro}"
    )

    return dinheiro

def tentativa_prisao(
    rodadas_preso,
    tentativas_prisao,
    dinheiro
):

    tentativas_prisao += 1

    print("\nVocê está preso!")

    print(
        f"Tentativa "
        f"{tentativas_prisao} de 3"
    )

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    print(
        f"Você tirou "
        f"{dado1} e {dado2}"
    )

    if dado1 == dado2:

        print(
            "\nDADOS IGUAIS!"
        )

        print(
            "Você saiu da prisão!"
        )

        rodadas_preso = 0
        tentativas_prisao = 0

    else:

        print(
            "Você continua preso."
        )

        if tentativas_prisao >= 3:

            dinheiro -= 50

            print(
                "\nVocê pagou $50 de fiança."
            )

            print(
                "Você saiu da prisão."
            )

            rodadas_preso = 0
            tentativas_prisao = 0

    return (
        rodadas_preso,
        tentativas_prisao,
        dinheiro
    )