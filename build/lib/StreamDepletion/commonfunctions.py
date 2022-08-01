"""Shared functions"""

import numpy as np

# Hunt exf
def exf(a, b):
    c = a - b * b
    exf = 0
    if abs(a) > 170. and b <= 0:
        return exf
    if abs(c) > 170. and b >= 0:
        return exf
    if c < -170.:
        if b < 0:
            exf = 2. * np.exp(a) - exf
            return exf
    x = abs(b)
    if x > 3.:
        y = 0.5641896 / \
            (x + 0.5 / (x + 1. / (x + 1.5 / (x + 2. / (x + 2.5 / x + 1.)))))
        exf = y * np.exp(c)
        if b < 0:
            exf = 2. * np.exp(a) - exf
        return exf
    T = 1. / (1. + 0.3275911 * x)
    y = T * (0.2548296 - T * (0.2844967 - T *
                              (1.421414 - T * (1.453152 - 1.061405 * T))))
    exf = y * np.exp(c)
    if b < 0:
        exf = 2. * np.exp(a) - exf
    return exf


#Calculate aquifer diffusivity from transmissivity and storativity
def calculateDiff(transmisivity, storativity):
    return transmisivity / storativity

