# -*- coding: utf-8 -*-
""" Exercice 3

Implemente o circuito lógico a seguir:

            __
  a---------\  \
             |  |-  __
  b---------/__/  -|  \
                   |   )-
  c----------------|__/  -  __
                          -|  \
                           |   )-
  d------------------------|__/  -  __
                                  -|  \
                                   |   )-----
  e--------------------------------|__/
"""


from myhdl import *


@block
def equacao(q, a, b, c, d, e):
    @always_comb
    def comb():
        q.next = (a or b) and c and d and e

    return instances()
