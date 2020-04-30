# PyBenchFCN

A python implementation of optimization benchmark functions (v0.0.2)

## Introduction

This library is a python implementation for the MatLab package [BenchmarkFcns Toolbox](http://benchmarkfcns.xyz/).

You can simply install with command ```pip install PyBenchFCN```.
- Pre-request: ```numpy```

## How to use

To use the package, one may see the sample code in ```Factory.py``` in the [repository](https://github.com/Y1fanHE/PyBenchFCN), or follow the script below.

```
import numpy as np

# import single objective problems from PyBenchFCN
from PyBenchFCN import SingleObjectiveProblem as SOP

n_var = 10                                      # dimension of problem
n_pop = 3                                       # size of population

problem = SOP.ackleyfcn(n_var)                  # Ackley problem

print( np.round(problem.optimalF, 5) )          # show rounded optimal value

xl, xu = problem.boundaries                     # bound of problem

x = np.random.uniform(xl, xu, n_var)            # initialize a solution
print( problem.f(x) )                           # show fitness value

X = np.random.uniform( xl, xu, (n_pop, n_var) ) # initialize a population
print( problem.F(X) )                           # show fitness values
```

## List of Functions

Totally, 61 functions are implemented. Please check the homepage of [BenchmarkFcns Toolbox](http://benchmarkfcns.xyz/) for the documentation.

- Ackley Function
- Ackley N.2 Function
- Ackley N.3 Function
- Adjiman Function
- Alpine N.1 Function
- Alpine N.2 Function
- Bartelsconn Function
- Beale Function
- Bird Function
- Bohachevsky N.1 Function
- Bohachevsky N.2 Function
- Booth Function
- Brent Function
- Brown Function
- Bukin N.6 Function
- Cross-in-Tray Function
- Deckkers-Aarts Function
- Dropwave Function
- Easom Function
- Egg Crate Function
- Eggholder Function
- Exponential Function
- Goldstein-Price Function
- Gramacy & Lee Function
- Griewank Function
- Happy Cat Function
- Himmelblau Function
- Holder-Table Function
- Keane Function
- Leon Function
- Levi N.13 Function
- Matyas Function
- McCormick Function
- Periodic Function
- Picheny Function
- Powell Sum Function
- Qing Function
- Quartic Function
- Rastrigin Function
- Ridge Function
- Rosenbrock Function
- Salomon Function
- Schaffer N.1 Function
- Schaffer N.2 Function
- Schaffer N.3 Function
- Schaffer N.4 Function
- Schwefel 2.20 Function
- Schwefel 2.21 Function
- Schwefel 2.22 Function
- Schwefel 2.23 Function
- Schwefel Function
- Sphere Function
- Styblinskitank Function
- Sum Squares Function
- Three-Hump Camel Function
- Wolfe Function
- Xin-She Yang N.1 Function
- Xin-She Yang N.2 Function
- Xin-She Yang N.3 Function
- Xin-She Yang N.4 Function
- Zakharov Function