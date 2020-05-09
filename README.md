# PyBenchFCN

- [How to Install](#how-to-install)
- [How to Use](#how-to-use)
  - [Classical Single-Objective Optimization](#classical-single-objective-optimization)
    - [Setup Benchmark Function](#setup-benchmark-function)
    - [Plot Fitness Landscape](#plot-fitness-landscape)
- [List of Functions](#list-of-functions)
  - [Classical Single-Objective Optimization](#classical-single-objective-optimization-1)
  - [Discrete Optimization](#discrete-optimization)
  - [Multi-Objective Optimization](#multi-objective-optimization)
  - [Real-World Optimization](#real-world-optimization)
- [Authors](#authors)
- [License](#license)
- [Acknowledgement](#acknowledgement)

## How to Install

You can simply install with command ```pip install PyBenchFCN```.
- Pre-request: ```numpy```, ```matplotlib```

## How to Use

### Classical Single-Objective Optimization

The input of each numerical optimization problem could be a 1-D ndarray, or 2-D ndarray.
- **1-D array**
  - an example of **a solution (individual)** for 10D problem is ```np.random.uniform(0, 1, 10)```, where each entry is a decision variable.
  - use ```f()``` to return a fitness value (scalar).
- **2-D array**
  - an example of **group of solutions (population)** for 10D problem is ```np.random.uniform(0, 1, (5, 10))```, where each row (totally 5) is an individual.
  - use ```F()``` to return an array of fitness value (1-D array).

#### Setup Benchmark Function

To set a benchmark function, one may see the sample code in ```Factory.py``` in the [repository](https://github.com/Y1fanHE/PyBenchFCN), or follow the script below. Also, there is a sample optimization program provided in ```sample.py```.

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
print( problem.f(x) )                           # show fitness value as scalar

X = np.random.uniform( xl, xu, (n_pop, n_var) ) # initialize a population
print( problem.F(X) )                           # show fitness values as 1d-array
```

#### Plot Fitness Landscape

To plot a fitness landscape (2D space), one can use the code below. **Notice, this function only works for continuous SOPs.**

```python3
from PyBenchFCN import Tool
Tool.plot_sop("sphere", mode="save")            # plot and save landscape of Sphere function
Tool.plot_sop("schwefel", plot_type="contour")  # plot contour plot of Schwefel function
```

## List of Functions

### Classical Single-Objective Optimization

Totally, [61 single-objective functions](./SingleObjectiveProblem.md) are implemented based on [BenchmarkFcns Toolbox](http://benchmarkfcns.xyz/). The plot of 2D versions of 59 problems are provided. Please check the homepage of [BenchmarkFcns Toolbox](http://benchmarkfcns.xyz/) or [this website](https://www.sfu.ca/~ssurjano/optimization.html) for the further documentation.

### Discrete Optimization

*Under development ...*

### Multi-Objective Optimization

*Under development ...*

### Real-World Optimization

*Under development ...*

## Authors

[Yifan He](https://y1fanhe.github.io) @ Dept. of CS, UTsukuba

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Acknowledgement

PyBenchFCN is maintained by [Yifan He](https://y1fanhe.github.io). The author of this repostory is very grateful to Mr. Mazhar Ansari Ardeh, who implemented the MatLab package BenchFCNs Toolbox.

- If you find any mistakes, please report at a new issue.
- If you want to help me implement more benchmarks (discrete optimization, multi-objective optimization), please contact at [he.yifan.xs@alumni.tsukuba.ac.jp](mailto:he.yifan.xs@alumni.tsukuba.ac.jp).
