#Este modulo conteria a interface do usuário (API do Discord) separado do fluxo de gameplay, apenas reagindo a eventos apropriadamente.

import mainJogo as jogo
import preferências
import localizaçãoBot as T
import discord as dsc
from typing import Literal, Callable, Any, Optional
from os import getenv
import sys
from dotenv import load_dotenv
import asyncio
from functools import lru_cache as cache
from datetime import timedelta as TD, datetime as DT
from enum import Enum
import gettext
from openpyxl.utils import column_index_from_string as letras_número, get_column_letter as número_letra


load_dotenv()
TOKEN = getenv('DEV')
com = dsc.app_commands
útil = dsc.utils
ls = com.locale_str


gettext.bindtextdomain("bot", "./locale")
gettext.textdomain("bot")
tradutor = gettext.translation("bot", "./locale", languages=['pt-br'])
tradutor.install()

class meuTradutor(com.Translator):
    async def translate(self, string: com.locale_str, locale: dsc.Locale, context: Any) -> str | None:
        if locale.language_code == 'pt-BR':
            return tradutor.gettext(string.message)
        else:
            return None


class meuClient(dsc.Client):
    def __init__(self) -> None:
        super().__init__(intents = dsc.Intents.default())
        self.tree = com.CommandTree(self, allowed_installs=com.AppInstallationType(guild=True), allowed_contexts=com.AppCommandContext(guild=True))

client = meuClient()

@client.event
async def on_ready():
    await client.tree.set_translator(meuTradutor())
    await client.tree.sync()
    # Avisar que tudo deu certo.
    print('Versão do Nextcord: ' + dsc.__version__)
    print(f'Login como @{client.user}!')
    print(DT.now().strftime(r"%d/%m/%Y, %H:%M:%S"))
    print('-----')

#setup


#elemento ui (1)

#elemento ui (2)

#elemento ui (3)

#elemento ui (4)

#elemento ui (5)

#elemento ui (6)

#elemento ui (7)

#elemento ui (8)

#elemento ui (9)

#elemento ui (10)


#API


#fim de jogo

#fluxo de jogo

#intenacionalização

#fluxo de jogo (timer)

#fluxo de jogo

#fluxo de jogo

#oponente CPU


#input usuário (1)

#input usuário (2)

#início jogo

#input usuário (3)

#input usuário (4)

#input usuário (5)

#input usuário (6)

#input usuário (7)

#oponente CPU

#input usuário (8)

#input usuário (9)

#input usuário (10)

#input usuário (11)

#input usuário (12) (config)

#input usuário (13)

# Começa
if __name__ == "__main__":
    print('-----')
    if TOKEN is not None:
        try:
            client.run(TOKEN)
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        print("Você esqueceu do token do bot!!")
        sys.exit(1)

#Arquivo original: 988 linhas
