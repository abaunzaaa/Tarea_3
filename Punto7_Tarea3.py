"""Punto 7 Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. 
Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros."""

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

def main():
    CuentaA = CuentaBancaria("1027945678", ["Angie Diaz", "Daniela Hernandez"], 1000.0)
    print(f"El número de cuenta es {CuentaA.numero_cuenta}, los propietarios son {CuentaA.propietarios} y el balance es {CuentaA.balance} USD")
main()    