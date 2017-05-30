# -*- coding: utf-8 -*-
"""
Find the energy loss in a given system to be defined
"""

from classes import *

# Define units
um = 1./10000
mm = 1./10
cm = 1
m = 10

# Define elements
H = Element("H", "pstar/hydrogen.csv")
C = Element("C", "pstar/carbon.csv")
O = Element("O", "pstar/oxygen.csv")
Si = Element("Si", "pstar/silicon.csv")
Cu = Element("Cu", "pstar/copper.csv")
Ag = Element ("Ag", "pstar/silver.csv")
Air = Element("Air", "pstar/air.csv")
Al = Element("Al", "pstar/aluminium.csv")
W = Element("W", "pstar/tungsten.csv")

# Define densities of materials
rhoSi = 2.33
rhoAg = 5.25
rhoPCB = 3.566
rhoAir = 0.001205
rhoAl = 2.6989
rhoW = 19.3
