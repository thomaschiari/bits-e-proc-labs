# -*- coding: utf-8 -*-

from myhdl import *
from ula_modules import *


def test_dff():
    @instance
    def stimulus():
        for i in range(4):
            t = bin(i, 2)
            a.next = bool(int(t[0]))
            b.next = bool(int(t[1]))
            yield delay(1)
            # print("{} {} {} {}".format(a, b, soma, vaiUm))
            assert soma == (a ^ b)
            assert vaiUm == (a and b)

    a = Signal(bool(0))
    b = Signal(bool(0))
    soma = Signal(bool(0))
    vaiUm = Signal(bool(0))
    dut = halfAdder(a, b, soma, vaiUm)
    sim = Simulation(dut, stimulus)
    sim.run()
