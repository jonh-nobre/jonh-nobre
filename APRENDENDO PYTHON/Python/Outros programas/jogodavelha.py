# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-----")

# Função para verificar se alguém venceu
def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == jogador and tabuleiro[1][coluna] == jogador and tabuleiro[2][coluna] == jogador:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False

# Função para realizar a jogada
def fazer_jogada(tabuleiro, jogador, linha, coluna):
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        return False

# Função principal
def jogar_jogo_da_velha():
    tabuleiro = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

    jogador_atual = "X"
    jogo_terminado = False

    while not jogo_terminado:
        imprimir_tabuleiro(tabuleiro)
        print("É a vez do jogador", jogador_atual)
        linha = int(input("Digite o número da linha (0-2): "))
        coluna = int(input("Digite o número da coluna (0-2): "))

        if fazer_jogada(tabuleiro, jogador_atual, linha, coluna):
            if verificar_vencedor(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print("O jogador", jogador_atual, "venceu!")
                jogo_terminado = True
            elif " " not in tabuleiro[0] and " " not in tabuleiro[1] and " " not in tabuleiro[2]:
                imprimir_tabuleiro(tabuleiro)
                print("O jogo empatou!")
                jogo_terminado = True
            else:
                jogador_atual = "O"
        else:
            print("Jogada inválida. Tente novamente.")

# Iniciar o jogo
jogar_jogo_da_velha()
