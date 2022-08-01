"""Depletion with semi-pervious layer (Hantush, 1965)"""

from StreamDepletion import sd_solution as sds
import numpy as np
from StreamDepletion import commonfunctions as cf


class semipervious(sds.sd_solution_base):

    # a = dist (distance to pump)
    # D = diff (aquifer diffusivity)
    # t = time (array of time values)
    # alpha = Alpha (aquifer k / bank k * bank width)
    # alpha = 0 will return a divide by zero error
    def __init__(self, dist=0, diff=0, time=(), Alpha=0):
        super().__init__(dist, diff, time)
        self.alpha = Alpha

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._alpha = value

    def run(self):
        resp = np.empty(len(self.t))
        for i in range(len(self.t)):
            Z1 = self.a / np.sqrt(4 * self.D * self.t[i])
            Z2 = self.a / self.alpha + self.D * self.t[i] / (self.alpha ** 2)
            Z3 = Z1 + (np.sqrt(self.D * self.t[i])) / self.alpha
            resp[i] = cf.exf(0, Z1) - cf.exf(Z2, Z3)
        return resp
