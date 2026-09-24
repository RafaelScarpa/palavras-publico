#Este arquivo modulo conteria o fluxo de jogo principal, de forma completamente separada da interface do usuário.

import random
from PIL import Image, ImageEnhance
from enum import Enum
import numpy as np
import io
import bolsa
import tabuleiro as tabuleiros
import pontos
import oponente
from converterEmoji import comparar as emojis
import ficha as F
from typing import Literal

class Partida:
    em_andamento: bool = False
    modo: int
    jogadores: int
    tabuleiro: F.Tabuleiro  # [↓[→]]
    ponto_início: list[int]
    mãos: list[list[F.tipo_fichas]]
    pontuações: list[int | float]
    jogador_atual: int = 0
    ganhador: list[int] | None = None
    pulos: list[bool]  # [pular?]
    rodadas_sem_marcar: int = 0
    configurações: list[int | str]  # [tabuleiro, bolsa, dicionário]
    dificuldade: None | int = None
    tempos: list  # [segundos, ..., continuo?, +adicionar]
    punições: list[int]
    novos: list[list[bool]]  # As fichas que mudaram desde a última rodada.
    # Abaixo, podem ajudar a lembrar quais são os jogadores e em que ordem jogam
    lista_de_jogadores: dict[int, int] = {}  # {id:posição}
    lista_de_jogadores_inversa: dict[int, int] = {}  # {posição:id}

    def __init__(self, modo: int, configurações: list[int | str], jogadores: int, tabuleiro: F.Tabuleiro, ponto_início: list[int], mãos: list[list[F.tipo_fichas]], tempo: list):
        self.em_andamento = True
        self.modo = modo
        self.jogadores = jogadores
        self.configurações = configurações
        self.tabuleiro = tabuleiro
        self.ponto_início = ponto_início
        self.mãos = mãos
        self.pontuações = [0 for _ in range(jogadores)]
        self.pulos = [False for _ in range(jogadores)]
        self.tempos = [tempo[0] for _ in range(jogadores)]
        self.tempos += tempo[1:]
        self.punições = [0 for _ in range(jogadores)]
        self.novos = [[False for _2 in _1] for _1 in tabuleiro]
        # O que não foi definido, será definido em seguida.


class SemPartida(Partida):
    def __init__(self): pass


partidas: dict[int, Partida] = {} #{id:partida}


#presets

#presets

#presets

#setup

#setup


#fluxo de jogo principal

#fluxo de jogo

#elemento de gameplay

#elemento de gameplay

#fluxo de jogo

#output

#output


def imagem_tabuleiro(num: int, para_arquivo: type):
    global partidas
    p = partidas[num]
    tabuleiro = p.tabuleiro

    grande = Image.new('RGBA', size=((len(tabuleiro[-1]) + 1) * 128, (len(tabuleiro) + 1) * 128))
    borda = Image.open(r"assets\régua_g.png")
    grande.paste(borda.convert('RGBA'))
    borda.close()
    for y, linha in enumerate(tabuleiro):
        for x, ficha in enumerate(linha):
            try:
                aqui = Image.open(fr"assets\{ficha.emoji}.png")
            except FileNotFoundError:
                aqui = Image.open(fr"assets\❓.png")
            if p.novos[y][x]:
                tal = ImageEnhance.Color(aqui.convert('RGBA')).enhance(2.5)
            else:
                tal = aqui.convert('RGBA')
            grande.paste(tal, ((x + 1) * 128, (y + 1) * 128))
            aqui.close()
    with io.BytesIO() as f:
        grande.save(f, "png")
        f.seek(0)
        return para_arquivo(f, "tabuleiro.png")


#output

#outuput

#output auxiliar

#mecânica auxiliar

#mecânica auxiliar

#Arquivo original: 481 linhas
