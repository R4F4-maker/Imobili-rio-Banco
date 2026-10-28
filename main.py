import random

from funcoes import (
    jogar_dado,
    mostrar_placar,
    carta_sorte,
    carta_cofre,
    cobrar_taxa,
    decidir_compra,
    tentativa_prisao
)

nomes_disponiveis = [
    "Lucas", "Gabriel", "Pedro", "Miguel", "Arthur",
    "Ana", "Maria", "Julia", "Beatriz", "Larissa",
    "Camila", "Fernanda", "Amanda", "Isabela", "Helena",
    "Rodrigo", "Victor", "Eduardo", "Alan", "Diego",
    "Bruno", "Rafael", "Matheus", "Gustavo", "Felipe",
    "Clara", "Manuela", "Valentina", "Alice", "Laura",
    "Sophia", "Yasmin", "Lívia", "Bianca", "Melissa",
    "Paulo", "Carlos", "Ricardo", "Marcelo", "André",
    "Thiago", "Daniel", "Caio", "Igor", "Murilo",
    "Nicolas", "Samuel", "Benjamin", "Lorenzo", "Enzo"
]

bots = random.sample(nomes_disponiveis, 4)

tipos_disponiveis = [
    "louco",
    "investidor",
    "aleatorio",
    "equilibrado"
]

tipos_bots = random.choices(
    tipos_disponiveis,
    k=4
)

nome = input("Digite seu nome: ")

if nome == "":
    nome = "Jogador"

#dinheiro = 1500
dinheiro = 500

posicao = 0
rodadas_preso = 2
tentativas_prisao = 0

print(f"Jogador: {nome}")
print(f"Dinheiro: ${dinheiro}")
print(f"Posição: {posicao}")

posicoes_bots = [0, 0, 0, 0]
preso_bots = [0, 0, 0, 0]
dinheiro_bots = [1500, 1500, 1500, 1500]
#dinheiro_bots = [500, 500, 500, 500]

print("\nBots na partida:")

for i in range(len(bots)):

    print(
        f"{bots[i]} "
        f"({tipos_bots[i]})"
    )
tabuleiro = [
    "Partida",                    # 0
    "Avenida Mediterranea",       # 1
    "Cofre",                      # 2
    "Avenida Baltica",            # 3
    "Imposto de Renda",           # 4
    "Ferrovia Reading",           # 5
    "Avenida Oriental",           # 6
    "Sorte",                      # 7
    "Avenida Vermont",            # 8
    "Avenida Connecticut",        # 9
    "Prisao",                     # 10
    "Praca St. Charles",          # 11
    "Companhia Eletrica",         # 12
    "Avenida dos Estados",        # 13
    "Avenida Virginia",           # 14
    "Ferrovia Pennsylvania",      # 15
    "Praca St. James",            # 16
    "Cofre",                      # 17
    "Avenida Tennessee",          # 18
    "Avenida Nova York",          # 19
    "Estacionamento Livre",       # 20
    "Avenida Kentucky",           # 21
    "Sorte",                      # 22
    "Avenida Indiana",            # 23
    "Avenida Illinois",           # 24
    "Ferrovia B&O",               # 25
    "Avenida Atlantica",          # 26
    "Avenida Ventnor",            # 27
    "Companhia de Agua",          # 28
    "Jardins Marvin",             # 29
    "Vá para a Prisao",           # 30
    "Avenida Pacifica",           # 31
    "Avenida Carolina do Norte",  # 32
    "Cofre",                      # 33
    "Avenida Pennsylvania",       # 34
    "Ferrovia Short Line",        # 35
    "Sorte",                      # 36
    "Praca Park Place",           # 37
    "Taxa de Luxo",               # 38
    "Calcadao Boardwalk"          # 39
]

cartas_sorte = [
    ("Receba $100", 100),
    ("Receba $50", 50),
    ("Pague $50", -50),
    ("Pague $100", -100)
]

cartas_cofre = [
    ("Receba herança de $200", 200),
    ("Receba restituição de $100", 100),
    ("Pague multa de $50", -50),
    ("Pague conserto da casa $100", -100)
]

propriedades = {

    "Avenida Mediterranea": {
        "preco": 60,
        "aluguel": 10,
        "dono": None
    },

    "Avenida Baltica": {
        "preco": 60,
        "aluguel": 20,
        "dono": None
    },

    "Avenida Oriental": {
        "preco": 100,
        "aluguel": 30,
        "dono": None
    },

    "Avenida Vermont": {
        "preco": 100,
        "aluguel": 30,
        "dono": None
    },

    "Avenida Connecticut": {
        "preco": 120,
        "aluguel": 40,
        "dono": None
    },

    "Avenida dos Estados": {
        "preco": 140,
        "aluguel": 50,
        "dono": None
    },

    "Avenida Virginia": {
        "preco": 160,
        "aluguel": 60,
        "dono": None
    },

    "Avenida Tennessee": {
        "preco": 180,
        "aluguel": 70,
        "dono": None
    },

    "Avenida Nova York": {
        "preco": 200,
        "aluguel": 80,
        "dono": None
    },

    "Avenida Kentucky": {
        "preco": 220,
        "aluguel": 90,
        "dono": None
    },

    "Avenida Indiana": {
        "preco": 220,
        "aluguel": 90,
        "dono": None
    },

    "Avenida Illinois": {
        "preco": 240,
        "aluguel": 100,
        "dono": None
    },

    "Avenida Atlantica": {
        "preco": 260,
        "aluguel": 110,
        "dono": None
    },

    "Avenida Ventnor": {
        "preco": 260,
        "aluguel": 110,
        "dono": None
    },

    "Jardins Marvin": {
        "preco": 280,
        "aluguel": 120,
        "dono": None
    },

    "Avenida Pacifica": {
        "preco": 300,
        "aluguel": 130,
        "dono": None
    },

    "Avenida Carolina do Norte": {
        "preco": 300,
        "aluguel": 130,
        "dono": None
    },

    "Avenida Pennsylvania": {
        "preco": 320,
        "aluguel": 150,
        "dono": None
    },

    "Praca Park Place": {
        "preco": 350,
        "aluguel": 175,
        "dono": None
    },

    "Calcadao Boardwalk": {
        "preco": 400,
        "aluguel": 200,
        "dono": None
    },

    "Ferrovia Reading": {
        "preco": 200,
        "aluguel": 50,
        "dono": None
    },

    "Ferrovia Pennsylvania": {
        "preco": 200,
        "aluguel": 50,
        "dono": None
    },

    "Ferrovia B&O": {
        "preco": 200,
        "aluguel": 50,
        "dono": None
    },

    "Ferrovia Short Line": {
        "preco": 200,
        "aluguel": 50,
        "dono": None
    },

    "Companhia Eletrica": {
    "preco": 150,
    "aluguel": 40,
    "dono": None
    },

    "Companhia de Agua": {
        "preco": 150,
        "aluguel": 40,
        "dono": None
    }



}
print(f"Você parou em: {tabuleiro[posicao]}")

print("\nCasa atual:")
print(tabuleiro[posicao])

rodada = 1

while rodada <= 200:

    print(f"\n===== RODADA {rodada} =====")

    jogador_joga = True

    if rodadas_preso > 0:

        (
            rodadas_preso,
            tentativas_prisao,
            dinheiro
        ) = tentativa_prisao(
            rodadas_preso,
            tentativas_prisao,
            dinheiro
        )


    else:

        if jogador_joga:

            input("\nPressione ENTER para jogar o dado")

            dado1, dado2 = jogar_dado()

            dado = dado1 + dado2

            print(
                f"Você tirou "
                f"{dado1} e {dado2}"
            )

            print(
                f"Total: {dado}"
            )

            if dado1 == dado2:

                print(
                    "DADOS IGUAIS!"
                )

            posicao += dado

        if posicao >= len(tabuleiro):

            posicao -= len(tabuleiro)

            dinheiro += 200

            print("Você passou pela partida!")
            print("Você ganhou $200!")

        print(f"Nova posição: {posicao}")

        print(f"Você parou em: {tabuleiro[posicao]}")

    if posicao >= len(tabuleiro):

        posicao -= len(tabuleiro)

        dinheiro += 200

        print("Você passou pela partida!")
        print("Você ganhou $200!")

        print(f"Nova posição: {posicao}")

        print(f"Você parou em: {tabuleiro[posicao]}")

    casa = tabuleiro[posicao]

    if jogador_joga:  

        if casa == "Sorte":
            dinheiro = carta_sorte(
                dinheiro,
                cartas_sorte
            )

        if casa == "Cofre":
            dinheiro = carta_cofre(
                dinheiro,
                cartas_cofre
            )

        if casa == "Imposto de Renda":
            dinheiro = cobrar_taxa(
                dinheiro,
                200,
                "Imposto de Renda"
            )

        if casa == "Taxa de Luxo":
            dinheiro = cobrar_taxa(
                dinheiro,
                100,
                "Taxa de Luxo"
            )

        if casa == "Prisao" or casa == "Vá para a Prisao":

            resultado = random.choice(
                ["visita", "preso"]
            )

            if resultado == "visita":

                print(
                    "\nApenas visitando a prisão."
                )

            else:

                posicao = 10

                rodadas_preso = 2

                print(
                    "\nVocê foi PRESO!"
                )

                print(
                    "Ficará 2 rodadas sem jogar."
                )

        if casa in propriedades:

            prop = propriedades[casa]

            if prop["dono"] is None:

                print("\n===== PROPRIEDADE =====")

                print(f"Nome: {casa}")

                print(f"Preço: ${prop['preco']}")

                print(f"Aluguel: ${prop['aluguel']}")

                print(f"Saldo atual: ${dinheiro}")

                resposta = input(
                    "Deseja comprar? (s/n): "
                ).lower()

                if resposta == "" or resposta == "s":

                    if dinheiro >= prop["preco"]:

                        dinheiro -= prop["preco"]

                        prop["dono"] = nome

                        print("Propriedade comprada!")

                    else:

                        print("Dinheiro insuficiente!")

            else:

                print(
                    f"A propriedade pertence a "
                    f"{prop['dono']}"
                )

                if prop["dono"] != nome:

                    aluguel = prop["aluguel"]

                    dinheiro -= aluguel

                    for j in range(len(bots)):

                        if bots[j] == prop["dono"]:

                            dinheiro_bots[j] += aluguel

                    print(
                        f"Você pagou "
                        f"${aluguel} "
                        f"para {prop['dono']}!"
                    )

                    print(
                        f"Seu saldo agora é "
                        f"${dinheiro}"
                    )

        print(f"Dinheiro atual: ${dinheiro}")

    for i in range(len(bots)):

        if preso_bots[i] > 0:

            print(
                f"{bots[i]} está preso."
            )

            preso_bots[i] -= 1

            continue

        if dinheiro_bots[i] <= 0:

            continue

        print(f"\n--- Vez de {bots[i]} ---")

        dado1, dado2 = jogar_dado()

        dado_bot = dado1 + dado2

        print(
            f"{bots[i]} tirou "
            f"{dado1} e {dado2}"
        )

        print(
            f"Total: {dado_bot}"
        )

        if dado1 == dado2:

            print(
                "DADOS IGUAIS!"
            )

        posicoes_bots[i] += dado_bot

        if posicoes_bots[i] >= len(tabuleiro):

            posicoes_bots[i] -= len(tabuleiro)

        casa_bot = tabuleiro[posicoes_bots[i]]

        print(f"{bots[i]} parou em: {casa_bot}")

        if casa_bot == "Sorte":
        
            texto, valor = random.choice(cartas_sorte)
        
            print(f"\nCARTA SORTE DE {bots[i]}:")
            print(texto)
        
            dinheiro_bots[i] += valor
        
            print(
                f"Novo saldo de {bots[i]}: "
                f"${dinheiro_bots[i]}"
            )

        if casa_bot == "Cofre":

            texto, valor = random.choice(cartas_cofre)

            print(f"\nCARTA COFRE DE {bots[i]}:")
            print(texto)

            dinheiro_bots[i] += valor

            print(
                f"Novo saldo de {bots[i]}: "
                f"${dinheiro_bots[i]}"
            )

        if casa_bot == "Imposto de Renda":

            dinheiro_bots[i] -= 200

            print(
                f"{bots[i]} pagou "
                f"$200 de imposto!"
            )

        if casa_bot == "Taxa de Luxo":

            dinheiro_bots[i] -= 100

            print(
                f"{bots[i]} pagou "
                f"$100 de taxa de luxo!"
            )

        if casa_bot in ["Vá para a Prisao", "Prisao"]:

            resultado = random.choice(
                ["visita", "preso"]
            )

            if resultado == "preso":

                posicoes_bots[i] = 10

                preso_bots[i] = 2

                print(
                    f"{bots[i]} foi PRESO!"
                )

            else:

                print(
                    f"{bots[i]} está apenas visitando."
                )


        if casa_bot in propriedades:

            prop = propriedades[casa_bot]

            if prop["dono"] is None:

                comprar = decidir_compra(
                    tipos_bots[i],
                    dinheiro_bots[i],
                    prop["preco"]
                )

                if comprar and dinheiro_bots[i] >= prop["preco"]:

                    prop["dono"] = bots[i]

                    dinheiro_bots[i] -= prop["preco"]

                    print(
                        f"{bots[i]} comprou "
                        f"{casa_bot}"
                    )

                    print(
                        f"Saldo do {bots[i]}: "
                        f"${dinheiro_bots[i]}"
                    )

                else:

                    print(
                        f"{bots[i]} não comprou "
                        f"a {casa_bot}"
                    )


            elif prop["dono"] == nome:

                aluguel = prop["aluguel"]

                dinheiro += aluguel

                dinheiro_bots[i] -= aluguel

                print(
                    f"{bots[i]} pagou "
                    f"${aluguel} de aluguel!"
                )

                print(
                    f"Seu saldo agora é "
                    f"${dinheiro}"
                )

            elif prop["dono"] != nome and prop["dono"] != bots[i]:

                aluguel = prop["aluguel"]

                dinheiro_bots[i] -= aluguel

                for j in range(len(bots)):

                    if bots[j] == prop["dono"]:

                        dinheiro_bots[j] += aluguel

                print(
                    f"{bots[i]} pagou "
                    f"${aluguel} para "
                    f"{prop['dono']}!"
                )

    mostrar_placar(
    nome,
    dinheiro,
    bots,
    dinheiro_bots,
    propriedades
)

    if dinheiro <= 0:

        print("\n====================")
        print(f"{nome} FALIU!")
        print("====================")

        ativos = []

        for i in range(len(bots)):

            if dinheiro_bots[i] > 0:

                ativos.append(bots[i])

        if len(ativos) > 0:

            print("\n====================")
            print("TEMOS UM VENCEDOR!")
            print(f"VENCEDOR: {ativos[0]}")
            print("====================")

        break

    ativos = []

    if dinheiro > 0:
        ativos.append(nome)

    for i in range(len(bots)):

        if dinheiro_bots[i] > 0:
            ativos.append(bots[i])

    if len(ativos) == 1:

        print("\n====================")
        print("TEMOS UM VENCEDOR!")
        print(f"VENCEDOR: {ativos[0]}")

        if ativos[0] == nome:

            print(
                f"Patrimônio final: "
                f"${dinheiro}"
            )

        else:

            for i in range(len(bots)):

                if bots[i] == ativos[0]:

                    print(
                        f"Patrimônio final: "
                        f"${dinheiro_bots[i]}"
                    )

        print("====================")


        break

    print(f"Fim da rodada {rodada}")

    rodada += 1

print(f"\nTotal de casas: {len(tabuleiro)}")