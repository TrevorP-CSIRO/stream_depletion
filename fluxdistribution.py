""" flux distribution along the river """


import sd_solution
import numpy as np


class fluxdistribution(sd_solution.sd_solution):

    # a = dist (distance to pump)
    # D = diff (aquifer diffusivity)
    # t = time (array of time values)
    # L = reach_L (the total river reach length which must be a function of 'a' (a * some multiplier)
    #             for purposes of flux calculation because the flux distribtion is very sensitive to 'a')
    # dL = spstep
    def __init__(self, dist=0, diff=0, time=(), reach_L=0, spstep=1):
        super().__init__(dist, diff, time)
        self.L = reach_L
        self.dL = spstep

    @property
    def L(self):
        return self._L

    @L.setter
    def L(self, value):
        self._L = value

    @property
    def dL(self):
        return self._dL

    @dL.setter
    def dL(self, value):
        self._dL = value

    @property
    def steps(self):
        return int(self.L/self.dL+1)

    @property
    def xcoords(self):
        x_coor = np.zeros(self.steps)
        x_coor[0] = -self.L/2
        # generate array of coordinates where fluxes are calculated
        for i in range(1, self.steps):
            x_coor[i] = x_coor[i-1] + self.dL
        x_zero = int((self.steps-1)/2)   # index where x-coor is zero
        # replace zero with a small value (avoid singilarity at zero)
        x_coor[x_zero] = 1E-6
        return x_coor

    def run(self):
        # current output is wrong
        # needs a speed up
        flux = np.zeros((len(self.t), self.steps))
        for i in range(len(self.t)):
            Z1 = np.multiply(self.xcoords, self.xcoords) + self.a**2
            Z2 = 4*self.D*self.t[i]
            flux[i][:] = (np.multiply(self.a/(np.pi*Z1), np.exp(-Z1/Z2)))[:]
            # for j in range(self.steps):
            #    Z1 = self.xcoords[j]**2 + self.a**2
            #    Z2 = 4*self.D*self.t[i]
            # calculate instantaneous flux
            #flux[i][j] = self.a/(np.pi*Z1)*np.exp(-Z1/Z2)
        return flux
