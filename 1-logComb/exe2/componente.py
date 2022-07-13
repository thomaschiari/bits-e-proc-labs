# -*- coding: utf-8 -*-
"""Exercice 1

Implemente a tabela verdade a seguir:

A B C | Q
------|--
0 0 0 | 1
0 0 1 | 0
0 1 0 | 0
0 1 1 | 1
1 0 0 | 1
1 0 1 | 0
1 1 0 | 0
1 1 1 | 1

Não utilize IF!
"""


from myhdl import *


@block
def equacao(q, a, b, c):
    @always_comb
    def comb():
        pass

    return instances()
