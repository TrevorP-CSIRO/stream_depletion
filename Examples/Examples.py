import numpy as np
import matplotlib.pyplot as plt
import gloverbalmer
import semipervious
import noflow
import clogged
import semiconfined
import threeorthog
import twoorthog
import fluxdistribution
import commonfunctions as cf


# Uncomment a section to run example

# glover balmer example
# response for various diff values
""" Diff = 10, 50, 1000  # Aquifer diffusivity
a,  time_max, x = 100, 1000, 3
t = np.linspace(1, time_max)
fig = plt.figure(figsize=(7, 4))
for i in range(x):
    D = Diff[i]
    Label = "Diffusivity; D = "+"% s" % D
    g = gloverbalmer.gloverbalmer(a, D, t)
    resp = g.run()
    plt.plot(t, resp,  label=Label)
plt.xlabel('Time (days)')
plt.ylabel('Depletion factor')
Title = "Glover and Balmer solution for differnt diffusivities"
plt.title(Title)
plt.grid(True)
plt.axis([0, time_max, 0, 1])
text_1 = "Distance to river (a) = "+"% s" % a + " m"
plt.text(400, .83, text_1)
plt.legend(loc='best')
plt.show() """

# semipervious example
# response for (x) different alpha values
""" a, D, time_max, x = 100, 1000, 1000, 3
Alpha = 10, 500, 1500  # Remove this line when calculating from basic parameters
resp = np.zeros(time_max)
t = np.linspace(1, time_max, time_max)
fig = plt.figure(figsize=(8, 4))
for j in range(x):
    alpha = Alpha[j]
    Label = "Alpha= "+"% s" % alpha+" m"
    g = semipervious.semipervious(a, D, t, alpha)
    resp = g.run()
    plt.plot(t, resp,  label=Label)
plt.xlabel('Time (days)')
plt.ylabel('Depletion factor')
plt.title('Hantush depletion for differnt Alpha values')
plt.grid(True)
plt.axis([0, time_max, 0, 1])
plt.legend(loc='best')
plt.show() """

# no flow boundary example
# response for various boundary distances
""" Dist_no_flow = 200, 300, 500  # when very large, reverts back to Glover and Balmer
time_max, a, D, x = 1000, 100, 100, 3
t = np.linspace(1, time_max, time_max)
fig = plt.figure(figsize=(7, 4))
for j in range(x):
    c = Dist_no_flow[j]
    Label = "Distance to no-flow boundary; c= "+"% s" % c+" m"
    g = noflow.noflow(a, D, t, c)
    resp = g.run()
    plt.plot(t, resp,  label=Label)
plt.xlabel('Time (days)')
plt.ylabel('Depletion factor')
plt.title('Depletion for varous distances to no-flow boundary')
plt.grid(True)
plt.axis([0, time_max, 0, 1])
plt.text(400, .25, "Distance to river (a) = "+"% s" % a + " m")
plt.legend(loc='right')
plt.show() """

# clogged partially penetrating stream example
# response for various lambda values
""" K, phi, h, a, x = 50, 0.04, 37, 500, 3
Lambda = 100, 1000, 20000
D = K*h/phi*365  # Calculate diffusivity
t = np.empty(64)
fig = plt.figure(figsize=(8, 4))
for j in range(x):
    lam = Lambda[j]
    Label = "Lambda = "+"% s" % lam
    for i in range(64):
        t[i] = np.exp(0.25*i)/1000
    g = clogged.clogged(a, D, t, Lambda[j], phi)
    plt.plot(t, g.run(),  label=Label)
plt.xlabel('Time (years)')
plt.ylabel('Depletion factor')
plt.title('Depletion for varous Lambda values')
plt.grid(True)
plt.xscale("log")
plt.axis([0.001, 10000, 0, 1])
text_1 = "Distance to river (a) = "+"% s" % a + " m"
plt.text(11, .35, text_1)
plt.legend(loc='best')
plt.show() """

# semi-confined aquifer example
# response for various epsilon and lambda values
# time in years
# Input Basic aquifer parameters
""" L = 400  #length
aquifer_transmisivity = 300
Cond_aquitard = 1
Sat_aquitard_thick = 1
aquifer_storativity = 0.004
aquitard_porosity = 0.0001  # yields very high 'eps' to compare with Glover and Balmer
stream_width = 10
# yields very high 'lambda' to compare with Glover and Balmer
aquitard_dep_below_stream = 0.1
# -------------------------------------

Diff = aquifer_transmisivity / aquifer_storativity
Response_time = L**2 / Diff
K = L**2 / aquifer_transmisivity * Cond_aquitard / \
    Sat_aquitard_thick  # Calculate non-dimensional parameter 1
# use 2 sets of non-dimensional parameters
x = 2
# two values are selected randomly (the basic parameters should be varied, but this is for demo purposes)
epsilon = [0.1, 1]
lamb = [1, 5]
time_max = 1000
time = np.linspace(1, time_max, time_max)
#resp  = np.zeros(time_max)
fig = plt.figure(figsize=(8, 4))
t = time/Response_time
for j in range(x):
    Eps = epsilon[j]
    Lamb = lamb[j]
    kk = round(K, 1)  # used for labels only
    LLamb = round(lamb[j], 1)  # used for labels only
    Label = "\u03B5 =  " + "% s" % Eps + "  \u03BB =  " + \
        "% s" % LLamb + " K =  " + "% s" % kk
    # Label= "\u03B5 = "+"% s" %Eps;  \u03B5 = "+"% s" %Lamb" "\u03B5 = 0.1; \u03BB
    g = semiconfined.semiconfined(t, K, Eps, Lamb)
    resp = g.run()
    plt.plot(time, resp, label=Label)
plt.xscale("log")
plt.xlabel('Time (days)')
plt.ylabel('Depletion factor')
plt.title('Response for dimensional time')
plt.grid(True)
plt.axis([1, 1000, 0, 1])
plt.legend(loc='best')
plt.show()
 """

# two orthogonal rivers example
# response for (x) different  distances to second river
""" a, D, time_max, x = 100, 100, 1000, 3
L_sec_river = 200, 300, 700  # when very large, reverts back to Glover and Balmer
# --------------------------------------------
fig = plt.figure(figsize=(7, 4))
t = np.linspace(1, time_max)
for i in range(x):
    L = L_sec_river[i]
    lab = "Distance to second river; L = "+"% s" % L + " m"
    g = twoorthog.twoorthog(a, D, t, L)
    plt.plot(t, g.run(),  label=lab)
plt.xlabel('Time (days)')
plt.ylabel('Depletion factor')
plt.title('Depletion for differnt distances to second river')
plt.grid(True)
plt.axis([0, time_max, 0, 1])
plt.text(450, .65, "Distance to first river (a) = "+"% s" % a + " m")
plt.legend(loc='best')
plt.show() """

# three orthogonal rivers example
# response for (x) different distances to third river
""" a, b, D, time_max, x = 100, 200, 100, 1000, 3
c = 100, 200, 100000
fig = plt.figure(figsize=(7, 4))
t = np.linspace(1, time_max)
for i in range(x):
    C = c[i]
    lab = "Distance to third river; c = "+"% s" % C + " m"
    g = threeorthog.threeorthog(a, D, t, b, C)
    plt.plot(t, g.run(),  label=lab)
plt.xlabel('Time (days)')
plt.ylabel('Depletion factor')
plt.title('Depletion for differnt distances to third river')
plt.grid(True)
plt.axis([0, time_max, 0, 1])
plt.text(450, .65, "Distance to first river (a) = "+"% s" % a + " m")
plt.text(450, .55, "Distance to second river (b) = "+"% s" % b + " m")
plt.legend(loc='best')
plt.show() """

# flux distribution along reach
# distribution for reach at various times and locations
# reach length is expressed as a multiple of a
# distance pump to river; aquifer diffusivity
"""a,  D = 100, 50
# x number of times at which flux is calculated; y is number of gauge locations
x, y = 9, 4
# spacial step for intamtaneous flux calculation
dL = 1
# last very large time, response approaches steady state
Time = [10, 30, 60, 100, 300, 1000, 10000, 100000, 1000000]
# x coordinate of gauge locations (relative to pump, which is at x=0)
x_gauge = [-500, -100, 0,  1000]
mult = 20
Reach_L = mult * a

plt.figure(1, figsize=(20, 5))
plt.subplot(1, 2, 1)
g = fluxdistribution.fluxdistribution(a, D, Time, Reach_L, dL)
flux = g.run()
# calculate and round cumulative flux
# multiply instantaneous flux by step size
dlflux = flux * dL
cflux = np.round(np.sum(dlflux, 0), 3)
for i in range(len(Time)):
    t = Time[i]
    lab = "T = " + "% s" % t + " days; " + "Cum. resp. = " + "% s" % cflux[i]
    plt.plot(g.xcoords, flux[i][0:g.steps],  label=lab)
plt.xlabel('x-coor relative to pump location (m)')
plt.ylabel('Instantaneous flux response')
plt.title(
    'Flux response distribution along river & cumulative responses along entire reach')
plt.grid(True)
# plot only '10a' as curve flattens beyond it
plt.axis([-10*a, 10*a, 0, .005])
plt.text(-10*a+50, .004, "Pump located @ x=0")
plt.legend(loc='best')

# Calculative and plot cumulative flux responses at each gauge at various times
plt.subplot(1, 2, 2)
Sum = np.zeros((y, x))
for i in range(y):                                                 # loop gauges
    # index of x-coor where the gauge is
    gauge_loc_index = int((g.steps-1)/2 + x_gauge[i]/dL)
    N = i+1                                                           # for label
    # for label
    x_gauge_coor = x_gauge[i]
    lab = "Gauge " + "% s" % N + "; x = " + "% s" % x_gauge_coor + "m"
    for j in range(x):                                             # loop times
        for k in range(0, gauge_loc_index):                         # loop x-coordinates
            Sum[i][j] += flux[j][k]*dL
    plt.plot(Time, Sum[i][0:x],  label=lab)
plt.xlabel('Time (days)')
plt.ylabel('Cumulative flux response')
plt.title('Cumulative flux response at various gauge locations relative to pump')
plt.grid(True)
plt.xscale("log")
plt.legend(loc='best')
plt.axis([Time[0], Time[x-1], 0, 1])
plt.show()
"""
