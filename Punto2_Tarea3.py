# Punto 2 Cree una clase Punto que represente un punto en el plano cartesiano.

class Punto:
    def __init__(self, Punto_x, Punto_y):
        self.Punto_x = Punto_x
        self.Punto_y = Punto_y

    def Coordenadas(self):
        print(f"Las coordenadas del punto son: ({self.Punto_x}, {self.Punto_y})")

def main():
    Punto_1 = Punto(5, 6)
    Punto_1.Coordenadas()
    Punto_2 = Punto(-6, -7)
    Punto_2.Coordenadas()
main()
