from unicodedata import name


#auxiliar

#auxiliar

#auxiliar

#auxiliar


class FichaBase:
    __slots__ = []

    letra: str | None = None
    valor: int = 0
    trocavel: bool = True
    atalho: str = ''
    emoji: str = "❓"
    string: str = " ## "
    multiletra: int = 1
    multipalavra: int = 1

    #
    #
    #  5 definições
    #
    #

class Vazia(FichaBase):
    __slots__ = []

    trocavel = True
    string = "[  ]"
    emoji = "fV"


#
#+2 classes derivadas

DL = lambda: Multi(L=2)
TL = lambda: Multi(L=3)
QL = lambda: Multi(L=4)

DP = lambda: Multi(P=2)
TP = lambda: Multi(P=3)
QP = lambda: Multi(P=4)


class Letra(FichaBase):
    __slots__ = ['letra', 'valor', 'trocavel', 'atalho', 'emoji', 'string']

    def __init__(self, letra: str, valor: int = 0, string: str | None = None, atalho: str | None = None):
        self.trocavel: bool = False

        self.letra = letra.upper()
        self.valor: int = valor
        self.atalho: str = letra_para_atalho(self.letra) if atalho is None else atalho.upper()
        self.emoji: str = "".join(["l", letra_para_emoji(self.letra), str(self.valor)])
        self.string: str = f"{self.letra:^4}" if string is None else string


class Coringa(FichaBase):
    __slots__ = ['letra', 'valor', 'trocavel', 'atalho', 'emoji', 'string', 'permitidos']

    def __init__(self, permitidos: set[str] | None = None):
        self.letra: str | None = None
        self.valor = 0
        self.trocavel = False
        self.atalho = ''
        self.emoji: str = "fC"
        self.string: str = " ?  "

        self.permitidos: set[str] = set() if permitidos is None else permitidos

    def escolher(self, atalho: str) -> bool:
        if self.permitidos != set() and atalho not in self.permitidos:
            raise ValueError(f"Atalho {atalho} não existe entre permitidos.\nP: {self.permitidos}")
        self.letra = atalho_para_letra(atalho)
        self.atalho = atalho.upper()
        self.emoji = "".join(["l", letra_para_emoji(self.letra), "0"])
        self.string = f"{self.letra:^4}"
        return True


#+1 classe derivada


type tipo_fichas = Vazia | Furo | Multi | Letra | Coringa | Gelo
type Tabuleiro = list[list[tipo_fichas]]
type Mão = list[tipo_fichas]

#Arquivo original: 175 linhas