import numpy as np

# import single objective problems from PyBenchFCN
from PyBenchFCN import SingleObjectiveProblem as SOP

n_var = 10                                      # dimension of problem
n_pop = 3                                       # size of population

problem = SOP.ackleyfcn(n_var)                  # Ackley problem

print(problem.optimalF)                         # show optimal value

xl, xu = problem.boundaries                     # bound of problem

x = np.random.uniform(xl, xu, n_var)            # initialize a solution
print( problem.f(x) )                           # show fitness value

X = np.random.uniform( xl, xu, (n_pop, n_var) ) # initialize a population
print( problem.F(X) )                           # show fitness values