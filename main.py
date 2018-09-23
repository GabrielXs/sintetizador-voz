# Sintetizador de Voz
# usando a Biblioteca pyttsx3

__author__ = "Gabriel Xavier da Silva"

# importando a biblioteca

import pyttsx3
"""
ImportError - Quando o driver solicitado não é encontrado
RuntimeError - Quando o driver falha ao inicializar
"""

while True:
    try:
        engine = pyttsx3.init()
    except ImportError:
        print("Erro ao Encontrar driver solicitado!")
        print("Reiniciando...")
    except RuntimeError:
        print("Erro Ao inicializar a instancia reiniciando a aplicaçao")
        continue

    texto = input("Digite um texto:  ")
    if texto == 'n':
        break

    else:
        engine.say(texto)
        engine.runAndWait()

