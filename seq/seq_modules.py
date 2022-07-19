#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import math
from myhdl import *
from ula.ula_modules import adder


@block
def dff(q, d, clk, rst):
    @always_seq(clk.posedge, reset=rst)
    def seq():
        q.next = d

    return instances()


@block
def blinkLedAdder(led, clk, rst):
    x = [Signal(bool(0)) for i in range(32)]
    y = [Signal(bool(0)) for i in range(32)]
    s = [Signal(bool(0)) for i in range(32)]
    c = Signal(bool(0))
    status = Signal(bool(0))

    y[0] = 1
    adder_1 = adder(x, y, s, c)

    @always_seq(clk.posedge, reset=rst)
    def seq():
        if x[24] == 0 and x[23] == 0:
            for i in range(len(x)):
                x[i].next = s[i]
            status.next = status
        else:
            for i in range(len(x)):
                x[i].next = 0
            status.next = not status

    @always_comb
    def comb():
        led.next = status

    return instances()


@block
def blinkLed(led, clk, rst):
    pass
    return instances()


@block
def barLed(leds, time_ms, dir, vel, clk, rst):
    pass
    return instances()
