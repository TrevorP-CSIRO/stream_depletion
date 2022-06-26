""" Depletion in aquifer with 3 orthogonal rivers """

import sd_solution
import numpy as np
from scipy import special
from scipy.special import erf


class threeorthog(sd_solution.sd_solution):

    # a = dist (distance to pump)
    # D = diff (aquifer diffusivity)
    # t = time (array of time values)
    # L_sec_river = L2 (distance to second river)
    # L_3rd_river = L3 (distance to third river)
    def __init__(self, dist=0, diff=0, time=(), L_sec_river=0, L_3rd_river=0):
        super().__init__(dist, diff, time)
        self.L2 = L_sec_river
        self.L3 = L_3rd_river

    @property
    def L2(self):
        return self._L2

    @L2.setter
    def L2(self, value):
        self._L2 = value

    @property
    def L3(self):
        return self._L3

    @L3.setter
    def L3(self, value):
        self._L3 = value

    def run(self):
        resp = np.empty(len(self.t))
        for i in range(len(self.t)):
            Z = 2 * np.sqrt(self.D * self.t[i])
            resp[i] = 1-special.erf(self.a/Z) * \
                special.erf(self.L2/Z)*special.erf(self.L3/Z)
        return resp
