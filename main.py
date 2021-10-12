import os
import time
from graphics import Graphics
from levels import Level

def run():
    os.system('cls')
    Graphics.welcome()
    faults = 0
    hits = 0
    while True:
        try: 
            nivel = int(input(
chr(27) + "[3;33m" + """
Modo de juego

Nivel 1: Palabras
Nivel 2: Frases

Elije el nivel: """ + chr(27) + "[0m"))
            if nivel == 1:
                Level.lvl1(faults, hits)
                option = input("Precione 'J' para volver a jugar: ").strip().upper()
                if option == "J":
                    option = ""
                    os.system('py main.py')                    
                break
            if nivel == 2:
                Level.lvl2(faults, hits)
                option = input("Precione 'J' para volver a jugar: ").strip().upper()
                if option == "J":
                    option = ""
                    os.system('py main.py')
                break
            if nivel != 1 or nivel != 2:
                input("Opcion incorrecta, precione ENTER para continuar")
                run()
        except:
            print("Err")
            time.sleep(3)
            break
        

if __name__ == '__main__':
    run()