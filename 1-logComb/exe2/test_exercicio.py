# -*- coding: utf-8 -*-

from myhdl import *
from exercicio import *

vec = [
    "0001",
    "0010",
    "0100",
    "0111",
    "1001",
    "1010",
    "1100",
    "1111",
]


def test_exercicio():
    @instance
    def stimulus():
        for t in vec:
            a.next = bool(int(t[0]))
            b.next = bool(int(t[1]))
            c.next = bool(int(t[2]))
            yield delay(1)
            assert q == bool(int(t[3]))

    q = Signal(bool(0))
    a = Signal(bool(0))
    b = Signal(bool(0))
    c = Signal(bool(0))
    dut = equacao(q, a, b, c)
    sim = Simulation(dut, stimulus)
    sim.run()
