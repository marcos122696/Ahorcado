import os 
import random


class Search:

    def find_word():
        """Create a list of words, it's in "data.txt".
        Choose a word at random.

        Returs the chosen word.
        """
        try:
            words = []
            base_dir = os.path.dirname(os.path.realpath(__file__))
            with open(os.path.join(base_dir, 'data.txt'), "r", encoding="utf-8") as f:
                for line in f:
                    words.append(line.strip().upper())
                word = random.choice(words)
            return word 
        except:
            print("Error al buscar las palabras")


    def find_phase():
        """Create a list of words, it's in "data.txt".
        Choose a word at random.

        Returs the chosen word.
        """
        try:
            sentenses = []
            base_dir = os.path.dirname(os.path.realpath(__file__))
            with open(os.path.join(base_dir, 'sentenses.txt'), "r", encoding="utf-8") as f:
                for line in f:
                    sentenses.append(line.strip().upper().split(' '))
                phase = random.choice(sentenses)
            return phase 
        except:
            print("Error al buscar las frases")
