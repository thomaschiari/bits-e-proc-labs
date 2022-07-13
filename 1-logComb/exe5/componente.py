# -*- coding: utf-8 -*-
""" Exercice 5

Faća com que:

- LED[0]: Aciona quando chave SW[0] on
- LED[1]: Acione somente quando SW[1] e SW[0] estiverem on
- LED[2]: Oposto do LED[0]
- LED[3]: Aciona quando SW[1] e SW[0] forem diferentes
- LED[10:4]: On sempre
    TIP: utilize um for acessando os elementos do LED.
"""


from myhdl import *


@block
def componente(leds, sw):
    @always_comb
    def comb():
        pass

    return instances()
