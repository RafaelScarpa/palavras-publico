import ficha as f
import copy


Scrabble: f.Tabuleiro = [
    [f.TP(), f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia(), f.Vazia(), f.TP(), f.Vazia(), f.Vazia(), f.Vazia(),  f.DL(), f.Vazia(),  f.Vazia(), f.TP()],
    [f.Vazia(), f.DP(), f.Vazia(), f.Vazia(), f.Vazia(), f.TL(), f.Vazia(), f.Vazia(), f.Vazia(), f.TL(), f.Vazia(), f.Vazia(), f.Vazia(), f.DP(), f.Vazia()],
    [f.Vazia(), f.Vazia(), f.DP(), f.Vazia(), f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia(), f.Vazia(), f.DP(), f.Vazia(), f.Vazia()],
    [f.DL(), f.Vazia(), f.Vazia(), f.DP(), f.Vazia(), f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia(), f.Vazia(), f.DP(), f.Vazia(), f.Vazia(),  f.DL()],
    [f.Vazia(), f.Vazia(), f.Vazia(), f.Vazia(), f.DP(), f.Vazia(), f.Vazia(), f.Vazia(), f.Vazia(), f.Vazia(), f.DP(), f.Vazia(), f.Vazia(), f.Vazia(), f.Vazia()],
    [f.Vazia(), f.TL(), f.Vazia(), f.Vazia(), f.Vazia(), f.TL(), f.Vazia(), f.Vazia(), f.Vazia(), f.TL(), f.Vazia(), f.Vazia(), f.Vazia(), f.TL(), f.Vazia()],
    [f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia()],
    [f.TP(), f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia(), f.Vazia(), f.DP(), f.Vazia(), f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia(), f.TP()],
    [f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia()],
    [f.Vazia(), f.TL(), f.Vazia(), f.Vazia(), f.Vazia(), f.TL(), f.Vazia(), f.Vazia(), f.Vazia(), f.TL(), f.Vazia(), f.Vazia(), f.Vazia(), f.TL(), f.Vazia()],
    [f.Vazia(), f.Vazia(), f.Vazia(), f.Vazia(), f.DP(), f.Vazia(), f.Vazia(), f.Vazia(), f.Vazia(), f.Vazia(), f.DP(), f.Vazia(), f.Vazia(), f.Vazia(), f.Vazia()],
    [f.DL(), f.Vazia(), f.Vazia(), f.DP(), f.Vazia(), f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia(), f.Vazia(), f.DP(), f.Vazia(), f.Vazia(),  f.DL()],
    [f.Vazia(), f.Vazia(), f.DP(), f.Vazia(), f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia(), f.Vazia(), f.DP(), f.Vazia(), f.Vazia()],
    [f.Vazia(), f.DP(), f.Vazia(), f.Vazia(), f.Vazia(), f.TL(), f.Vazia(), f.Vazia(), f.Vazia(), f.TL(), f.Vazia(), f.Vazia(), f.Vazia(), f.DP(), f.Vazia()],
    [f.TP(), f.Vazia(), f.Vazia(), f.DL(), f.Vazia(), f.Vazia(), f.Vazia(), f.TP(), f.Vazia(), f.Vazia(), f.Vazia(),  f.DL(), f.Vazia(),  f.Vazia(), f.TP()]
]
#
#
#
#
#10 definições de tabuleiro
#
#
#
#
#

def iniciar(tipo: int) -> tuple[f.Tabuleiro, list[int]]:
    match tipo:
        case 1:
            tabuleiro = copy.deepcopy(SuperScrabble)
            começo = [10, 10]
        case 2:
            tabuleiro = copy.deepcopy(Scratch)
            começo = [7, 7]
        case 3:
            tabuleiro = copy.deepcopy(Shrek)
            começo = [9, 9]
        case 4:
            tabuleiro = copy.deepcopy(WordsWithFriends)
            começo = [7, 7]
        case 5:
            tabuleiro = copy.deepcopy(Lexulous)
            começo = [7, 7]
        case 6:
            tabuleiro = copy.deepcopy(Recontextualize)
            começo = [0, 0]
        case 7:
            tabuleiro = copy.deepcopy(Wordfeud)
            começo = [7, 7]
        case 8:
            tabuleiro = copy.deepcopy(Battlefield)
            começo = [6, 6]
        case 9:
            tabuleiro = copy.deepcopy(Quad)
            começo = [7,7]
        case 10:
            tabuleiro = copy.deepcopy(Scarabeo)
            começo = [8,8]
        case 0 | _:
            tabuleiro = copy.deepcopy(Scrabble)
            começo = [7, 7]
    return tabuleiro, começo

#Arquivo original: 258 linhas