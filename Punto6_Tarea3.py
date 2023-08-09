"""Punto 6 Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción 
del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta."""

class Carta:
    Pintas_Cartas = ('Diamante', 'Pica', 'Trébol', 'Corazón')

    def __init__(self, Valor_Carta, Pinta_Carta):
        self.valor = Valor_Carta
        self.pinta = Pinta_Carta

def main():
    mi_carta = Carta(7, Carta.Pintas_Cartas[1])
    print(f"La pinta de la carta es {mi_carta.pinta} y el valor de la carta es {mi_carta.valor}")
main()