"""Punto 5 Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en 
el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no."""

import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, Centro, Radio):
        self.centro = Centro
        self.radio = Radio

    def Calcular_area(self):
        return math.pi * self.radio ** 2

    def Calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def Pertenecia_punto(self, punto):
        Distancia_radio = math.sqrt((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2)
        return Distancia_radio <= self.radio

def main():
    centro_circulo = Punto(2, 3)
    mi_circulo = Circulo(centro_circulo, 5)
    area = mi_circulo.Calcular_area()
    perimetro = mi_circulo.Calcular_perimetro()
    punto_fuera = Punto(10, 5)
    pertenece = mi_circulo.Pertenecia_punto(punto_fuera)
    print(f"Área del círculo: {area}")
    print(f"Perímetro del círculo: {perimetro}")
    print(f"¿El punto pertenece al círculo?: {pertenece}")
main()
