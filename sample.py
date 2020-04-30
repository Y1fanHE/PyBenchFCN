'''
This program shows an example of using PyBenchFCN to do optimization.
The sample code shows a differential evolution algorithm solving 10-D
rastrigin function. With a numpy seed of 1001, the result should be
the same as what is shown in the end of this file. For the further
information, please visit https://github.com/Y1fanHE/PyBenchFCN, or
contact the author via email (he.yifan.xs@alumni.tsukuba.ac.jp).
'''

import numpy as np
from PyBenchFCN import Factory

np.random.seed(1001)

#####################
# PARAMETER SETTING #
#####################
n_var = 10                                          # define 10D problem domain
n_pop = 100                                         # set population size
n_gen = 1000                                        # set maximum generations
scale = 0.5                                         # set scaling factor
crate = 0.5                                         # set crossover rate

###################
# PROBLEM SETTING #
###################
rastrigin = Factory.set_sop("rastrigin", n_var)     # set 10D rastrigin problem
n_var = rastrigin.n_var                             # get corrected dimension
xl, xu = rastrigin.boundaries                       # get upper and lower bound

######################
# OPTIMIZATION BY DE #
######################
X = np.random.uniform(xl, xu, (n_pop, n_var))       # initialize population
F = rastrigin.F(X)                                  # evaluate fitness

for c_gen in range(n_gen):                          # generation loop

    Xc = X[:,:]                                     # select current individuals
    Xr1 = X[np.random.choice(n_pop, n_pop),:]       # select random individuals
    Xr2 = X[np.random.choice(n_pop, n_pop),:]       # select random individuals

    X_ = Xc + scale * (Xr1 - Xr2) * \
        np.random.choice([0, 1], (n_pop, n_var),
                         p=[crate, 1 - crate])      # DE/current/1
    F_ = rastrigin.F(X_)                            # evaluate offspring

    X[F_ < F] = X_[F_ < F]                          # greedy selection
    F[F_ < F] = F_[F_ < F]

##########
# RESULT #
##########
fbest = np.round( min(F), 3 )                       # get best solution so far
xbest = list( np.round( X[np.argmin(F), :], 3 ) )

print("The best solution of this run is")           # show the best solution
print(f"  f = {fbest}\n  x = {xbest}")

'''OUTPUT
The best solution of this run is
  f = 6.214
  x = [0.077, -0.062, 0.013, -0.027, 0.066, -0.965, 0.986, -0.02, -0.994, -0.008]
'''