"""Punto 11 Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por 
consola los detalles de la cuenta bancaria."""

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def Acciones_deposito(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Se ha depositado {monto} en la cuenta.")
        else:
            print("El monto del depósito debe ser mayor que cero.")

    def retirar(self, monto):
        if 0 < monto <= self.balance:
            self.balance -= monto
            print(f"Se ha retirado {monto} USD de la cuenta.")
        else:
            print("El monto del retiro debe ser mayor que cero y no puede sobrepasar el balance disponible.")

    def Cuota_manejo(self):
        cuota_manejo = self.balance * 0.02
        self.balance -= cuota_manejo
        print(f"Se ha aplicado una cuota de manejo del 2%: {cuota_manejo}")

    def mostrar_detalles(self):
        print("Detalles de la cuenta:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance}")

def main():
    CuentaA = CuentaBancaria("1234567890", ["Angie Diaz", "Daniela Hernandez"], 1000.0)
    CuentaA.mostrar_detalles()
    CuentaA.Acciones_deposito(500.0)
    CuentaA.mostrar_detalles()
    CuentaA.Cuota_manejo()
    CuentaA.mostrar_detalles()
main()