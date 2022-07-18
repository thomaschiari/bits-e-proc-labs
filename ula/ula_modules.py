#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    s = Signal(bool())
    c = Signal(bool())

    @always_comb
    def comb():
        s = a ^ b
        c = a & b

        soma.next = s
        carry.next = c

        # print("a: %s b: %s | s: %s c: %s" % (bin(a), bin(b), bin(s), bin(c)))

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
def bin2bcdAdd3(din, dout):
    # implements with LUT
    @always_comb
    def comb():
        if din == 0:
            dout.next = 0
        elif din == 1:
            dout.next = 1
        elif din == 2:
            dout.next = 2
        elif din == 3:
            dout.next = 3
        elif din == 4:
            dout.next = 4
        elif din == 5:
            dout.next = 8
        elif din == 6:
            dout.next = 9
        elif din == 7:
            dout.next = 10
        elif din == 8:
            dout.next = 11
        elif din == 9:
            dout.next = 12
        else:
            dout.next = 0

    return instances()


@block
def bin2bcd(dig2, dig1, dig0, din):

    c1, c2, c3, c4, c5, c6, c7 = [Signal(intbv()[4:]) for i in range(7)]

    d1 = ConcatSignal(Signal(bool(0)), din[7:5])
    d2 = ConcatSignal(c1[2:0], din[4])
    d3 = ConcatSignal(c2[2:0], din[3])
    d4 = ConcatSignal(c3[2:0], din[2])
    d5 = ConcatSignal(c4[2:0], din[1])
    d6 = ConcatSignal(Signal(bool(0)), c1[3], c2[3], c3[3])
    d7 = ConcatSignal(c6[2:0], c4[3])

    add1 = bin2bcdAdd3(d1, c1)
    add2 = bin2bcdAdd3(d2, c2)
    add3 = bin2bcdAdd3(d3, c3)
    add4 = bin2bcdAdd3(d4, c4)
    add5 = bin2bcdAdd3(d5, c5)
    add6 = bin2bcdAdd3(d6, c6)
    add7 = bin2bcdAdd3(d7, c7)

    dig2 = ConcatSignal(c5[2:0], din[0])
    dig1 = ConcatSignal(c7[2:0], c5[3])
    dig0 = ConcatSignal(c6[3], c7[3])

    @always_comb
    def comb():
        print("d5:")
        print(bin(d5, 8))
        print(bin(d5[2:0], 3))
        print(bin(din[0], 1))

    return instances()
