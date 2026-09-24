#Este arquivo se encarrega de colocar as palavras no tabuleiro, lidar com as consequências e dar a pontuação da jogada.

import copy
import ficha
from typing import Literal
import dicionários


dicionário: dict[int | str, list[str]] = {}
vogais = ("a", "e", "i", "o", "u")


def iniciar(dic: int | str):
    global dicionário
    nome_arquivo: set[str]
    match dic:
        case 't':  # Todos
            nome_arquivo = set(dicionários.arquivos_extra)
        case _:
                assert type(dic) == int
                nome_arquivo = {dicionários.arquivos[dic]}
    dicionário[dic] = dicionários.carregar(*nome_arquivo)
    return dicionário[dic]


class Não:
    __slots__ = ['palavras', 'erro', 'mão']
    certo: Literal[False] = False

    def __init__(self, tipo: int | None = None, palavras: list[str] | None = None, mão: str = ''):
        self.erro: int = 0
        if palavras is None:
            palavras = []
        if tipo is None:
            if mão:
                self.erro = 1
            elif palavras:
                self.erro = 2
        else:
            self.erro = tipo
        self.mão: str = mão
        self.palavras: list[str] = palavras


class Sim:
    __slots__ = ['palavras', 'pontos_palavras', 'bônus', 'total']
    certo: Literal[True] = True

    def __init__(self, palavras: list[str], pontos: list[int | float], bônus: int):
        self.palavras: list[str] = palavras
        self.pontos_palavras: list[int | float] = pontos
        self.bônus: int | float = bônus
        self.total: int | float = sum(pontos, bônus)


#interpertação do input em texto do usuário, codificação precisa das regras do jogo

#auxiliar

#Arquivo original: 232 linhas.
