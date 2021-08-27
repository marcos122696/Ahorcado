import os

class Player:

    def __init__(self, name, pts=0):
        self.name = name
        self.pts = pts

    @property
    def get_pts(self):
        return self.pts

    @set
    def set_pts(self, pts):
        self.pts += pts

    
    def save_player(self, player):
        points = str(player.pts)
        try:
            with open(os.path.abspath('player.txt'), "a", encoding="utf-8") as f:
                f.write(player.name + " " + points + "\n")
                f.close()
        except:
            print("Error al guardar jugador")

if __name__ == '__main__':
    name = input("Igrese el nombre del jugador: ")
    new_player = Player(name)
    # name_player = new_player.name
    new_player.save_player(new_player)