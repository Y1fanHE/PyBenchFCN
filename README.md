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

print(problem.optimalF)                         # show optimal value

xl, xu = problem.boundaries                     # bound of problem

x = np.random.uniform(xl, xu, n_var)            # initialize a solution
print( problem.f(x) )                           # show fitness value

X = np.random.uniform( xl, xu, (n_pop, n_var) ) # initialize a population
print( problem.F(X) )                           # show fitness values
```

## List of Functions

Totally, 61 functions are implemented. Please check the homepage of [BenchmarkFcns Toolbox](http://benchmarkfcns.xyz/) for the documentation.

- ackley
- ackleyn2
- ackleyn3
- adjiman
- alpinen1
- alpinen2
- bartelsconn
- beale
- bird
- bohachevskyn1
- bohachevskyn2
- booth
- brent
- brown
- bukinn6
- crossintray
- deckkersaarts
- dropwave
- easom
- eggcrate
- eggholder
- exponential
- goldsteinprice
- gramacylee
- griewank
- happycat
- himmelblau
- holdertable
- keane
- leon
- levin13
- matyas
- mccormick
- periodic
- picheny
- powellsum
- qing
- quartic
- rastrigin
- ridge
- rosenbrock
- salomon
- schaffern1
- schaffern2
- schaffern3
- schaffern4
- schwefel220
- schwefel221
- schwefel222
- schwefel223
- schwefel
- sphere
- styblinskitank
- sumsquares
- threehumpcamel
- wolfe
- xinsheyangn1
- xinsheyangn2
- xinsheyangn3
- xinsheyangn4
- zakharov