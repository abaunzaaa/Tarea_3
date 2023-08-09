"""Punto 9 para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta."""

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
            print(f"Se ha retirado {monto} de la cuenta.")
        else:
            print("El monto del retiro debe ser mayor que cero y no puede sobrepasar el balance disponible.")

def main():
    CuentaA = CuentaBancaria("1234567890", ["Angie Diaz", "Daniela Hernandez"], 1000.0)
    print(f"El número de cuenta es: {CuentaA.numero_cuenta}")
    print(f"Los propietarios son: {CuentaA.propietarios}")
    print(f"El balance inicial es: {CuentaA.balance}")
    CuentaA.Acciones_deposito(500.0)
    print(f"El balance después del depósito es: {CuentaA.balance}")
    CuentaA.retirar(300.0)
    print(f"El balance después del retiro es: {CuentaA.balance}")
main()
