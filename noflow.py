""" Depletion with a no flow boundary (Knight et al., 2005) """

from scipy import special as special
import numpy as np
import sd_solution


class noflow(sd_solution.sd_solution):

    # a = dist (distance to pump)
    # D = diff (aquifer diffusivity)
    # t = time (array of time values)
    # nfdist = noflowdist (distance to no flow boundary which should be >= a)
    def __init__(self, dist=0, diff=0, time=(), noflowdist=0):
        super().__init__(dist, diff, time)
        self.nfdist = noflowdist

    @property
    def nfdist(self):
        return self._nfdist

    @nfdist.setter
    def nfdist(self, value):
        self._nfdist = value

    # if nfdist < dist then resp = 0
    def run(self):
        if self.nfdist < self.a:
            return np.zeros(len(self.t))
        resp = np.empty(len(self.t))
        for i in range(len(self.t)):
            term_1 = 1/np.sqrt(self.D*self.t[i])/2
            R_1 = special.erfc(self.a*term_1)
            R_2 = 0
            # calculate the sum of the series for 20 terms
            for j in range(20):
                n = j+1
                term_2 = 2*n*self.nfdist-self.a
                term_3 = 2*n*self.nfdist+self.a
                term_4 = (-1)**(n+1)
                term_5 = special.erfc(term_1*term_2)
                term_6 = special.erfc(term_1*term_3)
                R_2 = R_2+term_4*(term_5-term_6)
            resp[i] = R_1+R_2
        return resp
