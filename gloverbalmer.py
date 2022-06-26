""" Depletion in semi-infinite aquifer with fully penetrating stream (Glover and Balmer, 1954) """

from scipy import special as special
import numpy as np
import sd_solution


class gloverbalmer(sd_solution.sd_solution):

    # a = dist (distance to pump)
    # D = diff (aquifer diffusivity)
    # t = time (array of time values)
    def __init__(self, dist=0, diff=0, time=()):
        super(self.__class__, self).__init__(dist, diff, time)

    def run(self):
        return special.erfc(self.a / np.sqrt(4 * self.D * self.t))
