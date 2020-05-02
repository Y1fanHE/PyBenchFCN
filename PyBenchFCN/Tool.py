from PyBenchFCN import Factory
import numpy as np
import matplotlib.pyplot as plt

class plot_sop():
    def __init__(self, problem_name, plot_type="surface",
                 mode="show", savepath="./fig.png",
                 plot_bound=None, n_part=100, n_level=10):
        self.problem_name = problem_name
        self.mode = mode
        self.savepath = savepath
        self.plot_type = plot_type
        self.plot_bound = plot_bound
        self.n_part = n_part
        self.n_level = n_level
        self._do()

    def _do(self):
        if self.plot_type == "surface":
            self._plot_surfaceSOP(self._calc_plot_dataSOP())
        if self.plot_type == "contour":
            self._plot_contourSOP(self._calc_plot_dataSOP())

    def _calc_plot_dataSOP(self):
        problem = Factory.set_sop(self.problem_name, n_var=2)                       # Set benchmark problem
        if problem.n_var != 2: print("This function does not support 2D space."); return None
        if self.plot_bound == None:
            xl, xu = problem.plot_bound
        else:
            xl, xu = self.plot_bound

        xl = np.zeros(2) + xl
        xu = np.zeros(2) + xu

        x1 = np.linspace(xl[0], xu[0], self.n_part)                                 # Generate pairs of decision value
        x2 = np.linspace(xl[1], xu[1], self.n_part)                                 # Generate pairs of decision value
        X1, X2 = np.meshgrid(x1, x2)
        X = np.c_[np.ravel(X1), np.ravel(X2)]
        F = problem.F(X).reshape(len(X1), len(X2))

        return X1, X2, F

    def _plot_surfaceSOP(self, INPUT):
        if INPUT == None: return
        X1, X2, F = INPUT
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d'); ax.plot_surface(X1, X2, F, cmap='winter_r')
        if self.mode == "show":
            plt.show()
        if self.mode == "save":
            plt.savefig(self.savepath)
        plt.close("all")

    def _plot_contourSOP(self, INPUT):
        if INPUT == None: return
        X1, X2, F = INPUT
        plt.figure()
        plt.contour(X1, X2, F, levels=self.n_level, cmap='winter_r'); plt.colorbar()
        if self.mode == "show":
            plt.show()
        if self.mode == "save":
            plt.savefig(self.savepath)
        plt.close("all")