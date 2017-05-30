# -*- coding: utf-8 -*-
"""
Find the energy loss in a given system to be defined
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

um = 1./10000
mm = 1./10
cm = 1
m = 10

class Element:
    def __init__(self, name, filename):
        self.name = name
        self.filename = filename
        self.stopping_powers = False
        self.readFile()
        
    def readFile(self):
        """Read from CSV file and create a spline of stopping power values."""
        
        csv = open(self.filename, "r")
        energy, stopping_power = [], []
        for line in csv:
            line_split = [float(x) for x in line.strip().split(" ")]
            energy.append(line_split[0])
            stopping_power.append(line_split[1])
        
        self.stopping_powers = interp1d(energy, stopping_power)
        
    def getStoppingPower(self, energy):
        """Returns the stopping power in MeV cm2 / g."""
        
        return self.stopping_powers(energy)
        
class Material:
    def __init__(self, name, rho):
        self.name = name
        self.rho = rho
        self.elements = []
        self.thickness = False
    
    def addElement(self, element, fraction = 1):
        self.elements.append([element, fraction])
    
    def setThickness(self, thickness):
        """In cm."""
        
        self.thickness = thickness
    
    def getStoppingPower(self, energy):
        """Returns stopping power in terms of MeV (if thickness is defined)."""
        stopping_power = 0

        if not self.elements:
            raise Exception("Material {} has no defined elements!".format(self.name))
        
        for element, fraction in self.elements:
            stopping_power += element.getStoppingPower(energy) * fraction
        
        # Convert from MeV cm2 / g to MeV / cm        
        stopping_power *= self.rho
        
        # Convert from MeV / cm to MeV
        if self.thickness:
            stopping_power *= self.thickness
        
        return stopping_power

class System:
    def __init__(self):
        self.system = []

    def addMaterial(self, material):
        self.system.append(material)

    def getStoppingPower(self, energy):
        sum_stopping_power = 0
        for material in self.system:
            if not material.thickness:
                raise Exception("Material \"{}\" needs a defined thickness!".format(material.name))
                
            sum_stopping_power += material.getStoppingPower(energy - sum_stopping_power)
            
            if sum_stopping_power < 0:
                return 0

        return sum_stopping_power
