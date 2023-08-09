"""Punto 3 A la clase del punto anterior, defínale los siguientes métodos:
- Un método mostrar que imprima por consola las coordenadas del punto
- Un método mover que cambie las coordenadas del punto
- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto."""

import math

class Punto:
    def __init__(self, Punto_x, Punto_y):
        self.x = Punto_x
        self.y = Punto_y

    def Mostrar_Coordenadas(self):
        print(f"Las coordenadas del punto son: ({self.x}, {self.y})")

    def Mover_Coordenadas(self, Punto2_x, Punto2_y):
        self.x = Punto2_x
        self.y = Punto2_y

    def calcular_distancia(self, Nuevo_punto):
        distancia = math.sqrt((self.x - Nuevo_punto.x) ** 2 + (self.y - Nuevo_punto.y) ** 2)
        return distancia

def main():
    Punto_1 = Punto(3, 5)
    Punto_1.Mostrar_Coordenadas()
    Punto_1.Mover_Coordenadas(7, 2)
    Punto_1.Mostrar_Coordenadas()
    Punto_2 = Punto(-2, 7)
    Punto_2.Mostrar_Coordenadas()
    distancia = Punto_1.calcular_distancia(Punto_2)
    print(f"La distancia entre el punto 1 y el punto 2 es: {distancia}")
main()    
