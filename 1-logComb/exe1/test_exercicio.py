# -*- coding: utf-8 -*-

from myhdl import *
from exercicio import *


def test_exercicio():
    @instance
    def stimulus():
        for i in range(4):
            t = bin(i, 2)
            a.next = bool(int(t[0]))
            b.next = bool(int(t[1]))
            yield delay(1)
            assert q == (a or (not b))

    q = Signal(bool(0))
    a = Signal(bool(0))
    b = Signal(bool(0))
    dut = equacao(q, a, b)
    sim = Simulation(dut, stimulus)
    sim.run()
