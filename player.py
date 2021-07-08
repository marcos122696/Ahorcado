import os

class Player:
    nombre = str
    pts = int

    def __init__(self, nombre, pts=0):
        self.nombre = nombre
        self.pts = pts


    @property
    def pts(self):
        return self.pts


    @pts.setter
    def more_pts(self, pts_win):
        self.pts += pts_win

    
    def save_player():
        try:
            name_player = input("Ingrese el nombre del jugador: ")
            base_dir = os.path.dirname(os.path.realpath(__file__))
            with open(os.path.join(base_dir, 'player.txt'), "a", encoding="utf-8") as f:
                for line in f:
                    line.write(name_player)
        except:
            print("Error al guardar jugador")

if __name__ == '__main__':
    Player.save_player()