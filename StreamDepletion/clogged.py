""" Depletion for clogged partially penetrating stream (Hunt, 1999) """

import numpy as np
from scipy import special
from scipy.special import erfc
from StreamDepletion import sd_solution as sds
from StreamDepletion import commonfunctions as cf


class clogged(sds.sd_solution_base):
    # a = dist (distance to pump)
    # D = diff (aquifer diffusivity)
    # t = time (array of time values)
    # lam = lambd (constant of proportionality between the seepage flow rate per unit distance
    #             (in the y direction) through the streambed and the difference between the river
    #             and groundwater levels at x=0
    # As lambd approaches infinity the solution converges back to the Glover & Balmer solution
    # ph = phi (specific yield)

    def __init__(self, dist=0, diff=0, time=(), lambd=0, phi=0):
        super().__init__(dist, diff, time)
        self.lam = lambd
        self.ph = phi

    @property
    def lam(self):
        return self._lam

    @lam.setter
    def lam(self, value):
        self._lam = value

    @property
    def ph(self):
        return self._ph

    @ph.setter
    def ph(self, value):
        self._ph = value

    def run(self):
        resp = np.empty(len(self.t))
        Tr = self.D * self.ph
        for i in range(len(self.t)):
            Z1 = self.a / np.sqrt(4 * self.D * self.t[i])
            Z2 = self.lam ** 2 * self.t[i] / 4 / \
                self.ph / Tr + self.lam * self.a / 2 / Tr
            Z3 = np.sqrt(self.lam ** 2 * self.t[i] / 4 / self.ph / Tr) + np.sqrt(
                self.ph * self.a ** 2 / 4 / self.t[i] / Tr)
            resp[i] = cf.exf(0, Z1) - cf.exf(Z2, Z3)
        return resp
