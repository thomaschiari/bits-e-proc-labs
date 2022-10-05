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
def contador(leds, clk, rst):

    @always_seq(clk.posedge, reset=rst)
    def seq():
        pass

    return instances()


@block
def blinkLed(led, clk, rst):
    cnt = Signal(intbv(0)[32:])
    l = Signal(bool(0))

    @always_seq(clk.posedge, reset=rst)
    def seq():
        if cnt < 25000000:
            cnt.next = cnt + 1
        else:
            cnt.next = 0
            l.next = not l

    @always_comb
    def comb():
        led.next = l

    return instances()


@block
def barLed(leds, clk, rst):
    @always_seq(clk.posedge, reset=rst)
    def seq():
        pass

    return instances()


@block
def barLed2(leds, clk, rst):
    @always_seq(clk.posedge, reset=rst)
    def seq():
        pass

    return instances()
