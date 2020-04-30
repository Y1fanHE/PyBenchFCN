# PyBenchFCN

A python implementation of optimization benchmark functions (v1.0.0)

## Introduction

This library is a python implementation for the MatLab package [BenchmarkFcns Toolbox](http://benchmarkfcns.xyz/).

You can simply install with command ```pip install PyBenchFCN```.
- Pre-request: ```numpy```

## How to Use

To use the package, one may see the sample code in ```Factory.py``` in the [repository](https://github.com/Y1fanHE/PyBenchFCN), or follow the script below.

```
import numpy as np

# import single objective problems from PyBenchFCN
from PyBenchFCN import SingleObjectiveProblem as SOP

n_var = 10                                      # dimension of problem
n_pop = 3                                       # size of population

problem = SOP.ackleyfcn(n_var)                  # Ackley problem

'''same function as the code above
from PyBenchFCN import Factory
problem = Factory.set_sop("f1", n_var)
'''

print( np.round(problem.optimalF, 5) )          # show rounded optimal value

xl, xu = problem.boundaries                     # bound of problem

x = np.random.uniform(xl, xu, n_var)            # initialize a solution
print( problem.f(x) )                           # show fitness value

X = np.random.uniform( xl, xu, (n_pop, n_var) ) # initialize a population
print( problem.F(X) )                           # show fitness values
```

## List of Functions

Totally, 61 functions are implemented. The plot of 2D versions of 59 problems are provided. Please check the homepage of [BenchmarkFcns Toolbox](http://benchmarkfcns.xyz/) for the further documentation.

- Ackley Function [>>](./FitnessLandScape.md#ackley-function)
- Ackley N.2 Function [>>](./FitnessLandScape.md#ackley-n2-function)
- Ackley N.3 Function [>>](./FitnessLandScape.md#ackley-n3-function)
- Adjiman Function [>>](./FitnessLandScape.md#adjiman-function)
- Alpine N.1 Function [>>](./FitnessLandScape.md#alpine-n1-function)
- Alpine N.2 Function [>>](./FitnessLandScape.md#alpine-n2-function)
- Bartelsconn Function [>>](./FitnessLandScape.md#bartelsconn-function)
- Beale Function [>>](./FitnessLandScape.md#beale-function)
- Bird Function [>>](./FitnessLandScape.md#bird-function)
- Bohachevsky N.1 Function [>>](./FitnessLandScape.md#bohachevsky-n1-function)
- Bohachevsky N.2 Function [>>](./FitnessLandScape.md#bohachevsky-n2-function)
- Booth Function [>>](./FitnessLandScape.md#booth-function)
- Brent Function [>>](./FitnessLandScape.md#brent-function)
- BrownFunction [>>](./FitnessLandScape.md#brown-function)
- Bukin N.6 Function [>>](./FitnessLandScape.md#bukin-n6-function)
- Cross-in-Tray Function [>>](./FitnessLandScape.md#cross-in-tray-function)
- Deckkers-Aarts Function [>>](./FitnessLandScape.md#deckkers-aarts-function)
- Dropwave Function [>>](./FitnessLandScape.md#dropwave-function)
- Easom Function [>>](./FitnessLandScape.md#easom-function)
- Egg Crate Function [>>](./FitnessLandScape.md#egg-crate-function)
- Eggholder Function [>>](./FitnessLandScape.md#eggholder-function)
- Exponential Function [>>](./FitnessLandScape.md#exponential-function)
- Goldstein-Price Function [>>](./FitnessLandScape.md#goldstein-price-function)
- Gramacy & Lee Function
- Griewank Function [>>](./FitnessLandScape.md#griewank-function)
- Happy Cat Function [>>](./FitnessLandScape.md#happy-cat-function)
- Himmelblau Function [>>](./FitnessLandScape.md#himmelblau-function)
- Holder-Table Function [>>](./FitnessLandScape.md#holder-table-function)
- Keane Function [>>](./FitnessLandScape.md#keane-function)
- Leon Function [>>](./FitnessLandScape.md#leon-function)
- Levi N.13 Function [>>](./FitnessLandScape.md#levi-n13-function)
- Matyas Function [>>](./FitnessLandScape.md#matyas-function)
- McCormick Function [>>](./FitnessLandScape.md#mccormick-function)
- Periodic Function [>>](./FitnessLandScape.md#periodic-function)
- Picheny Function [>>](./FitnessLandScape.md#picheny-function)
- Powell Sum Function [>>](./FitnessLandScape.md#powell-sum-function)
- Qing Function [>>](./FitnessLandScape.md#qing-function)
- Quatric Function [>>](./FitnessLandScape.md#quartic-function)
- RastriginFunction [>>](./FitnessLandScape.md#rastrigin-function)
- Ridge Function [>>](./FitnessLandScape.md#ridge-function)
- Rosenbrock Function [>>](./FitnessLandScape.md#rosenbrock-function)
- Salomon Function [>>](./FitnessLandScape.md#salomon-function)
- Schaffer N.1 Function [>>](./FitnessLandScape.md#schaffer-n1-function)
- Schaffer N.2 Function [>>](./FitnessLandScape.md#schaffer-n2-function)
- Schaffer N.3 Function [>>](./FitnessLandScape.md#schaffer-n3-function)
- Schaffer N.4 Function [>>](./FitnessLandScape.md#schaffer-n4-function)
- Schwefel 2.20 Function [>>](./FitnessLandScape.md#schwefel-220-function)
- Schwefel 2.21 Function [>>](./FitnessLandScape.md#schwefel-221-function)
- Schwefel 2.22 Function [>>](./FitnessLandScape.md#schwefel-222-function)
- Schwefel 2.23 Function [>>](./FitnessLandScape.md#schwefel-223-function)
- Schwefel Function [>>](./FitnessLandScape.md#schwefel-function)
- Sphere Function [>>](./FitnessLandScape.md#sphere-function)
- StyblinskitankFunction [>>](./FitnessLandScape.md#styblinskitank-function)
- Sum Squares Function [>>](./FitnessLandScape.md#sum-squares-function)
- Three-Hump Camel Function [>>](./FitnessLandScape.md#three-hump-camel-function)
- Wolfe Function
- Xin-She Yang N.1 Function [>>](./FitnessLandScape.md#xin-she-yang-n1-function)
- Xin-She Yang N.2 Function [>>](./FitnessLandScape.md#xin-she-yang-n2-function)
- Xin-She Yang N.3 Function [>>](./FitnessLandScape.md#xin-she-yang-n3-function)
- Xin-She Yang N.4 Function [>>](./FitnessLandScape.md#xin-she-yang-n4-function)
- Zakharov Function [>>](./FitnessLandScape.md#zakharov-function)
