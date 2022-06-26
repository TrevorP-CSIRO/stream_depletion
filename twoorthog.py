""" Depletion in aquifer with two orthogonal rivers (Hantush, 1967) """

import sd_solution
import numpy as np
from scipy import special as special


class twoorthog(sd_solution.sd_solution):

    # a = dist (distance to pump)
    # D = diff (aquifer diffusivity)
    # t = time (array of time values)
    # L_sec_river = L (distance to second river)
    def __init__(self, dist=0, diff=0, time=(), L_sec_river=0):
        super().__init__(dist, diff, time)
        self.L = L_sec_river

    @property
    def L(self):
        return self._L

    @L.setter
    def L(self, value):
        self._L = value

    def run(self):
        resp = np.empty(len(self.t))
        for i in range(len(self.t)):
            Z = 2 * np.sqrt(self.D * self.t[i])
            resp[i] = 1-special.erf(self.a/Z)*special.erf(self.L/Z)
        return resp
