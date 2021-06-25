import os
import random
import time


def welcome():
    print(""""
    ▄▄▄▄▄    ▀   ▄▄▄▄▄   ▄▄▄   ▄   ▄       ▄   ▄▄▄▄▄   ▄▄▄   ▄   ▀   ▄▄▄▄     ▄▄▄▄▄▄
    █    █   █   █       █ █   █    █     █    █       █ █   █   █   █   █    █    █
    █ █■■    █   █■■■    █  █  █     █   █     █■■■    █  █  █   █   █    █   █    █
    █    █   █   █       █   █ █      █ █      █       █   █ █   █   █   █    █    █
    ▀▀▀▀▀    ▀   ▀▀▀▀▀   ▀   ▀▀▀       ▀       ▀▀▀▀▀   ▀   ▀▀▀   ▀   ▀▀▀▀     ▀▀▀▀▀▀
    """)
    time.sleep(1)
    os.system('cls')
    print(chr(27) + "[1;31m" + """
    ▄▄▄▄▄    ▀   ▄▄▄▄▄   ▄▄▄   ▄   ▄       ▄   ▄▄▄▄▄   ▄▄▄   ▄   ▀   ▄▄▄▄     ▄▄▄▄▄▄ {
    █   █   █   █       █ █   █    █     █    █       █ █   █   █   █   █    █    █
    █ █■■    █   █■■■    █  █  █     █   █     █■■■    █  █  █   █   █    █   █    █
    █   █   █   █       █   █ █      █ █      █       █   █ █   █   █   █    █    █
    ▀▀▀▀▀    ▀   ▀▀▀▀▀   ▀   ▀▀▀       ▀       ▀▀▀▀▀   ▀   ▀▀▀   ▀   ▀▀▀▀     ▀▀▀▀▀▀
    """ + chr(27) + "[0m")
    time.sleep(1)
    os.system('cls')



def win():
    """Show some graphics if the user wins.

    retuns graphics.
    """
    os.system('cls')
    print(chr(27) + "[1;32m" + """
        ╔═════════════╗
        ║           ╔═══╗
        ║          [▀ ▄ ▀]
        ║           └───┘
        ║             ║
        ║          ▄▄▄║▄▄▄
        ║             ║
        ║             ║
        ║            █ █
        ║           ▀   ▀
        ║
        ╩═══════[~~~~~~~~~~]
        """ + chr(27)  + "[0m")
    time.sleep(0.3)
    os.system('cls')
    print(chr(27) + "[1;32m" + """
        ╔═════════════╗
        ║           ╔═══╗
        ║          [▀ ▄ ▀]
        ║           └───┘
        ║             ║
        ║          ▄▄▄║▄▄▄
        ║             ║
        ║             ║
        ║            █ █
        ║           ▀   ▀
        ║
        ╩═══════[]
        """ + chr(27)  + "[0m")
    time.sleep(0.3)
    os.system('cls')
    print(chr(27) + "[1;32m" + """
        ╔═════════════╗
        ║        
        ║           ╔═══╗
        ║          [▀ ▄ ▀]
        ║           └───┘
        ║             ║
        ║          ▄▄▄║▄▄▄
        ║             ║
        ║             ║
        ║            █ █
        ║           ▀   ▀
        ╩═══════[]
        """ + chr(27)  + "[0m")
    time.sleep(0.3)
    os.system('cls')
    print(chr(27) + "[1;32m" + """
        ╔═════════════╗
        ║        
        ║          
        ║           ╔═══╗
        ║          [▀ ▄ ▀]
        ║           └───┘
        ║             ║
        ║          ▄▄▄║▄▄▄
        ║             ║
        ║             ║
        ║            █ █
        ╩═══════[]  ▀   ▀
        """ + chr(27)  + "[0m")
    time.sleep(0.3)
    os.system('cls')
    print(chr(27) + "[1;32m" + """
        ╔═════════════╗
        ║        
        ║          
        ║             ╔═══╗
        ║            [▀ ▄ ▀]
        ║             └───┘
        ║               ║
        ║            ▄▄▄║▄▄▄
        ║               ║
        ║               ║
        ║              █ █
        ╩═══════[]    ▀   ▀
        """ + chr(27)  + "[0m")
    time.sleep(0.3)
    os.system('cls')
    print(chr(27) + "[1;32m" + """
        ╔═════════════╗
        ║        
        ║          
        ║              ╔═══╗
        ║             [▀ ▄ ▀]
        ║              └───┘
        ║                ║
        ║             ▄▄▄║▄▄▄
        ║                ║
        ║                ║
        ║               █ █
        ╩═══════[]     ▀   ▀
        """ + chr(27)  + "[0m")
    time.sleep(0.3)
    os.system('cls')
    print(chr(27) + "[1;32m" + """
        ╔═════════════╗
        ║        
        ║          
        ║                  ╔═══╗
        ║                 [▀ ▄ ▀]
        ║                  └───┘
        ║                    ║
        ║                 ▄▄▄║▄▄▄
        ║                    ║
        ║                    ║
        ║                   █ █
        ╩═══════[]         ▀   ▀
        """ + chr(27)  + "[0m")
    time.sleep(0.3)
    os.system('cls')
    print(chr(27) + "[1;32m" + """
        ╔═════════════╗
        ║        
        ║          
        ║                    ╔═══╗
        ║                   [▀ ▄ ▀]
        ║                    └───┘
        ║                      ║
        ║                   ▄▄▄║▄▄▄
        ║                      ║
        ║                      ║
        ║                     █ █
        ╩═══════[]           ▀   ▀
        """ + chr(27)  + "[0m")        
    time.sleep(0.3)
    os.system('cls')
    print(chr(27) + "[1;32m" + """
        ╔═════════════╗
        ║                      
        ║                  
        ║                       ╔═══╗
        ║                      [▀ ▄ ▀]    
        ║        ¡YOU WIN!      └───┘ 
        ║                         ║ 
        ║                      ▄▄▄║▄▄▄ 
        ║                         ║  
        ║                         ║
        ║                        █ █ 
        ╩═══════[]              ▀   ▀
        """ + chr(27)  + "[0m")



def fail(faults):
    """Show a graphic for each fail.

    param Int faults, an num from 0 to 7.
    retuns graphic.
    """ 
    if faults == 0:
        print("""
        ╔═════════════╗
        ║       
        ║      
        ║
        ║
        ║
        ║
        ║        
        ║
        ║
        ║
        ╩═══════[~~~~~~~~~~]
        """)
    if faults == 1:
        print("""
        ╔═════════════╗
        ║           ╔═══╗
        ║          [▀ ▄ ▀]
        ║           └───┘
        ║
        ║
        ║
        ║
        ║
        ║
        ║
        ╩═══════[~~~~~~~~~~]
        """) 
    elif faults == 2:
        print("""
        ╔═════════════╗
        ║           ╔═══╗
        ║          [▀ • ▀]
        ║           └───┘
        ║             ║
        ║             ║
        ║             ║
        ║             ║
        ║
        ║
        ║
        ╩═══════[~~~~~~~~~~]
        """)
    elif faults == 3:
        print("""
        ╔═════════════╗
        ║           ╔═══╗
        ║          [▀ ▄ ▀]
        ║           └───┘
        ║             ║
        ║             ║▄▄▄
        ║             ║
        ║             ║
        ║            
        ║           
        ║
        ╩═══════[~~~~~~~~~~]
        """)
    elif faults == 4:
        print("""
        ╔═════════════╗
        ║           ╔═══╗
        ║          [▀ ▄ ▀]
        ║           └───┘
        ║             ║
        ║          ▄▄▄║▄▄▄
        ║             ║
        ║             ║
        ║              
        ║               
        ║
        ╩═══════[~~~~~~~~~~]
        """)
    elif faults == 5:
        print("""
        ╔═════════════╗
        ║           ╔═══╗
        ║          [▀ ▄ ▀]
        ║           └───┘
        ║             ║
        ║          ▄▄▄║▄▄▄
        ║             ║
        ║             ║
        ║              █
        ║               ▀
        ║
        ╩═══════[~~~~~~~~~~]
        """)
    elif faults == 6:
        print("""
        ╔═════════════╗
        ║           ╔═══╗
        ║          [▀ ▄ ▀]
        ║           └───┘
        ║             ║
        ║          ▄▄▄║▄▄▄
        ║             ║
        ║             ║
        ║            █ █
        ║           ▀   ▀
        ║
        ╩═══════[~~~~~~~~~~]
        """)

    elif faults == 7:
        print(chr(27) + "[1;31m" + """
        ╔═════════════╗
        ║
        ║            
        ║          
        ║         GAME OVER
        ║            
        ║            
        ║           ╔═══╗
        ║          [X × X]
        ║           ┌───┐
        ║             ║ 
        ╩═══════[~~~~~~~~~~]
        """ + chr(27)  + "[0m")
        


def normalize(char):
    """Receives an accented vowel and returns it without an accent.

    Param String "char" vocal.
    Returns la vocal sin acento.
    """
    dic_word = char.maketrans('ÁÉÍÓÚ', 'AEIOU')
    new_char = char.translate(dic_word)
    return new_char


def find_word():
    """Create a list of words, it's in "data.txt".
    Choose a word at random.

    Returs the chosen word.
    """
    try:
        words = []
        with open('./data.txt', "r", encoding="utf-8") as f:
            for line in f:
                words.append(line.strip().upper())
            word = random.choice(words)
        return word 
    except:
        print("Error al buscar la letra")


def run():
    os.system('cls')
    welcome()
    faults = 0
    hits = 0
    word_guess = find_word()       
    progress = ["_ " for i in range(len(word_guess))]
    letters_used = []

    while faults <= 7:
        os.system('cls')
        print("¡Adivina la palabra!")
        fail(faults) 
        if faults == 7:
            print(f'La palabra era: {word_guess}')
            break
        if hits == len(word_guess):
            win()
            break

        print(''.join(progress))
        print('Letras usadas: ', ', '.join(letters_used))
        try:
            letter_user = normalize(input("Elije una letra: ").strip().upper())
            assert letter_user.isalpha(), input("Caracter no valido, PRESIONE ENTER PARA CONTINUAR ")
            assert len(letter_user) == 1, input("Seleccione solo una letra, PRESIONE ENTER PARA CONTINUAR")
        except AssertionError as ae:
            print(ae)
            continue

        if letter_user in letters_used:
            input("Ya elegiste esta letra, PRESIONE ENTER PARA CONTINUAR")
        else:
            letters_used.append(letter_user)
            was_found = False
            for i in range(len(word_guess)):
                letter_actually = normalize(word_guess[i])
                if letter_user == letter_actually:
                    progress[i] = word_guess[i] + ' '
                    was_found = True
                    hits+=1
            if was_found == False:
                faults+=1





if __name__ == '__main__':
    run()