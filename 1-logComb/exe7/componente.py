# -*- coding: utf-8 -*-
""" Exercice 7

Considere que as chaves SW3..SW0
formam um vetor que indica um número
em binário. Exiba esse número no display
de 7s.

Você deve editar o "....." para corresponder
ao valor correto. Apenas o número 1 está certo.

Uma outra alternativa a implementacao seria a de
encontrarmos para cada um dos segmentos uma equacao:

hex0[0].next = sw[0] and ....
hex0[1].next = sw[0] and not ....

"""


from myhdl import *


@block
def componente(hex0, sw):
    @always_comb
    def comb():
        if sw[4:0] == 0:
            hex0.next = "1000000"
        elif sw[4:0] == 1:
            hex0.next = "1111001"
        elif sw[4:0] == 2:
            hex0.next = "0100100"
        elif sw[4:0] == 3:
            hex0.next = "0110000"
        elif sw[4:0] == 4:
            hex0.next = "0011001"
        elif sw[4:0] == 5:
            hex0.next = "0010010"
        elif sw[4:0] == 6:
            hex0.next = "0000010"
        elif sw[4:0] == 7:
            hex0.next = "1111000"
        elif sw[4:0] == 8:
            hex0.next = "0000000"
        elif sw[4:0] == 9:
            hex0.next = "0011000"
        elif sw[4:0] == 10:
            hex0.next = "0001000"
        elif sw[4:0] == 11:
            hex0.next = "0000011"
        elif sw[4:0] == 12:
            hex0.next = "1000110"
        elif sw[4:0] == 13:
            hex0.next = "0100001"
        elif sw[4:0] == 14:
            hex0.next = "0000110"
        else:
            hex0.next = "0001110"

    return instances()
