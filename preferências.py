import pickle


prefs: dict[int, dict[int | str, str]]
try:
    with open("prefs.pkl", "rb") as f:
        prefs = pickle.load(f)
except FileNotFoundError:
    prefs = dict()
    print("'prefs.pkl' não encontrado.")


def atualizar(num: int, dados: dict[int | str, str] | None) -> bool:
    global prefs
    if dados is None:
        if num in prefs:
            del prefs[num]
        else:
            return False
    else:
        prefs |= {num: dados}
    with open("prefs.pkl", "wb") as f:
        pickle.dump(prefs, f)
    return True