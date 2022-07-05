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
        leds[0].next = sw[0]
        leds[1].next = sw[0] and sw[1]
        leds[2].next = not sw[0]
        leds[3].next = sw[0] ^ sw[1]
        for i in range(10 - 4):
            leds[i].next = 1

    return instances()
