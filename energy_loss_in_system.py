# -*- coding: utf-8 -*-
"""
Find the energy loss in a given system to be defined.
"""

from classes import *
from init import *

# Define materials
sensor = Material("sensor", rhoSi)
sensor.addElement(Si)
sensor.setThickness(120*um)

glue = Material("sensor", rhoAg)
glue.addElement(Ag)
glue.setThickness(80*um)

PCB = Material("PCB", rhoPCB)
PCB.addElement(H, 0.1502)
PCB.addElement(C, 0.1423)
PCB.addElement(O, 0.3910)
PCB.addElement(Si, 0.1836)
PCB.addElement(Cu, 0.1329)
PCB.setThickness(160*um)

air = Material("Air", rhoAir)
air.addElement(Air)
air.setThickness(4*mm)

absorberAl = Material("Al", rhoAl)
absorberAl.addElement(Al)
absorberAl.setThickness(15.5*mm)

absorberW = Material("W", rhoW)
absorberW.addElement(W)
absorberW.setThickness(3.3*mm)

DTC = System()
DTC.addMaterial(sensor)
DTC.addMaterial(glue)
DTC.addMaterial(PCB)
DTC.addMaterial(air)
DTC.addMaterial(absorberAl)

DTCW = System()
DTCW.addMaterial(sensor)
DTCW.addMaterial(glue)
DTCW.addMaterial(PCB)
DTCW.addMaterial(air)
DTCW.addMaterial(absorberW)

print("The energy loss in a 15.5 mm Al layer @ 100 (200) MeV proton is {:.2f} ({:.2f}) MeV.".format(DTC.getStoppingPower(100), DTC.getStoppingPower(200)))
print("The energy loss in a 3.3 mm W layer @ 100 (200) MeV proton is {:.2f} ({:.2f}) MeV.".format(DTCW.getStoppingPower(100), DTCW.getStoppingPower(200)))
