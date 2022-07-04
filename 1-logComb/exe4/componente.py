# -*- coding: utf-8 -*-
""" Exercice 4


"""


from myhdl import *


@block
def componente(led, sw):
    @always_comb
    def comb():
        led[0].next = sw[0] and (not sw[1])

    return instances()
