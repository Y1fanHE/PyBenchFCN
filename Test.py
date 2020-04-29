import numpy as np
from Factory import set_problem

n_var = 10

for i in range(1, 62):
    prob = set_problem(f"f{i}", n_var)
    print(prob.optimalF, file=open("optim.txt", "a"))
