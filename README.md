<h1>
<p align="center"># PyBenchFCN #</p>
<p align="center">A python implementation of optimization benchmarks</p>
</h1>

<p align="center">
<img src="./image/f51_3D.svg" width=300><img src="./image/f51_2D.svg" width=300></p>
<p align="center"><img src="./image/f58_2D.svg" width=300><img src="./image/f58_3D.svg" width=300></p>

- [How to Install](#how-to-install)
- [How to Use](#how-to-use)
  - [Set Benchmark Function](#set-benchmark-function)
  - [Plot Fitness Landscape](#plot-fitness-landscape)
- [List of Functions](#list-of-functions)
- [Acknowledgement](#acknowledgement)

## How to Install

This library is a python implementation for the MatLab package [BenchmarkFcns Toolbox](http://benchmarkfcns.xyz/).

You can simply install with command ```pip install PyBenchFCN```.
- Pre-request: ```numpy```, ```matplotlib```

## How to Use

### Set Benchmark Function

To set a benchmark function, one may see the sample code in ```Factory.py``` in the [repository](https://github.com/Y1fanHE/PyBenchFCN), or follow the script below.

```python3
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

### Plot Fitness Landscape

To plot a fitness landscape (2D space), one can use the code below.

```python3
from PyBenchFCN import Tool
Tool.plot("sphere", savepath="img.svg")         # plot and save landscape of Sphere function
Tool.plot("schwefel", plot_type="contour")      # plot contour plot of Schwefel function
```

## List of Functions

Totally, 61 functions are implemented. The plot of 2D versions of 59 problems are provided. Please check the homepage of [BenchmarkFcns Toolbox](http://benchmarkfcns.xyz/) for the further documentation.

- Ackley Function [>>](./FitnessLandScape.md#ackley-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```separable```

- Ackley N.2 Function [>>](./FitnessLandScape.md#ackley-n2-function)

```2-dim``` ```differentiable``` ```convex``` ```unimodal``` ```non-separable```

- Ackley N.3 Function [>>](./FitnessLandScape.md#ackley-n3-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Adjiman Function [>>](./FitnessLandScape.md#adjiman-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Alpine N.1 Function [>>](./FitnessLandScape.md#alpine-n1-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Alpine N.2 Function [>>](./FitnessLandScape.md#alpine-n2-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Bartelsconn Function [>>](./FitnessLandScape.md#bartelsconn-function)

```2-dim``` ```non-differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Beale Function [>>](./FitnessLandScape.md#beale-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Bird Function [>>](./FitnessLandScape.md#bird-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Bohachevsky N.1 Function [>>](./FitnessLandScape.md#bohachevsky-n1-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Bohachevsky N.2 Function [>>](./FitnessLandScape.md#bohachevsky-n2-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Booth Function [>>](./FitnessLandScape.md#booth-function)

```2-dim``` ```differentiable``` ```convex``` ```unimodal``` ```non-separable```

- Brent Function [>>](./FitnessLandScape.md#brent-function)

```2-dim``` ```differentiable``` ```convex``` ```unimodal``` ```non-separable```

- BrownFunction [>>](./FitnessLandScape.md#brown-function)

```n-dim``` ```differentiable``` ```convex``` ```unimodal``` ```non-separable```

- Bukin N.6 Function [>>](./FitnessLandScape.md#bukin-n6-function)

```2-dim``` ```non-differentiable``` ```convex``` ```multimodal``` ```non-separable```

- Cross-in-Tray Function [>>](./FitnessLandScape.md#cross-in-tray-function)

```2-dim``` ```non-differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Deckkers-Aarts Function [>>](./FitnessLandScape.md#deckkers-aarts-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Dropwave Function [>>](./FitnessLandScape.md#dropwave-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Easom Function [>>](./FitnessLandScape.md#easom-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```separable```

- Egg Crate Function [>>](./FitnessLandScape.md#egg-crate-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```separable```

- Eggholder Function [>>](./FitnessLandScape.md#eggholder-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Exponential Function [>>](./FitnessLandScape.md#exponential-function)

```n-dim``` ```differentiable``` ```convex``` ```unimodal``` ```non-separable```

- Goldstein-Price Function [>>](./FitnessLandScape.md#goldstein-price-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Gramacy & Lee Function [>>](./FitnessLandScape.md#gramacy--lee-function)

```1-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```separable```

- Griewank Function [>>](./FitnessLandScape.md#griewank-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Happy Cat Function [>>](./FitnessLandScape.md#happy-cat-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Himmelblau Function [>>](./FitnessLandScape.md#himmelblau-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Holder-Table Function [>>](./FitnessLandScape.md#holder-table-function)

```2-dim``` ```non-differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Keane Function [>>](./FitnessLandScape.md#keane-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Leon Function [>>](./FitnessLandScape.md#leon-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Levi N.13 Function [>>](./FitnessLandScape.md#levi-n13-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Matyas Function [>>](./FitnessLandScape.md#matyas-function)

```2-dim``` ```differentiable``` ```convex``` ```unimodal``` ```non-separable```

- McCormick Function [>>](./FitnessLandScape.md#mccormick-function)

```2-dim``` ```differentiable``` ```convex``` ```multimodal``` ```non-separable```

- Periodic Function [>>](./FitnessLandScape.md#periodic-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Picheny Function [>>](./FitnessLandScape.md#picheny-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Powell Sum Function [>>](./FitnessLandScape.md#powell-sum-function)

```n-dim``` ```differentiable``` ```convex``` ```unimodal``` ```separable```

- Qing Function [>>](./FitnessLandScape.md#qing-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Quatric Function [>>](./FitnessLandScape.md#quartic-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```separable``` ```random```

- RastriginFunction [>>](./FitnessLandScape.md#rastrigin-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```separable```

- Ridge Function [>>](./FitnessLandScape.md#ridge-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Rosenbrock Function [>>](./FitnessLandScape.md#rosenbrock-function)

```n-dim``` ```differentiable``` ```convex``` ```unimodal``` ```non-separable```

- Salomon Function [>>](./FitnessLandScape.md#salomon-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Schaffer N.1 Function [>>](./FitnessLandScape.md#schaffer-n1-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Schaffer N.2 Function [>>](./FitnessLandScape.md#schaffer-n2-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Schaffer N.3 Function [>>](./FitnessLandScape.md#schaffer-n3-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Schaffer N.4 Function [>>](./FitnessLandScape.md#schaffer-n4-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Schwefel 2.20 Function [>>](./FitnessLandScape.md#schwefel-220-function)

```n-dim``` ```non-differentiable``` ```convex``` ```unimodal``` ```separable```

- Schwefel 2.21 Function [>>](./FitnessLandScape.md#schwefel-221-function)

```n-dim``` ```non-differentiable``` ```convex``` ```unimodal``` ```separable```

- Schwefel 2.22 Function [>>](./FitnessLandScape.md#schwefel-222-function)

```n-dim``` ```non-differentiable``` ```convex``` ```unimodal``` ```non-separable```

- Schwefel 2.23 Function [>>](./FitnessLandScape.md#schwefel-223-function)

```n-dim``` ```differentiable``` ```convex``` ```unimodal``` ```separable```

- Schwefel Function [>>](./FitnessLandScape.md#schwefel-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```separable```

- Sphere Function [>>](./FitnessLandScape.md#sphere-function)

```n-dim``` ```differentiable``` ```convex``` ```unimodal``` ```separable```

- Styblinski-Tang Function [>>](./FitnessLandScape.md#styblinski-tang-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```separable```

- Sum Squares Function [>>](./FitnessLandScape.md#sum-squares-function)

```n-dim``` ```differentiable``` ```convex``` ```unimodal``` ```separable```

- Three-Hump Camel Function [>>](./FitnessLandScape.md#three-hump-camel-function)

```2-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Wolfe Function [>>](./FitnessLandScape.md#wolfe-function)

```3-dim``` ```non-differentiable``` ```non-convex``` ```multimodal``` ```separable```

- Xin-She Yang N.1 Function [>>](./FitnessLandScape.md#xin-she-yang-n1-function)

```n-dim``` ```non-differentiable``` ```non-convex``` ```multimodal``` ```separable``` ```random```

- Xin-She Yang N.2 Function [>>](./FitnessLandScape.md#xin-she-yang-n2-function)

```n-dim``` ```non-differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Xin-She Yang N.3 Function [>>](./FitnessLandScape.md#xin-she-yang-n3-function)

```n-dim``` ```differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Xin-She Yang N.4 Function [>>](./FitnessLandScape.md#xin-she-yang-n4-function)

```n-dim``` ```non-differentiable``` ```non-convex``` ```multimodal``` ```non-separable```

- Zakharov Function [>>](./FitnessLandScape.md#zakharov-function)

```n-dim``` ```differentiable``` ```convex``` ```unimodal``` ```non-separable```

## Acknowledgement

PyBenchFCN is maintained by [Y1fanHE](https://y1fanhe.github.io). The author of this repostory is very grateful to Mr. Mazhar Ansari Ardeh, who implemented the MatLab package BenchFCNs Toolbox.

- If you find any mistakes, please report at a new issue.
- If you want to help me implement more benchmarks (discrete optimization, multi-objective optimization), please contact at [he.yifan.xs@alumni.tsukuba.ac.jp](mailto:he.yifan.xs@alumni.tsukuba.ac.jp).
