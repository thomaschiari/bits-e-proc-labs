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
        carry.next = a and b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):

    s = [Signal(bool(0)) for i in range(3)]

    half_1 = halfAdder(a, b, s[0], s[1])  # 2
    half_2 = halfAdder(c, s[0], soma, s[2])  # 3

    @always_comb
    def comb():
        carry.next = s[1] | s[2]  # 4

    return instances()


@block
def adder2bits(x, y, s, carry):
    x_ = [x(i) for i in range(2)]
    y_ = [y(i) for i in range(2)]
    c_ = [Signal(bool(0)) for i in range(2)]
    s_ = [Signal(bool(0)) for i in range(2)]
    s_out = ConcatSignal(*reversed(s_))

    f0 = fullAdder(x_[0], y_[0], 0, s_[0], c_[0])
    f1 = fullAdder(x_[1], y_[1], c_[0], s_[1], carry)

    @always_comb
    def comb():
        s.next = s_out

    return instances()


@block
def adder(x, y, s, carry):
    x_ = [x(i) for i in range(2)]
    y_ = [y(i) for i in range(2)]
    c_ = [Signal(bool()) for i in range(2)]
    s_ = [Signal(bool()) for i in range(2)]
    s_out = ConcatSignal(*reversed(s_))

    f0 = halfAdder(x_[0], y_[0], s_[0], c_[0])
    f1 = fullAdder(x_[1], y_[1], c_[0], s_[1], carry)

    @always_comb
    def comb():
        s.next = s_out

    return instances()


@block
def run():
    x = Signal(intbv(0)[2:])
    y = Signal(intbv(0)[2:])
    s = Signal(intbv(0))
    carry = Signal(intbv(0))

    dut = adder(x, y, s, carry)

    @instance
    def stimulus():
        x.next = int(input("x="))
        y.next = int(input("y="))
        yield delay(1)
        print("x:%s y:%s soma:%s carry:%s" % (bin(x, 2), bin(y, 2), bin(s, 2), carry))

    return instances()


tb = run()
tb.run_sim()
