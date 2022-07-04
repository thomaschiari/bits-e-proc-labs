# -*- coding: utf-8 -*-

from myhdl import *
from componente import *


def test_exercicio():
    @instance
    def stimulus():
        for i in range(2**5 - 1):
            t = bin(i, 5)
            a.next = bool(int(t[0]))
            b.next = bool(int(t[1]))
            c.next = bool(int(t[2]))
            d.next = bool(int(t[3]))
            e.next = bool(int(t[4]))
            yield delay(1)
            assert q.val == ((a or b) and c and d and e).val

    q = Signal(bool(0))
    a = Signal(bool(0))
    b = Signal(bool(0))
    c = Signal(bool(0))
    d = Signal(bool(0))
    e = Signal(bool(0))
    dut = equacao(q, a, b, c, d, e)
    sim = Simulation(dut, stimulus)
    sim.run()
