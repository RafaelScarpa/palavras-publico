import ficha as f
import random


type lista_de_paramentros = list[tuple[tuple[str, int, str | None], int] | tuple[tuple[str, int, str | None, str], int]]


def montar(detalhes: lista_de_paramentros, coringas: int, loops: int = 1) -> list[f.tipo_fichas]:
    resultado: list[f.tipo_fichas] = []
    tipos: set[str] = set()
    letra: str
    pontos: int
    for item in detalhes:
        parametros, quantos = item
        letra, pontos, *opcionais = parametros
        for _ in range(quantos * loops):
            resultado.append(f.Letra(letra, pontos, *opcionais))
        tipos.add(f.letra_para_atalho(letra).lower())  # Criar uma lista de permissão para o coringa.
    for _ in range(coringas * loops):
        resultado.append(f.Coringa(tipos))
    return resultado


#setup


Scrabble: lista_de_paramentros = [
    (("A", 1, " A ₁"), 9),
    (("B", 3, " B ₃"), 2),
    (("C", 3, " C ₃"), 2),
    (("D", 2, " D ₂"), 4),
    (("E", 1, " E ₁"), 12),
    (("F", 4, " F ₄"), 2),
    (("G", 2, " G ₂"), 3),
    (("H", 4, " H ₄"), 2),
    (("I", 1, " I ₁"), 9),
    (("J", 8, " J ₈"), 1),
    (("K", 5, " K ₅"), 1),
    (("L", 1, " L ₁"), 4),
    (("M", 3, " M ₃"), 2),
    (("N", 1, " N ₁"), 6),
    (("O", 1, " O ₁"), 8),
    (("P", 3, " P ₃"), 2),
    (("Q", 10, " Q₁₀"), 1),
    (("R", 1, " R ₁"), 6),
    (("S", 1, " S ₁"), 4),
    (("T", 1, " T ₁"), 6),
    (("U", 1, " U ₁"), 2),
    (("V", 4, " V ₄"), 2),
    (("W", 4, " W ₄"), 2),
    (("X", 8, " X ₈"), 1),
    (("Y", 4, " Y ₄"), 2),
    (("Z", 10, " Z₁₀"), 1)
]

#
#
#
#
#     9 definições de bolsa
#
#
#
#

#setup

#mecânica

#mecânica

#Arquivo original: 350 linhas