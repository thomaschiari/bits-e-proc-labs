#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a & b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b ^ c
        carry.next = (a & b) | (b & c) | (a & c)

    return instances()


@block
def adder2bits(x, y, soma, carry):
    temp = Signal(bool(0))
    full1 = fullAdder(x[0], y[0], 0, soma[0], temp)
    full2 = fullAdder(x[1], y[1], temp, soma[1], carry)

    return instances()


@block
def adder(x, y, soma, carry):

    n = len(x)

    tempList = [Signal(bool(0)) for i in range(n)]

    fullAdderList = [fullAdder(x[i], y[i], tempList[i], soma[i], tempList[i+1]) for i in range(n-1)]

    @always_comb
    def comb():

        carry.next = tempList[n-1]
        

    return instances()