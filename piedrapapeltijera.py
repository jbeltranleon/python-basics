#!/usr/bin/env python
# -*-coding:utf-8-*-
import time
from time import sleep
import random

sus="-"*35
depo=["piedra","papel","tijera"]
while True:
    x=raw_input("piedra , papel, tijera: ")
    if x not in depo:
        print ("No hagas trampa!")
        continue

    pc=random.choice(depo)
    sleep(0.5)
    print (("Computadora elijio {}.").format(pc))
    if x==pc:
        sleep(0.5)
        print (("\nEmpate.\n{}").format(sus))
    elif x=="piedra" and pc=="tijera":
        sleep(0.5)
        print (("\nGanaste.piedra gana tijera\n{}").format(sus))
    elif x=="papel" and pc=="piedra":
        sleep(0.5)
        print (("\nGanaste.papel gana roca\n{}").format(sus))
    elif x=="tijera" and pc=="papel":
        sleep(0.5)
        print (("\nGanaste.tijera gana papel\n{}").format(sus))
    else:
        sleep(0.5)
        print (("\nPerdiste. {} gana {}\n{}").format(pc,x,sus))
input()