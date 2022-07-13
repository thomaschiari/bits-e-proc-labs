# -*- coding: utf-8 -*-

from myhdl import *
from componentes import fullAdder


def test_fullAdder():
    @instance
    def stimulus():
        for i in range(2**3):
            t = bin(i, 3)
            a.next = bool(int(t[0]))
            b.next = bool(int(t[1]))
            c.next = bool(int(t[2]))
            yield delay(1)
            assert soma == a ^ b ^ c
            assert vaiUm == (a and b) or (a and c) or (c and b)

    a = Signal(bool(0))
    b = Signal(bool(0))
    c = Signal(bool(0))
    soma = Signal(bool(0))
    vaiUm = Signal(bool(0))
    dut = fullAdder(a, b, c, soma, vaiUm)
    sim = Simulation(dut, stimulus)
    sim.run()
