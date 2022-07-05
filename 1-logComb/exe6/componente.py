# -*- coding: utf-8 -*-
""" Exercice 6
Faca com que cada segmento do display HEX0
seja controlado por uma das chaves SW.

Utilize um for para isso!

tip: len(hex0) retorna o tamanho de HEX0

Utilizando as chaves exiba o digito 2
"""


from myhdl import *


@block
def componente(hex0, sw):
    @always_comb
    def comb():
        for i in range(len(hex0)):
            hex0[i].next = sw[i]

    return instances()
