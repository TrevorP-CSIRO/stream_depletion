""" Depletion in semi-confined aquifer (Hunt, 2003) """

from StreamDepletion import sd_solution as sds
import numpy as np


class semiconfined(sds.sd_solution_base):

    # t = time (array of time values)
    # k = nondim_k (L**2 / aquifer_transmisivity * Cond_aquitard / Sat_aquitard_thick)
    # eps = epsilon
    # lam = lambd (
    def __init__(self, time=(), nondim_k=0, epsilon=0, lambd=0):
        self.t = time
        self.k = nondim_k
        self.eps = epsilon
        self.lam = lambd

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, value):
        self._k = value

    @property
    def eps(self):
        return self._eps

    @eps.setter
    def eps(self, value):
        self._eps = value

    @property
    def lam(self):
        return self._lam

    @lam.setter
    def lam(self, value):
        self._lam = value

    def run(self):
        resp = np.empty(len(self.t))
        factor = np.zeros(16)
        factor[0] = -3.96825396825397E-04
        factor[1] = 2.13373015873016
        factor[2] = -551.016666666667
        factor[3] = 33500.1611111111
        factor[4] = -812665.111111111
        factor[5] = 10076183.7666667
        factor[6] = -73241382.9777778
        factor[7] = 339059632.073016
        factor[8] = -1052539536.27857
        factor[9] = 2259013328.58333
        factor[10] = -3399701984.43333
        factor[11] = 3582450461.7
        factor[12] = -2591494081.36667
        factor[13] = 1227049828.76667
        factor[14] = -342734555.428571
        factor[15] = 42841819.4285714
        for j in range(len(self.t)):
            a = 0.693147180559945 / self.t[j]
            sum = 0
            for i in range(16):
                b = a * (i+1)
                u1 = b + self.eps * self.k
                u2 = u1 + self.k
                Top = b * u2
                m0 = np.sqrt(Top / u1)
                u3 = self.lam + 2 * m0
                u4 = b * u3
                D = np.exp(-m0)
                e = self.lam * D / u4
                f = e * factor[i]
                sum = sum + f
            resp[j] = sum * a
        return resp
