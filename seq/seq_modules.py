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
def blinkLedAdder(led, time_ms, clk, rst):
    ms = 50000
    x = [Signal(bool(0)) for i in range(32)]
    y = [Signal(bool(0)) for i in range(32)]
    s = [Signal(bool(0)) for i in range(32)]
    c = Signal(bool(0))
    l = Signal(bool(0))

    bit = round(math.log2(ms * time_ms))

    adder_1 = adder(x, y, s, c)

    @always_seq(clk.posedge, reset=rst)
    def seq():
        if s[bit] == 0:
            for i in range(len(x)):
                x[i].next = s[i]
            y[0].next = 1
        else:
            for i in range(len(x)):
                x[i].next = 0
                y[0].next = 0
            l.next = not l

    @always_comb
    def comb():
        led.next = l

    return instances()


@block
def blinkLed(led, time_ms, clk, rst):
    ms = 50000
    cnt = Signal(intbv(0)[32:])
    l = Signal(bool(0))

    @always_seq(clk.posedge, reset=rst)
    def seq():
        if cnt < ms * time_ms:
            cnt.next = cnt + 1
        else:
            cnt.next = 0
            l.next = not l

    @always_comb
    def comb():
        led.next = l

    return instances()


@block
def stepMotor(phases, dir, vel, clk, rst):
    cnt = Signal(intbv(0)[32:])
    top = Signal(intbv(0)[32:])
    activated = Signal(intbv(0)[4:])

    @always_seq(clk.posedge, reset=rst)
    def seq():
        if cnt <= top:
            cnt.next = cnt + 1
        else:
            cnt.next = 0
            if activated < 3:
                activated.next = activated + 1
            else:
                activated.next = 0

    @always_comb
    def comb():
        if vel:
            top.next = 5000000
        else:
            top.next = 2500000

        if dir:
            phases.next = intbv(1)[4:] << activated
        else:
            phases.next = intbv(8)[4:] >> activated

    return instances()
