#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da linha configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar: 

Tenha a variável de ambiente LANG devidamente configurada, ex:

    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py 
"""
#Dunder - Nome dado a dois underscores
__version__ = "0.0.1"
__author__ = "Washington Cardoso"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "pt_BR")[:5]

msg = "Olá, Mundo!"

if current_language == "en_US":
    msg = "Hello, World!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjuor, Monde!"

print(msg)
