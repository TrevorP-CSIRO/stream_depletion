"""Base class for all solutions"""

import numpy as np


class sd_solution_base():

    # dist = distance from stream to pump (a)
    # diff = aquifer diffusivity (D)
    # time = python list of timesteps (t)
    def __init__(self, dist=0, diff=0, time=()):
        self.a = dist
        self.D = diff
        self.t = np.asarray(time)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def D(self):
        return self._D

    @D.setter
    def D(self, value):
        self._D = value

    @property
    def t(self):
        return self._t

    @t.setter
    def t(self, values):
        self._t = np.asarray(values)

    def run():
        pass
