from myhdl import *
from equacao import *


def test_equacao():
    @instance
    def stimulus():
        a.next = 0
        b.next = 1
        c.next = 1
        yield delay(1)
        assert q == 1

    q = Signal(bool(0))
    a = Signal(bool(0))
    b = Signal(bool(0))
    c = Signal(bool(0))
    dut = equacao(q, a, b, c)
    sim = Simulation(dut, stimulus)
    sim.run()
