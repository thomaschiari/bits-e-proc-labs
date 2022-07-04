from myhdl import *


@block
def equacao(q, a, b, c):
    @always_comb
    def comb():
        q.next = a or (b and c)

    return instances()
