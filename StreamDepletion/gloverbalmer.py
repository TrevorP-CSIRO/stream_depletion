""" Depletion in semi-infinite aquifer with fully penetrating stream (Glover and Balmer, 1954) """

from scipy import special as special
import numpy as np
from StreamDepletion import sd_solution as sds


class gloverbalmer(sds.sd_solution_base):

    # a = dist (distance to pump)
    # D = diff (aquifer diffusivity)
    # t = time (array of time values)
    def __init__(self, dist=0, diff=0, time=()):
        super(self.__class__, self).__init__(dist, diff, time)

    def run(self):
        return special.erfc(self.a / np.sqrt(4 * self.D * self.t))
