from search import Search
from graphics import Graphics
import os

class Level:

    def __init__(self):
        pass

    def normalize(char):
        """Receives an accented vowel and returns it without an accent.

        Param String "char" vocal.
        Returns la vocal sin acento.
        """
        dic_word = char.maketrans('ÁÉÍÓÚ', 'AEIOU')
        new_char = char.translate(dic_word)
        return new_char


    def lvl1(faults, hits):
        word_guess = Search.find_word()  
        progress = ["_ " for i in range(len(word_guess))]
        letters_used = []

        while faults <= 7:
            os.system('cls')
            print("¡Adivina la palabra!")
            Graphics.fail(faults)

            if faults == 7:
                print(f'La palabra era: {chr(27) + "[2;32m"} {"".join(word_guess)} {chr(27) + "[0m"}')
                break

            if hits == len(word_guess):
                Graphics.win(faults)
                print(f'La palabra era: {chr(27) + "[2;32m"} {"".join(word_guess)} {chr(27) + "[0m"}')
                break
            
            print(''.join(progress))
            print(chr(27) + "[1;35m" + 'Letras usadas: ', ', '.join(letters_used) + chr(27) + "[0m")

            try:
                letter_user = Level.normalize(input("Elije una letra: ").strip().upper())
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
                    letter_actually = Level.normalize(word_guess[i])
                    if letter_user == letter_actually:
                        progress[i] = word_guess[i] + ' '
                        was_found = True
                        hits+=1
                if was_found == False:
                    faults+=1


    def lvl2(faults, hits):
        sentense_guess = Search.find_phase()
        sentense_win = 0
        progress = []
        for i in range(len(sentense_guess)):
            for j in range(len(sentense_guess[i])):
                progress.append('_ ')
                sentense_win+=1
            progress.append('  ')
        letters_used = []
        
        while faults <= 7:
            os.system('cls')
            print("¡Adivina la palabra!")
            Graphics.fail(faults)

            if faults == 7:
                print(f'La frase era: {chr(27) + "[2;32m"} {" ".join(sentense_guess)} {chr(27) + "[0m"}')
                break
            if hits == sentense_win:
                Graphics.win(faults)
                print(f'La frase era: {chr(27) + "[2;32m"} {" ".join(sentense_guess)} {chr(27) + "[0m"}')
                break

            print(''.join(progress))
            print(chr(27) + "[1;35m" + 'Letras usadas: ', ', '.join(letters_used) + chr(27) + "[0m")
            
            try:
                letter_user = Level.normalize(input("Elije una letra: ").strip().upper())
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
                iterator = 0
                for i in range(len(sentense_guess)):
                    for j in range(len(sentense_guess[i])):
                        if letter_user == Level.normalize(sentense_guess[i][j]):
                            progress[iterator] = sentense_guess[i][j] + " "
                            was_found = True
                            hits+=1
                        iterator+=1
                    iterator+=1
                if was_found == False:
                    faults+=1
                iterator = 0