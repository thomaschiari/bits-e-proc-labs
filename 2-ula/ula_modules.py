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
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]

    haList[0] = halfAdder(a, b, s[0], s[1])  # 2
    haList[1] = halfAdder(c, s[0], soma, s[2])  # 3

    @always_comb
    def comb():
        carry.next = s[1] | s[2]  # 4

    return instances()


@block
def adder2bits(x, y, soma, carry):
    c_ = [Signal(bool()) for i in range(2)]
    f0 = fullAdder(x[0], y[0], 0, soma[0], c_[0])
    f1 = fullAdder(x[1], y[1], c_[0], soma[1], carry)

    return instances()


@block
def adder(x, y, soma, carry):
    n = len(x)
    c = [Signal(bool(0)) for i in range(n + 1)]
    fa_list = [None for i in range(n)]

    for i in range(n):
        fa_list[i] = fullAdder(x[i], y[i], c[i], soma[i], c[i + 1])

    @always_comb
    def comb():
        carry.next = c[n]

    return instances()


@block
def bin2bcd(dig2, dig1, dig0, sw):
    @always_comb
    def comb():
        h2 = Signal(mobdv(0)[4:])
        h1 = Signal(mobdv(0)[4:])
        h0 = Signal(mobdv(0)[4:])

        for i in range(7):
            if h2 >= 5:
                h2 = h2 + 3
            if h1 >= 5:
                h1 = h1 + 3
            if h0 >= 5:
                h0 = h0 + 1

            h2 = h2 << 1
            h2[0] = h1[3]

            h1 = h1 << 1
            h1[0] = h0[3]

            h0 = h0 << 1
            h0[0] = sw[i]

        dig2.next = h2
        dig1.next = h1
        dig0.next = h0
