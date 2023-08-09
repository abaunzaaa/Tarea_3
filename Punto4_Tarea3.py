""" Punto 4 Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. 
Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado."""

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectángulo:
    def __init__(self, Punto_1, Punto_2):
        self.Esquina_sup_izq = Punto_1
        self.Esquina_inf_der = Punto_2

    def Calcular_lado(self):
        return abs(self.Esquina_inf_der.x - self.Esquina_sup_izq.x)

    def Calcular_altura(self):
        return abs(self.Esquina_inf_der.y - self.Esquina_sup_izq.y)

    def Calcular_perímetro(self):
        lado = self.Calcular_lado()
        altura = self.Calcular_altura()
        return 2 * (lado + altura)

    def Calcular_area(self):
        lado = self.Calcular_lado()
        altura = self.Calcular_altura()
        return lado * altura

    def Comprobar_Cuadrado(self):
        lado = self.Calcular_lado()
        altura = self.Calcular_altura()
        return lado == altura
    
def main():
    Primera_Esquina = Punto(2, 5)
    Segunda_Esquina = Punto(6, 3)
    Rectangulo1 = Rectángulo(Primera_Esquina, Segunda_Esquina)
    Perímetro = Rectangulo1.Calcular_perímetro()
    Área = Rectangulo1.Calcular_area()
    Comprobar_Cuadrado = Rectangulo1.Comprobar_Cuadrado()
    print(f"El perímetro del rectángulo es: {Perímetro}")
    print(f"El área del rectángulo es: {Área}")
    print(f"¿El rectángulo es un cuadrado?: {Comprobar_Cuadrado}")
main()    