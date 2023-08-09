# Punto 1 Cree una clase vehiculo que contenga los atributos de instancia velocidad_máxima y kilometraje

class Vehículo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

    def acelerar(self, incremento):
        if self.velocidad_maxima + incremento >= 0:
            self.velocidad_maxima += incremento
        else:
            print("La velocidad no se puede reducir más de 0.")

    def mostrar_informacion(self):
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")
        print(f"Kilometraje: {self.kilometraje} km")

def main():
    mi_auto = Vehículo(200, 50000)
    mi_auto.mostrar_informacion()
    mi_auto.acelerar(30)
    mi_auto.mostrar_informacion()
main()    