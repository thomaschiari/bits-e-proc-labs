#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from myhdl import *
from componentes import *


@block
def toplevel(LEDR, SW, KEY, HEX0, HEX1, HEX2, HEX3, HEX4, HEX5):
    sw = [SW(i) for i in range(10)]
    key = [KEY(i) for i in range(10)]
    ledr_ = [Signal(bool()) for i in range(10)]
    hex0_ = [Signal(bool()) for i in range(7)]
    hex1_ = [Signal(bool()) for i in range(7)]
    hex2_ = [Signal(bool()) for i in range(7)]
    hex3_ = [Signal(bool()) for i in range(7)]
    hex4_ = [Signal(bool()) for i in range(7)]
    hex5_ = [Signal(bool()) for i in range(7)]

    # --=======================================--
    # INSTANCE
    # --=======================================--
    ic1 = halfAdder(sw[0], sw[0], ledr_[1], ledr_[0])

    @always_comb
    def comb():
        for i in range(len(ledr_)):
            LEDR[i].next = ledr_[i]

        for i in range(len(hex0_)):
            HEX0[i].next = hex0_[i]
            HEX1[i].next = hex1_[i]
            HEX2[i].next = hex2_[i]
            HEX3[i].next = hex3_[i]
            HEX4[i].next = hex4_[i]
            HEX5[i].next = hex5_[i]

    return instances()


LEDR = Signal(intbv(0)[10:])
SW = Signal(intbv(0)[10:])
KEY = Signal(intbv(0)[4:])
HEX0 = Signal(intbv(1)[7:])
HEX1 = Signal(intbv(1)[7:])
HEX2 = Signal(intbv(1)[7:])
HEX3 = Signal(intbv(1)[7:])
HEX4 = Signal(intbv(1)[7:])
HEX5 = Signal(intbv(1)[7:])
top = toplevel(LEDR, SW, KEY, HEX0, HEX1, HEX2, HEX3, HEX4, HEX5)
top.convert(hdl="VHDL")
