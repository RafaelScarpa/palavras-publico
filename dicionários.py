from functools import lru_cache as cache

arquivos = [
    r"words.txt",
    r"palavras com çã.txt",
    r"nimi.txt",
    r"palavras com ç.txt",
    r"palavras sem acentos.txt",
    r"mots.txt",
    r"palabras con ñ.txt",
    r"palabras sin acentos.txt",
    r"parole.txt",
    r"todos.txt"  # Sempre no final.
]

arquivos_extra = arquivos + [
    r"palavras com todos os acentos.txt",
    r"palabras con todos los acentos.txt",
]

@cache(20)
def carregar(*quais: str, direto: bool = False) -> list[str]:
    novo: set[str] = set()
    texto = ""
    if r"todos.txt" in quais:
        quais = tuple(arquivos + arquivos_extra)
    for nome_arquivo in quais:
        with open(fr"assets\{nome_arquivo}", "r", encoding="utf-8") as f:
            if direto:
                texto += "\n".join(j.strip() for j in f.readlines() if len(j.strip()) >= 2)
            else:
                for i in f.readlines():
                    limpo = i.strip()
                    if len(limpo) < 2:
                        continue
                    novo.add(limpo.upper())
    if direto:
        return [f"\n{texto}\n"]
    else:
        return list(novo)