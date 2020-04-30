import numpy as np

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of Ackley benchmark function.
% SCORES = ACKLEYFCN(X) computes the value of the Ackey function at point
% X. ACKLEYFCN accepts a matrix of size M-by-N and returns a vetor SCORES
% of size M-by-1 in which each row contains the function value for each row
% of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = ackleyfcn(x)
    n = size(x, 2);
    ninverse = 1 / n;
    sum1 = sum(x .^ 2, 2);
    sum2 = sum(cos(2 * pi * x), 2);
    
    scores = 20 + exp(1) - (20 * exp(-0.2 * sqrt( ninverse * sum1))) - exp( ninverse * sum2);
end
'''
class ackleyfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-32, 32])
        self.plot_bound = np.array([-40, 40])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        n = X.shape[1]
        ninverse = 1 / n
        sum1 = np.sum( np.power(X, 2), axis=1 )
        sum2 = np.sum( np.cos(2 * np.pi * X), axis=1 )

        scores = 20 + np.exp(1) - ( 20 * np.exp( -0.2 * np.sqrt(ninverse * sum1) ) ) - np.exp(ninverse * sum2)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Ackley N. 2 function.
% SCORES = ACKLEYN2FCN(X) computes the value of the Ackley N. 2
% function at point X. ACKLEYN2FCN accepts a matrix of size M-by-2 and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = ackleyn2fcn(x)
    
    n = size(x, 2);
    assert(n == 2, 'Ackley N. 2 function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = -200 * exp(-0.02 * sqrt((X .^ 2) + (Y .^ 2)));
end
'''
class ackleyn2fcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-32, 32])
        self.plot_bound = np.array([-4, 4])
        self.n_var = 2
        if n_var != self.n_var: print('Ackley N. 2 function is only defined on a 2D space.')
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = -200 * np.exp( -0.02 * np.sqrt( np.power(x1, 2) + np.power(x2, 2) ) )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Ackley N. 3 function.
% SCORES = ACKLEYN3FCN(X) computes the value of the Ackley N. 3
% function at point X. ACKLEYN3FCN accepts a matrix of size M-by-2 and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = ackleyn3fcn(x)
    
    n = size(x, 2);
    assert(n == 2, 'Ackley N. 3 function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = -200 * exp(-0.02 * sqrt((X .^ 2) + (Y .^ 2))) + ...
             5 * exp(cos(3 * X) + sin(3 * Y));
end
'''
class ackleyn3fcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-32, 32])
        self.plot_bound = np.array([-4, 4])
        self.n_var = 2
        if n_var != self.n_var: print('Ackley N. 3 function is only defined on a 2D space.')
        self.optimalX = np.array([0.682584587365898, -0.36075325513719])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = -200 * np.exp( -0.02 * np.sqrt( np.power(x1, 2) + np.power(x2, 2) ) ) + \
                5 * np.exp( np.cos(3 * x1) + np.sin(3 * x2) )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Adjiman benchmark function.
% SCORES = ADJIMANHFCN(X) computes the value of the Adjiman function at 
% point X. ADJIMANHFCN accepts a matrix of size M-by-2 and returns a  
% vetor SCORES of size M-by-1 in which each row contains the function value 
% for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = adjimanfcn(x)
    
    n = size(x, 2);
    assert(n == 2, 'Adjiman function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = (cos(X) .* sin(Y)) - (X ./ ((Y .^ 2) + 1));
end
'''
class adjimanfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([[-1,-1], [2,1]])
        self.plot_bound = self.boundaries
        self.n_var = 2
        if n_var != self.n_var: print('Adjiman function is only defined on a 2D space.')
        self.optimalX = np.array([5, 0])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = ( np.cos(x1) * np.sin(x2) ) - ( x1 / ( np.power(x2, 2) + 1 ) )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Alpine N. 1 function.
% SCORES = ALPINEN1FCN(X) computes the value of the Alpine N. 1
% function at point X. ALPINEN1FCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information, please visit:
% benchmarkfcns.xyz/fcns/alpinen1fcn
% See also: alpinen2fcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = alpinen1fcn(x)
     scores = sum(abs(x .* sin(x) + 0.1 * x), 2);
end 
'''
class alpinen1fcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([0, 10])
        self.plot_bound = np.array([-10, 10])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = np.sum( np.abs(X * np.sin(X) + 0.1 * X), axis=1)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Alpine N. 2 function.
% SCORES = ALPINEN2FCN(X) computes the value of the Alpine N. 2
% function at point X. ALPINEN2FCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information, please visit:
% benchmarkfcns.xyz/fcns/alpinen2fcn
% See also: alpinen1fcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = alpinen2fcn(x)
     scores = prod(sqrt(x) .* sin(x), 2);
end 
'''
class alpinen2fcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([0, 10])
        self.plot_bound = self.boundaries
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var) + 7.917
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = - np.prod( np.sqrt(X) * np.sin(X), axis=1 )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Bartels Conn benchmark function.
% SCORES = BARTELSCONNFCN(X) computes the value of the Bartels Conn 
% function at point X. BARTELSCONNFCN accepts a matrix of size M-by-2 and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = bartelsconnfcn(x)
    
    n = size(x, 2);
    assert(n == 2, 'Bartels Conn function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = abs((X .^ 2) + (Y .^ 2) + (X .* Y)) + abs(sin(X)) + abs(cos(Y));
end
'''
class bartelsconnfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-500, 500])
        self.plot_bound = np.array([-4, 4])
        self.n_var = 2
        if n_var != self.n_var: print('Bartels Conn function is only defined on a 2D space.')
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = np.abs( np.power(x1, 2) + np.power(x2, 2) + (x1 * x2) ) + np.abs( np.sin(x1) ) + np.abs( np.cos(x2) )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Beale benchmark function.
% SCORES = BEALEFCN(X) computes the value of the Beale function at 
% point X. BEALEFCN accepts a matrix of size M-by-2 and returns a  
% vetor SCORES of size M-by-1 in which each row contains the function value 
% for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = bealefcn(x)
    n = size(x, 2);
    assert(n == 2, 'Beale''s function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = (1.5 - X + (X .* Y)).^2 + ...
             (2.25 - X + (X .* (Y.^2))).^2 + ...
             (2.625 - X + (X .* (Y.^3))).^2;
end
'''
class bealefcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-4.5, 4.5])
        self.plot_bound = np.array([-5, 5])
        self.n_var = 2
        if n_var != self.n_var: print('Beale\'s function is only defined on a 2D space.')
        self.optimalX = np.array([3, 0.5])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = np.power( 1.5 - x1 + (x1 * x2), 2 ) + \
                np.power( 2.25 - x1 + ( x1 * np.power(x2, 2) ), 2 ) + \
                np.power( 2.625 - x1 + ( x1 * np.power(x2, 3) ), 2 )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Bird function.
% SCORES = BIRDFCN(X) computes the value of the Bird 
% function at point X. BIRDFCN accepts a matrix of size M-by-2 and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = birdfcn(x)
    
    n = size(x, 2);
    assert(n == 2, 'Bird function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = sin(X) .* exp((1 - cos(Y)).^2) + ... 
        cos(Y) .* exp((1 - sin(X)) .^ 2) + ...
        (X - Y) .^ 2;
end
'''
class birdfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-2 * np.pi, 2 * np.pi])
        self.plot_bound = np.array([-10, 10])
        self.n_var = 2
        if n_var != self.n_var: print('Bird function is only defined on a 2D space.')
        self.optimalX = np.array([4.70104, 3.15294])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = np.sin(x1) * np.exp( np.power( 1 - np.cos(x2), 2 ) ) + \
            np.cos(x2) * np.exp( np.power( 1 - np.sin(x1), 2 ) ) + \
            np.power(x1 - x2, 2)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of Bohachevsky N. 1 benchmark function.
% SCORES = BOHACHEVSKYN1FCN(X) computes the value of the Bohachevsky N. 1
% function at point X. BOHACHEVSKYFCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for each row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = bohachevskyn1fcn(x)
    n = size(x, 2);
    assert(n == 2, 'The Bohachevsky N. 1 function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = (X .^ 2) + (2 * Y .^ 2) - (0.3 * cos(3 * pi * X)) - (0.4 * cos(4 * pi * Y)) + 0.7;
end
'''
class bohachevskyn1fcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-100, 100])
        self.plot_bound = self.boundaries
        self.n_var = 2
        if n_var != self.n_var: print('The Bohachevsky N. 1 function is only defined on a 2D space.')
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = np.power(x1, 2) + 2 * np.power(x2, 2) - 0.3 * np.cos(3 * np.pi * x1) - 0.4 * np.cos(4 * np.pi * x2) + 0.7
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of Bohachevsky N. 2 benchmark function.
% SCORES = BOHACHEVSKYN2FCN(X) computes the value of the Bohachevsky N. 2
% function at point X. BOHACHEVSKYN2FCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for each row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = bohachevskyn2fcn(x)
    n = size(x, 2);
    assert(n == 2, 'The Bohachevsky N. 2 function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = (X .^ 2) + (2 * Y .^ 2) - (0.3 * cos(3 * pi * X)) .* (0.4 * cos(4 * pi * Y)) + 0.3;
end
'''
class bohachevskyn2fcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-100, 100])
        self.plot_bound = np.array([-1.5, 1.5])
        self.n_var = 2
        if n_var != self.n_var: print('The Bohachevsky N. 2 function is only defined on a 2D space.')
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = np.power(x1, 2) + 2 * np.power(x2, 2) - 0.3 * np.cos(3 * np.pi * x1) * np.cos(4 * np.pi * x2) + 0.3
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Booth benchmark function.
% SCORES = BOOTHFCN(X) computes the value of the Booth's function at 
% point X. BOOTHFCN accepts a matrix of size M-by-2 and returns a  
% vetor SCORES of size M-by-1 in which each row contains the function value 
% for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = boothfcn(x)
    
    n = size(x, 2);
    assert(n == 2, 'Booth''s function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = (X + (2 * Y) - 7).^2 + ( (2 * X) + Y - 5).^2;
end
'''
class boothfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-10, 10])
        self.plot_bound = self.boundaries
        self.n_var = 2
        if n_var != self.n_var: print('Booth\'s function is only defined on a 2D space.')
        self.optimalX = np.array([1, 3])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = np.power(x1 + 2 * x2 - 7, 2) + np.power(2 * x1 + x2 - 5, 2)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Egg Crate function.
% SCORES = BRENTFCN(X) computes the value of the Brent 
% function at point X. BRENTFCN accepts a matrix of size M-by-2 and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information, please visit:
% benchmarkfcns.xyz/benchmarkfcns/brentfcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = brentfcn(x)
    n = size(x, 2);
    assert(n == 2, 'The Brent function is defined only on the 2-D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = (X + 10).^2 + (Y + 10).^2 + exp(-X.^2 - Y.^2);
end
'''
class brentfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-20, 0])
        self.plot_bound = self.boundaries
        self.n_var = 2
        if n_var != self.n_var: print('The Brent function is defined only on the 2-D space.')
        self.optimalX = np.zeros(self.n_var) - 10
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = np.power(x1 + 10, 2) + np.power(x2 + 10, 2) + np.exp( -np.power(x1, 2) - np.power(x2, 2) )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Brown benchmark function.
% SCORES = BROWNFCN(X) computes the value of the Brown function at point X.
% BROWNFCN accepts a matrix of size M-by-N and returns a vetor SCORES of 
% size M-by-1 in which each row contains the function value for the 
% corresponding row of X. For more information please visit: 
% http://benchmarkfcns.xyz/benchmarkfcns/brownfcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = brownfcn(x)
    
    n = size(x, 2);  
    scores = 0;
    
    x = x .^ 2;
    for i = 1:(n-1)
        scores = scores + x(:, i) .^ (x(:, i+1) + 1) + x(:, i+1).^(x(:, i) + 1);
    end
end
'''
class brownfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-1, 4])
        self.plot_bound = np.array([-1, 1])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        n = X.shape[1]
        scores = 0

        X1 = np.power(X, 2)
        for i in range(0, n-1):
            scores = scores + np.power(X1[:, i], X1[:, i + 1] + 1) + np.power(X1[:, i + 1], X1[:, i] + 1)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Bukin N. 6 benchmark function.
% SCORES = BUKINN6FCN(X) computes the value of the Bukin N. 6 function at 
% point X. BUKINN6FCN accepts a matrix of size M-by-2 and returns a  
% vetor SCORES of size M-by-1 in which each row contains the function value 
% for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = bukinn6fcn(x)
    n = size(x, 2);
    assert(n == 2, 'The Bukin N. 6 functions is only defined on a 2D space.')
    
    X = x(:, 1);
    X2 = X .^ 2;
    Y = x(:, 2);
    
    scores = 100 * sqrt(abs(Y - 0.01 * X2)) + 0.01 * abs(X  + 10);
end
'''
class bukinn6fcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([[-15,-3], [-5,3]])
        self.plot_bound = self.boundaries
        self.n_var = 2
        if n_var != self.n_var: print('The Bukin N. 6 functions is only defined on a 2D space.')
        self.optimalX = np.array([-10, 1])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = np.power(x1, 2)
        x3 = X[:, 1]

        scores = 100 * np.sqrt( np.abs(x3 - 0.01 * x2) ) + 0.01 * np.abs(x1  + 10)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Cross-in-tray benchmark function.
% SCORES = CROSSINTRAYFCN(X) computes the value of the Cross-in-tray 
% function at point X. CROSSINTRAYFCN accepts a matrix of size M-by-2 
% and returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X. For more information 
% please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = crossintrayfcn(x)
    
    n = size(x, 2);
    assert(n == 2, 'The Cross-in-tray function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);

    expcomponent = abs(100 - (sqrt(X .^2 + Y .^2) / pi));
    
    scores = -0.0001 * ((abs(sin(X) .* sin(Y) .* exp(expcomponent)) + 1) .^ 0.1);
end
'''
class crossintrayfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-10, 10])
        self.plot_bound = self.boundaries
        self.n_var = 2
        if n_var != self.n_var: print('The Cross-in-tray function is only defined on a 2D space.')
        self.optimalX = np.array([1.349406685353340, 1.349406608602084])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        expcomponent = np.abs( 100 - ( np.sqrt( np.power(x1, 2) + np.power(x2, 2) ) / np.pi ) )

        scores = -0.0001 * np.power( np.abs( np.sin(x1) * np.sin(x2) * np.exp(expcomponent) ) + 1, 0.1 )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Deckkers-Aarts function.
% SCORES = DECKKERSAARTSFCN(X) computes the value of the Deckkers-Aarts  
% function at point X. DECKKERSAARTSFCN accepts a matrix of size M-by-2 and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information, please visit:
% benchmarkfcns.xyz/fcns/deckkersaartsfcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = deckkersaartsfcn(x)
    n = size(x, 2);
    assert(n == 2, 'The Deckkers-Aarts function is defined only on the 2-D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = (100000 * X.^2) + Y.^2 + - (X.^2 + Y.^2).^2 + (10^-5) * (X.^2 + Y.^2 ) .^4;
end 
'''
class deckkersaartsfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-20, 20])
        self.plot_bound = self.boundaries
        self.n_var = 2
        if n_var != self.n_var: print('The Deckkers-Aarts function is defined only on the 2-D space.')
        self.optimalX = np.array([0, 15])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = 100000 * np.power(x1, 2) + np.power(x2, 2) + - np.power( np.power(x1, 2) + \
            np.power(x2, 2), 2 ) + 1e-05 * np.power( np.power(x1, 2) + np.power(x2, 2), 4)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Drop-Wave benchmark function.
% SCORES = DROPWAVEFCN(X) computes the value of the Drop-Wave function at 
% point X. DROPWAVEFCN accepts a matrix of size M-by-2 and returns a  
% vetor SCORES of size M-by-1 in which each row contains the function value 
% for the corresponding row of X.
% For more information please visit: 
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = dropwavefcn(x)
    n = size(x, 2);
    assert(n == 2, 'Drop-Wave function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    numeratorcomp = 1 + cos(12 * sqrt(X .^ 2 + Y .^ 2));
    denumeratorcom = (0.5 * (X .^ 2 + Y .^ 2)) + 2;
    scores = - numeratorcomp ./ denumeratorcom;
end
'''
class dropwavefcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-5.2, 5.2])
        self.plot_bound = np.array([-5, 5])
        self.n_var = 2
        if n_var != self.n_var: print('Drop-Wave function is only defined on a 2D space.')
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        numeratorcomp = 1 + np.cos( 12 * np.sqrt( np.power(x1, 2) + np.power(x2, 2) ) )
        denumeratorcom = 0.5 * ( np.power(x1, 2) + np.power(x2, 2) ) + 2
        scores = - numeratorcomp / denumeratorcom
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Easom benchmark function.
% SCORES = EASOMFCN(X) computes the value of the Easom function at point X.
% EASOMFCN accepts a matrix of size M-by-2 and returns a vetor SCORES of 
% size M-by-1 in which each row contains the function value for the 
% corresponding row of X. For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = easomfcn(x)
    
    n = size(x, 2);
    assert(n == 2, 'The Easom''s function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = -cos(X) .* cos(Y) .* exp(-( ((X - pi) .^2) + ((Y - pi) .^ 2)) );
end
'''
class easomfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-100, 100])
        self.plot_bound = np.array([-50, 50])
        self.n_var = 2
        if n_var != self.n_var: print('The Easom\'s function is only defined on a 2D space.')
        self.optimalX = np.zeros(self.n_var) + np.pi
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = - np.cos(x1) * np.cos(x2) * np.exp( -( np.power(x1 - np.pi, 2) + np.power(x2 - np.pi, 2) ) )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Egg Crate function.
% SCORES = EGGCRATEFCN(X) computes the value of the Egg Crate 
% function at point X. EGGCRATEFCN accepts a matrix of size M-by-2 and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information, please visit:
% benchmarkfcns.xyz/fcns/eggcratefcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = eggcratefcn(x)
    n = size(x, 2);
    assert(n == 2, 'The Egg Crate function is defined only on the 2-D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = X.^2 + Y.^2 + (25 * (sin(X).^2 + sin(Y).^2));
end 
'''
class eggcratefcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-5, 5])
        self.plot_bound = self.boundaries
        self.n_var = 2
        if n_var != self.n_var: print('The Egg Crate function is defined only on the 2-D space.')
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = np.power(x1, 2) + np.power(x2, 2) + 25 * ( np.power( np.sin(x1), 2 ) + np.power( np.sin(x2), 2 ) )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Eggholder benchmark function.
% SCORES = EGGHOLDERFCN(X) computes the value of the Eggholder
% function at point X. EGGHOLDERFCN accepts a matrix of size M-by-2 
% and returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X. For more information 
% please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = eggholderfcn(x)
    n = size(x, 2);
    assert(n == 2, 'The Eggholder function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    sin1component = sin(sqrt(abs( (X / 2) + Y + 47)));
    sin2component = sin(sqrt(abs( X - Y + 47)));
    
    scores = -(Y + 47) .* sin1component - (X .* sin2component);
end
'''
class eggholderfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-512, 512])
        self.plot_bound = np.array([-600, 600])
        self.n_var = 2
        if n_var != self.n_var: print('The Eggholder function is only defined on a 2D space.')
        self.optimalX = np.array([512, 404.2319])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        sin1component = np.sin( np.sqrt( np.abs( (x1 / 2) + x2 + 47 ) ) )
        sin2component = np.sin( np.sqrt( np.abs(x1 - (x2 + 47) ) ) )

        scores = -(x2 + 47) * sin1component - (x1 * sin2component)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Exponential function.
% SCORES = EXPONENTIALFCN(X) computes the value of the Exponential
% function at point X. EXPONENTIALFCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = exponentialfcn(x)
   x2 = x .^2;
   
   scores = -exp(-0.5 * sum(x2, 2));
end
'''
class exponentialfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-1, 1])
        self.plot_bound = np.array([-2, 2])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        X1 = np.power(X, 2)

        scores = -np.exp( -0.5 * np.sum(X1, axis=1) )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of GOldstein-Price benchmark function.
% SCORES = GOLDSTEINPRICEFCN(X) computes the value of the GOLDSTEINPRICEFCN  
% function at point X. GOLDSTEINPRICEFCN accepts a matrix of size M-by-2 
% and returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = goldsteinpricefcn(x)
    n = size(x, 2);
    assert(n == 2, 'The Goldstein-Price function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = (1 + ((X + Y + 1).^ 2) .* (19 - (14 * X) + (3 * (X .^2)) - 14 * Y + (6 .* X .* Y) + (3 * (Y.^2)))) .* ...
        (30 + ((2 * X - 3 * Y).^2) .* (18 - 32 * X + 12 * (X .^2) + 48 * Y - (36 .* X .* Y) + (27 * (Y.^2))) );
end
'''
class goldsteinpricefcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-2, 2])
        self.plot_bound = self.boundaries
        self.n_var = 2
        if n_var != self.n_var: print('The Goldstein-Price function is only defined on a 2D space.')
        self.optimalX = np.array([0, -1])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = ( 1 + np.power(x1 + x2 + 1, 2) * ( 19 - 14 * x1 + 3 * np.power(x1, 2) - 14 * x2 + (6 * x1 * x2) + 3 * np.power(x2, 2) ) ) * \
            ( 30 + np.power(2 * x1 - 3 * x2, 2) * ( 18 - 32 * x1 + 12 * np.power(x1, 2) + 48 * x2 - (36 * x1 * x2) + 27 * np.power(x2, 2) ) )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Gramacy & Lee benchmark function.
% SCORES = GRAMACYLEEFCN(X) computes the value of the Gramacy & Lee 
% function at point X. GRAMACYLEEFCN accepts a matrix of size M-by-2 and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = gramacyleefcn(x)
    n = size(x, 2);
    assert(n == 1, 'Gramacy & Lee function is only defined on a 1-D space.')

    scores = (sin(10 .* pi .* x) ./ (2 * x) ) + ((x - 1) .^ 4);
end
'''
class gramacyleefcn():
    def __init__(self, n_var=1):
        self.boundaries = np.array([-0.5, 2.5])
        self.plot_bound = self.boundaries
        self.n_var = 1
        if n_var != self.n_var: print('Gramacy & Lee function is only defined on a 1-D space.')
        self.optimalX = np.array([0.548563444114526])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = ( np.sin(10 * np.pi * X) / (2 * X + 1e-14) ) + np.power(X - 1, 4)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Griewank benchmark function.
% SCORES = GRIEWANKFCN(X) computes the value of the Griewank's
% function at point X. GRIEWANKFCN accepts a matrix of size M-by-N 
% and returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = griewankfcn(x)
    
    n = size(x, 2);
    
    sumcomp = 0;
    prodcomp = 1;
    
    for i = 1:n
        sumcomp = sumcomp + (x(:, i) .^ 2);
        prodcomp = prodcomp .* (cos(x(:, i) / sqrt(i)));
    end
    
    scores = (sumcomp / 4000) - prodcomp + 1;
end
'''
class griewankfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-600, 600])
        self.plot_bound = np.array([-5, 5])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        n = self.n_var

        sumcomp = 0
        prodcomp = 1

        for i in range(n):
            sumcomp = sumcomp + np.power(X[:, i], 2)
            prodcomp = prodcomp * ( np.cos( X[:, i] / np.sqrt(i + 1) ) )

        scores = (sumcomp / 4000) - prodcomp + 1
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Happy Cat benchmark function.
% SCORES = HAPPYCATFCN(X) computes the value of the Happy Cat function at 
% point X. HAPPYCATFCN accepts a matrix of size M-by-N and returns a vetor 
% SCORES of size M-by-1 in which each row contains the function value for 
% the corresponding row of X. 
% SCORES = HAPPYCAT(X, ALPHA) specifies power of the sphere component of 
% the function.
% For more information please visit: 
% http://benchmarkfcns.xyz/benchmarkfcns/happycatfcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = happycatfcn(x, alpha)

    if nargin < 2 
        alpha = 0.5;
    end
    
    n = size(x, 2);
    x2 = sum(x .* x, 2);
    scores = ((x2 - n).^2).^(alpha) + (0.5*x2 + sum(x,2))/n + 0.5;
end
'''
class happycatfcn():
    def __init__(self, n_var=10, alpha=0.5):
        self.boundaries = np.array([-2, 2])
        self.plot_bound = self.boundaries
        self.alpha = alpha
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var) - 1
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        n = X.shape[1]
        x1 = np.sum(X * X, axis=1)
        scores = np.power( np.power(x1 - n, 2), self.alpha ) + ( 0.5 * x1 + np.sum(X, axis=1) ) / n + 0.5
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Himmelblau's benchmark function.
% SCORES = HIMMELBLAUFCN(X) computes the value of the Himmelblau's
% function at point X. HIMMELBLAUFCN accepts a matrix of size M-by-2 
% and returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Himmelblau's_function
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = himmelblaufcn(x)
    n = size(x, 2);
    assert(n == 2, 'Himmelblau''s function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = ((X .^ 2 + Y - 11) .^2) + ((X + (Y .^ 2) - 7) .^ 2);
end
'''
class himmelblaufcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-6, 6])
        self.plot_bound = np.array([-5, 5])
        self.n_var = 2
        if n_var != self.n_var: print('Himmelblau\'s function is only defined on a 2D space.')
        self.optimalX = np.array([3, 2])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = np.power( np.power(x1, 2) + x2 - 11, 2 ) + np.power( x1 + np.power(x2, 2) - 7, 2 )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the H�lder table benchmark function.
% SCORES = HOLDERTABLEFCN(X) computes the value of the H�lder table  
% function at point X. HOLDERTABLEFCN accepts a matrix of size M-by-2 and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X. For more information 
% please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = holdertablefcn(x)
    
    n = size(x, 2);
    assert(n == 2, 'The H�lder table function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    expcomponent = exp( abs(1 - (sqrt(X .^2 + Y .^ 2) / pi)) );
    
    scores = -abs(sin(X) .* cos(Y) .* expcomponent);
end
'''
class holdertablefcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-10, 10])
        self.plot_bound = self.boundaries
        self.n_var = 2
        if n_var != self.n_var: print('The Holder table function is only defined on a 2D space.')
        self.optimalX = np.array([8.05502, 9.66459])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        expcomponent = np.exp( np.abs( 1 - ( np.sqrt( np.power(x1, 2) + np.power(x2, 2) ) / np.pi ) ) )

        scores = -np.abs( np.sin(x1) * np.cos(x2) * expcomponent )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Keane function.
% SCORES = KEANEFCN(X) computes the value of the Keane function at point X.
% KEANEFCN accepts a matrix of size M-by-2 and returns a vetor SCORES of 
% size M-by-1 in which each row contains the function value for the 
% corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = keanefcn(x)
    n = size(x, 2);
    assert(n == 2, 'Keane function is defined only on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    numeratorcomp = (sin(X - Y) .^ 2) .* (sin(X + Y) .^ 2); 
    denominatorcomp = sqrt(X .^2 + Y .^2);
    scores = - numeratorcomp ./ denominatorcomp;
end
'''
class keanefcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([0, 10])
        self.plot_bound = np.array([-10, 10])
        self.n_var = 2
        if n_var != self.n_var: print('Keane function is defined only on a 2D space.')
        self.optimalX = np.array([1.393249070031784, 0])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]
        
        numeratorcomp = np.power( np.sin(x1 - x2), 2 ) * np.power( np.sin(x1 + x2), 2 )
        denominatorcomp = np.sqrt( np.power(x1, 2) + np.power(x2, 2) ) + 1e-14
        scores = - numeratorcomp / denominatorcomp
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Leon function.
% SCORES = LEONFCN(X) computes the value of the Leon function at point X.
% LEONFCN accepts a matrix of size M-by-2 and returns a vetor SCORES of 
% size M-by-1 in which each row contains the function value for the 
% corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = leonfcn(x)
    n = size(x, 2);
    assert(n == 2, 'Leon function is defined only on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = 100 * ((Y - X.^3) .^2) + ((1 - X) .^2);
end
'''
class leonfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([0, 10])
        self.plot_bound = np.array([-1.5, 1.5])
        self.n_var = 2
        if n_var != self.n_var: print('Leon function is defined only on a 2D space.')
        self.optimalX = np.zeros(self.n_var) + 1
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = 100 * np.power(x2 - np.power(x1, 3), 2) + np.power(1 - x1, 2)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the L�vi N. 13 benchmark function.
% SCORES = LEVIN13FCN(X) computes the value of the L�vi N. 13 function at 
% point X. LEVIN13FCN accepts a matrix of size M-by-2 and returns a  
% vetor SCORES of size M-by-1 in which each row contains the function value 
% for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = levin13fcn(x)
    n = size(x, 2);
    assert(n == 2, 'Levi''s function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    scores = sin(3 * pi * X) .^ 2 + ...
        ((X - 1).^2) .* (1 + sin(3 * pi * Y) .^ 2) + ...
        ((Y - 1).^2) .* (1 + sin(2 * pi * Y) .^ 2);
end
'''
class levin13fcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-10, 10])
        self.plot_bound = self.boundaries
        self.n_var = 2
        if n_var != self.n_var: print('Levi\'s function is only defined on a 2D space.')
        self.optimalX = np.zeros(self.n_var) + 1
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]
        scores = np.power( np.sin(3 * np.pi * x1), 2 ) + \
            np.power(x1 - 1, 2) * (1 + np.power( np.sin(3 * np.pi * x2), 2 ) ) + \
            np.power(x2 - 1, 2) * (1 + np.power( np.sin(2 * np.pi * x2), 2 ) )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Matyas benchmark function.
% SCORES = MATYASFCN(X) computes the value of the Matyas function at 
% point X. MATYASFCN accepts a matrix of size M-by-2 and returns a  
% vetor SCORES of size M-by-1 in which each row contains the function value 
% for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = matyasfcn(x)
    n = size(x, 2);
    assert(n == 2, 'Matyas''s function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = 0.26 * (X .^ 2 + Y.^2) - 0.48 * X .* Y;
end
'''
class matyasfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-10, 10])
        self.plot_bound = self.boundaries
        self.n_var = 2
        if n_var != self.n_var: print('Matyas\'s function is only defined on a 2D space.')
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = 0.26 * ( np.power(x1, 2) + np.power(x2, 2) ) - 0.48 * x1 * x2
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the McCormick benchmark function.
% SCORES = MCCORMICKFCN(X) computes the value of the McCormick function 
% at point X. MCCORMICKFCN accepts a matrix of size M-by-2 and returns a 
% vetor SCORES of size M-by-1 in which each row contains the function value 
% for the corresponding row of X. For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = mccormickfcn(x)
    
    n = size(x, 2);
    assert(n == 2, 'The McCormick function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = sin(X + Y) + ((X - Y) .^2 ) - 1.5 * X + 2.5 * Y + 1;
end
'''
class mccormickfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([ [-1.5, -3], [4, 3] ])
        self.plot_bound = np.array([ [-2, -3], [4, 3] ])
        self.n_var = 2
        if n_var != self.n_var: print('The McCormick function is only defined on a 2D space.')
        self.optimalX = np.array([-0.547, -1.547])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = np.sin(x1 + x2) + np.power(x1 - x2, 2) - 1.5 * x1 + 2.5 * x2 + 1
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Sum Square function.
% SCORES = SUMSQUAREFCN(X) computes the value of the Periodic 
% function at point X. PERIODICFCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = periodicfcn(x)

    sin2x = sin(x) .^ 2;
    sumx2 = sum(x .^2, 2);
    scores = 1 + sum(sin2x, 2) -0.1 * exp(-sumx2);
    
end
'''
class periodicfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-10, 10])
        self.plot_bound = np.array([-2, 2])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        sin2x = np.power( np.sin(X), 2 )
        sumx2 = np.sum( np.power(X, 2), axis=1 )
        scores = 1 + np.sum(sin2x, axis=1) -0.1 * np.exp(-sumx2)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Picheny benchmark function.
% SCORES = PICHENYFCN(X) computes the value of the Beale function at 
% point X. PICHENYFCN accepts a matrix of size M-by-2 and returns a  
% vetor SCORES of size M-by-1 in which each row contains the function value 
% for the corresponding row of X.
% For more information please visit: 
% http://www.sfu.ca/~ssurjano/goldpr.html
% Note: The Picheny function is a modification of the Goldstein-Price 
% function. 
% See also: goldsteinpricefcn.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = pichenyfcn(x)
    n = size(x, 2);
    assert(n == 2, 'The Picheny function is only defined on a 2D space.')
    X = 4 * x(:, 1) - 2;
    Y = 4 * x(:, 2) - 2;
    
    term = (1 + ((X + Y + 1).^2) * (19 - (14 * X) + (3 * (X .^2)) - 14*Y + (6 .* X.*Y) + (3 * (Y.^2)))) .* ...
        (30 + ((2 * X - 3 * Y).^2) .* (18 - 32 * X + 12 * (X .^2) + 48 * Y - (36 .* X.*Y) + (27 * (Y.^2))) );
    coef = 1 / 2.427;
    scores = coef * (log10(term) - 8.693);
end
'''
class pichenyfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([0, 1])
        self.plot_bound = np.array([-2, 2])
        self.n_var = 2
        if n_var != self.n_var: print('The Picheny function is only defined on a 2D space.')
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = 4 * X[:, 0] - 2
        x2 = 4 * X[:, 1] - 2

        term = ( 1 + np.power(x1 + x2 + 1, 2) * ( 19 - 14 * x1 + 3 * np.power(x1, 2) - 14 * x2 + 6 * x1 * x2 + 3 * np.power(x2, 2) ) ) * \
            ( 30 + np.power(2 * x1 - 3 * x2, 2) * (18 - 32 * x1 + 12 * np.power(x1, 2) + 48 * x2 - 36 * x1 * x2 + 27 * np.power(x2, 2) ) )
        coef = 1 / 2.427
        scores = coef * (np.log10(term) - 8.693)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Powell Sum benchmark function.
% SCORES = POWELLSUMFCN(X) computes the value of the Powell Sum function at 
% point X. POWELLSUMFCN accepts a matrix of size M-by-N and returns a vetor 
% SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X. 
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = powellsumfcn(x)
    n = size(x, 2);
    absx = abs(x);
    
    scores = 0;
    for i = 1:n
        scores = scores + (absx(:, i) .^ (i + 1));
    end
end
'''
class powellsumfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-1, 1])
        self.plot_bound = np.array([-2, 2])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        n = X.shape[1]
        absx = np.abs(X)

        scores = 0
        for i in range(n):
            scores = scores + np.power(absx[:, i], i + 2)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Qing function.
% SCORES = QINGFCN(X) computes the value of the Qing
% function at point X. QINGFCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information, please visit:
% benchmarkfcns.xyz/fcns/qingfcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = qingfcn(x)
    n = size(x, 2);
    x2 = x .^2;
    
    scores = 0;
    for i = 1:n
        scores = scores + (x2(:, i) - i) .^ 2;
    end
end 
'''
class qingfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-500, 500])
        self.plot_bound = np.array([-2, 2])
        self.n_var = n_var
        self.optimalX = np.sqrt( (np.arange(self.n_var) + 1) )
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        n = X.shape[1]
        X1 = np.power(X, 2)

        scores = 0
        for i in range(n):
            scores = scores + np.power( X1[:, i] - (i + 1), 2 )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of Quartic benchmark function.
% SCORES = QUARTICFCN(X) computes the value of the Quartic function at 
% point X. QUARTICFCN accepts a matrix of size M-by-N and returns a vetor 
% SCORES of size M-by-1 in which each row contains the function value for
% each row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = quarticfcn(x)

    n = size(x, 2);
    
    scores = 0;
    for i = 1:n
        scores = scores + i *(x(:, i) .^ 4);
    end
     
    scores = scores + rand;
end
'''
class quarticfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-1.28, 1.28])
        self.plot_bound = self.boundaries
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        n = X.shape[1]

        scores = 0
        for i in range(n):
            scores = scores + (i + 1) * np.power(X[:, i], 4)

        scores = scores + np.random.rand(len(scores))
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of Rastrigin benchmark function.
% SCORES = RASTRIGINFCN(X) computes the value of the Rastrigin function at 
% point X. RASTRIGINFCN accepts a matrix of size M-by-N and returns a vetor 
% SCORES of size M-by-1 in which each row contains the function value for
% the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Rastrigin_function
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function f = rastriginfcn(x)
    n = size(x, 2);
    A = 10;
    f = (A * n) + (sum(x .^2 - A * cos(2 * pi * x), 2));
end
'''
class rastriginfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-5.12, 5.12])
        self.plot_bound = np.array([-5, 5])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        A = 10
        scores = (A * self.n_var) + np.sum( np.power(X, 2) - A * np.cos(2 * np.pi * X), axis=1 )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Ridge benchmark function.
% SCORES = RIDGEFCN(X) computes the value of the Ridge function at point X.
% RIDGEFCN accepts a matrix of size M-by-N and returns a vetor SCORES of 
% size M-by-1 in which each row contains the function value for the 
% corresponding row of X. 
% SCORES = RIDGEFCN(X, D) specifies contribution coefficient of the sphere 
% component of the function.
% SCORES = RIDGEFCN(X, D, ALPHA) specifies power of the sphere component of 
% the function.
% 
% For more information please visit: 
% http://benchmarkfcns.xyz/benchmarkfcns/ridgefcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = ridgefcn(x, d, alpha)

    if nargin < 3 
        alpha = 0.5;
    end
    if nargin < 2
        d = 1;
    end
        
    x1 = x(:, 1);
    scores = x1 + d * (sum(x(:, 2:end).^2, 2) .^ alpha);
end
'''
class ridgefcn():
    def __init__(self, n_var=10, d=1, alpha=0.5):
        self.boundaries = np.array([-5, 5])
        self.plot_bound = np.array([-2, 2])
        self.d = d
        self.alpha = alpha
        self.n_var = n_var
        self.optimalX = np.hstack( [self.boundaries[0], np.zeros(self.n_var - 1)] )
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        scores = x1 + self.d * np.power( np.sum( np.power(X[:, 1:], 2), axis=1), self.alpha )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Rosenbrock benchmark function.
% SCORES = ROSENBROCKFCN(X) computes the value of the Rosenbrock function  
% at point X. ROSENBROCKFCN accepts a matrix of size M-by-N and returns a  
% vetor SCORES of size M-by-1 in which each row contains the function value 
% for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Rosenbrock_function
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = rosenbrockfcn(x)
    scores = 0;
    n = size(x, 2);
    assert(n >= 1, 'Given input X cannot be empty');
    a = 1;
    b = 100;
    for i = 1 : (n-1)
        scores = scores + (b * ((x(:, i+1) - (x(:, i).^2)) .^ 2)) + ((a - x(:, i)) .^ 2);
    end
end
'''
class rosenbrockfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-5, 10])
        self.plot_bound = np.array([-10, 10])
        self.n_var = int( max(1, n_var) )
        if n_var < 1: print('Given input X cannot be empty')
        self.optimalX = np.zeros(self.n_var) + 1
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = 0
        a = 1
        b = 100
        for i in range(self.n_var - 1):
            scores = scores + b * np.power( X[:, i+1] - np.power(X[:, i], 2), 2 ) + np.power(a - X[:, i], 2)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Salomon's benchmark function.
% SCORES = SALOMONFCN(X) computes the value of the Salomon's   
% function at point X. SALOMONFCN accepts a matrix of size M-by-N  
% and returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = salomonfcn(x)
    x2 = x .^ 2;
    sumx2 = sum(x2, 2);
    sqrtsx2 = sqrt(sumx2);
    
    scores = 1 - cos(2 .* pi .* sqrtsx2) + (0.1 * sqrtsx2);
end
'''
class salomonfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-100, 100])
        self.plot_bound = np.array([-4, 4])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        X1 = np.power(X, 2)
        sumx2 = np.sum(X1, axis=1)
        sqrtsx2 = np.sqrt(sumx2)

        scores = 1 - np.cos(2 * np.pi * sqrtsx2) + (0.1 * sqrtsx2)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Schaffer N. 1 function.
% SCORES = SCHAFFERN1FCN(X) computes the value of the Schaffer N. 1 
% function at point X. SCHAFFERN1FCN accepts a matrix of size M-by-2 and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = schaffern1fcn(x)
    n = size(x, 2);
    assert(n == 2, 'Schaffer function N. 1 is defined only on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    numeratorcomp = (sin((X .^ 2 + Y .^ 2) .^ 2) .^ 2) - 0.5; 
    denominatorcomp = (1 + 0.001 * (X .^2 + Y .^2)) .^2 ;
    scores = 0.5 + numeratorcomp ./ denominatorcomp;
end
'''
class schaffern1fcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-100, 100])
        self.plot_bound = np.array([-50, 50])
        self.n_var = 2
        if n_var != self.n_var: print('Schaffer function N. 1 is defined only on a 2D space.')
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        numeratorcomp = np.power( np.sin( np.power( np.power(x1, 2) + np.power(x2, 2), 2 ) ), 2) - 0.5
        denominatorcomp = np.power( 1 + 0.001 * ( np.power(x1, 2) + np.power(x2, 2) ), 2 )
        scores = 0.5 + numeratorcomp / denominatorcomp
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Schaffer N. 2 benchmark function.
% SCORES = SCHAFFERN2FCN(X) computes the value of the Schaffer N. 2 function 
% at point X. SCHAFFERN2FCN accepts a matrix of size M-by-2 and returns a 
% vetor SCORES of size M-by-1 in which each row contains the function value 
% for the corresponding row of X. For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = schaffern2fcn(x)
    
    n = size(x, 2);
    assert(n == 2, 'The Schaffer N. 2 function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    sincomponent = sin( (X .^ 2) - (Y .^ 2) ).^2;
    
    scores = 0.5 + ((sincomponent - 0.5) ./ (1 + 0.001 * (X .^2 + Y .^2)) .^2 ) ;
end
'''
class schaffern2fcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-100, 100])
        self.plot_bound = np.array([-50, 50])
        self.n_var = 2
        if n_var != self.n_var: print('The Schaffer N. 2 function is only defined on a 2D space.')
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        sincomponent = np.power( np.sin( np.power(x1, 2) - np.power(x2, 2) ), 2 )

        scores = 0.5 + (sincomponent - 0.5) / np.power( 1 + 0.001 * ( np.power(x1, 2) + np.power(x2, 2) ), 2 )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Schaffer N. 3 function.
% SCORES = SCHAFFERN3FCN(X) computes the value of the Schaffer N. 3  
% function at point X. SCHAFFERN3FCN accepts a matrix of size M-by-2 and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = schaffern3fcn(x)
    n = size(x, 2);
    assert(n == 2, 'Schaffer function N. 3 is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    numeratorcomp = (sin(cos(abs(X .^ 2 - Y .^ 2))) .^ 2) - 0.5; 
    denominatorcomp = (1 + 0.001 * (X .^2 + Y .^2)) .^2 ;
    scores = 0.5 + numeratorcomp ./ denominatorcomp;
end
'''
class schaffern3fcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-100, 100])
        self.plot_bound = np.array([-50, 50])
        self.n_var = 2
        if n_var != self.n_var: print('Schaffer function N. 3 is only defined on a 2D space.')
        self.optimalX = np.array([0, 1.253115])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        numeratorcomp = np.power( np.sin( np.cos( np.abs( np.power(x1, 2) - np.power(x2, 2) ) ) ), 2 ) - 0.5
        denominatorcomp = np.power( 1 + 0.001 * ( np.power(x1, 2) + np.power(x2, 2) ), 2 )
        scores = 0.5 + numeratorcomp / denominatorcomp
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Schaffer N. 4 function.
% SCORES = SCHAFFERN4FCN(X) computes the value of the Schaffer N. 4  
% function at point X. SCHAFFERN4FCN accepts a matrix of size M-by-2 and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = schaffern4fcn(x)
    n = size(x, 2);
    assert(n == 2, 'Schaffer function N. 4 is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    numeratorcomp = (cos(sin(abs(X .^ 2 - Y .^ 2))) .^ 2) - 0.5; 
    denominatorcomp = (1 + 0.001 * (X .^2 + Y .^2)) .^2 ;
    scores = 0.5 + numeratorcomp ./ denominatorcomp;
end
'''
class schaffern4fcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-100, 100])
        self.plot_bound = np.array([-50, 50])
        self.n_var = 2
        if n_var != self.n_var: print('Schaffer function N. 4 is only defined on a 2D space.')
        self.optimalX = np.array([0, 1.253115])
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        numeratorcomp = np.power( np.cos( np.sin( np.abs( np.power(x1, 2) - np.power(x2, 2) ) ) ), 2 ) - 0.5
        denominatorcomp = np.power( 1 + 0.001 * ( np.power(x1, 2) + np.power(x2, 2) ), 2 )
        scores = 0.5 + numeratorcomp / denominatorcomp
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Schwefel 2.20 function.
% SCORES = SCHWEFEL220FCN(X) computes the value of the Schwefel 2.20 
% function at point X. SCHWEFEL220FCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = schwefel220fcn(x)
    scores = sum(abs(x), 2);
end
'''
class schwefel220fcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-100, 100])
        self.plot_bound = np.array([-10, 10])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = np.sum( np.abs(X), axis=1 )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Schwefel 2.21 function.
% SCORES = SCHWEFEL221FCN(X) computes the value of the Schwefel 2.21 
% function at point X. SCHWEFEL221FCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = schwefel221fcn(x)
    scores = max(abs(x), [], 2);
end
'''
class schwefel221fcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-100, 100])
        self.plot_bound = np.array([-10, 10])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = np.max( np.abs(X), axis=1 )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Schwefel 2.22 function.
% SCORES = SCHWEFEL222FCN(X) computes the value of the Schwefel 2.22 
% function at point X. SCHWEFEL222FCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = schwefel222fcn(x)

    absx = abs(x);
    scores = sum(absx, 2) + prod(absx, 2);
end
'''
class schwefel222fcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-100, 100])
        self.plot_bound = np.array([-10, 10])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        absx = np.abs(X)
        scores = np.sum(absx, axis=1) + np.prod(absx, axis=1)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Schwefel 2.23 function.
% SCORES = SCHWEFEL223FCN(X) computes the value of the Schwefel 2.23 
% function at point X. SCHWEFEL223FCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = schwefel223fcn(x)
    scores = sum(x .^10, 2);
end
'''
class schwefel223fcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-10, 10])
        self.plot_bound = self.boundaries
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = np.sum( np.power(X, 10), axis=1)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Schwefel benchmark function.
% SCORES = SCHWEFELFCN(X) computes the value of the Schwefel function at 
% point X. SCHWEFELFCN accepts a matrix of size M-by-2 and returns a  
% vetor SCORES of size M-by-1 in which each row contains the function value 
% for the corresponding row of X.
% For more information please visit: 
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = schwefelfcn(x)
    n = size(x, 2);
    scores = 418.9829 * n - (sum(x .* sin(sqrt(abs(x))), 2));
end
'''
class schwefelfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-500, 500])
        self.plot_bound = self.boundaries
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var) + 420.968746
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = 418.982887272433799807913601398 * self.n_var - np.sum( X * np.sin( np.sqrt( np.abs(X) ) ), axis=1 )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of Sphere benchmark function.
% SCORES = SPHEREFCN(X) computes the value of the Ackey function at 
% point X. SPHEREFCN accepts a matrix of size M-by-N and returns a vetor 
% SCORES of size M-by-1 in which each row contains the function value for
% each row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function f = spherefcn(x)
    f = sum(x .^ 2, 2);
end
'''
class spherefcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-5.12, 5.12])
        self.plot_bound = np.array([-5, 5])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = np.sum( np.power(X, 2), axis=1 )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Styblinski-Tank benchmark function.
% SCORES = STYBLINSKITANKFCN(X) computes the value of the Styblinski-Tank  
% function at point X. STYBLINSKITANKFCN accepts a matrix of size M-by-2 
% and returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = styblinskitankfcn(x)
    n = size(x, 2);
    scores = 0;
    for i = 1:n
        scores = scores + ((x(:, i) .^4) - (16 * x(:, i) .^ 2) + (5 * x(:, i)));
    end
    scores = 0.5 * scores;
end
'''
class styblinskitankfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-5, 5])
        self.plot_bound = self.boundaries
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var) - 2.903534
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = 0
        for i in range(self.n_var):
            scores = scores + ( np.power(X[:, i], 4) - 16 * np.power(X[:, i], 2) + 5 * X[:, i] )
        scores = 0.5 * scores
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Sum Squares function.
% SCORES = SUMSQUARESFCN(X) computes the value of the Sum Squares
% function at point X. SUMSQUARESFCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = sumsquaresfcn(x)
   
   [m, n] = size(x);
   x2 = x .^2;
   I = repmat(1:n, m, 1);
   scores = sum( I .* x2, 2);
   
end
'''
class sumsquaresfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-10, 10])
        self.plot_bound = self.boundaries
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x2 = np.power(X, 2)
        I = np.arange(1, self.n_var + 1)
        scores = np.sum( I * x2, axis=1 )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Three-hump camel benchmark function.
% SCORES = THREEHUMPCAMELFCN(X) computes the value of the Three-hump camel   
% function at point X. THREEHUMPCAMELFCN accepts a matrix of size M-by-2  
% and returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information please visit: 
% https://en.wikipedia.org/wiki/Test_functions_for_optimization
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = threehumpcamelfcn(x)
    
    n = size(x, 2);
    assert(n == 2, 'The Three-hump camel function is only defined on a 2D space.')
    X = x(:, 1);
    Y = x(:, 2);
    
    scores = (2 * X .^ 2) - (1.05 * (X .^ 4)) + ((X .^ 6) / 6) + X .* Y + Y .^2;
end
'''
class threehumpcamelfcn():
    def __init__(self, n_var=2):
        self.boundaries = np.array([-5, 5])
        self.plot_bound = np.array([-2, 2])
        self.n_var = 2
        if n_var != self.n_var: print('The Three-hump camel function is only defined on a 2D space.')
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]

        scores = 2 * np.power(x1, 2) - 1.05 * np.power(x1, 4) + ( np.power(x1, 6) / 6 ) + x1 * x2 + np.power(x2, 2)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Wolfe function.
% SCORES = WOLFEFCN(X) computes the value of the Wolfe 
% function at point X. WOLFEFCN accepts a matrix of size M-by-3 and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information, please visit:
% benchmarkfcns.xyz/fcns/wolfefcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = wolfefcn(x)
    n = size(x, 2);
    assert(n == 3, 'The Wolfe function is defined only on the 3-D space.')
    X = x(:, 1);
    Y = x(:, 2);
    Z = x(:, 3);
    
    scores = (4/3)*(((X .^ 2 + Y .^ 2) - (X .* Y)).^(0.75)) + Z;
end 
'''
class wolfefcn():
    def __init__(self, n_var=3):
        self.boundaries = np.array([0, 2])
        self.plot_bound = self.boundaries
        self.n_var = 3
        if n_var != self.n_var: print('The Wolfe function is defined only on the 3-D space.')
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        x1 = X[:, 0]
        x2 = X[:, 1]
        x3 = X[:, 2]

        scores = (4/3) * np.power( np.power(x1, 2) + np.power(x2, 2) - (x1 * x2), 0.75 ) + x3
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Xin-She Yang function.
% SCORES = XINSHEYANGN1FCN(X) computes the value of the Xin-She Yang
% function at point X. XINSHEYANGN1FCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information, please visit:
% benchmarkfcns.xyz/fcns/xinsheyangn1fcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = xinsheyangn1fcn(x)
    n = size(x, 2);

    scores = 0;
    for i = 1:n
        scores = scores + rand * (abs(x(:, i)) .^ i);
    end
end 
'''
class xinsheyangn1fcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-5, 5])
        self.plot_bound = self.boundaries
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = 0
        for i in range(self.n_var):
            scores = scores + np.random.rand(X.shape[0]) * np.power( np.abs(X[:, i]), i + 1 )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Xin-She Yang N. 2 function.
% SCORES = XINSHEYANGN2FCN(X) computes the value of the Xin-She Yang N. 2
% function at point X. XINSHEYANGN2FCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information, please visit:
% benchmarkfcns.xyz/fcns/xinsheyangn2fcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = xinsheyangn2fcn(x)
     scores = sum(abs(x), 2) .* exp(-sum(sin(x .^2), 2));
end 
'''
class xinsheyangn2fcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-2 * np.pi, 2 * np.pi])
        self.plot_bound = np.array([-10, 10])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = np.sum( np.abs(X), axis=1) * np.exp( -np.sum( np.sin( np.power(X, 2) ), axis=1) )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Xin-She Yang N. 3 function.
% The Xin-She Yang N. 3 function is a parametric function and it is
% behaviour can be controlled with two additional parameters 'beta' and 
% 'm'. In this implementation, the parameters are optional and when not
% given, their default value will be used. 
% SCORES = XINSHEYANGN3FCN(X) computes the value of the Xin-She Yang N. 3
% function at point X. XINSHEYANGN3FCN accepts a matrix of size P-by-N and 
% returns a vetor SCORES of size P-by-1 in which each row contains the 
% function value for the corresponding row of X. In this case, the default
% values of 'm=5' and 'beta=15' is used for function parameters. 
% SCORES = XINSHEYANGN3FCN(X, BETA) computes the function with the given
% value of BETA for its 'beta' parameter. In this case, the default value
% of 'm=5' will be used for the parameter. 
% SCORES = XINSHEYANGN3FCN(X, BETA, M) computes the function with the given
% value of M for its 'm' parameter.
% For more information, please visit:
% benchmarkfcns.xyz/fcns/xinsheyangn3fcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = xinsheyangn3fcn(x, beta, m)
   if nargin < 2
       beta = 15;
   end
   if nargin < 3
       m = 5;
   end
   
   scores = exp(-sum((x / beta).^(2*m), 2)) - (2 * exp(-sum(x .^ 2, 2)) .* prod(cos(x) .^ 2, 2));
end 
'''
class xinsheyangn3fcn():
    def __init__(self, n_var=10, beta=15, m=5):
        self.boundaries = np.array([-2 * np.pi, 2 * np.pi])
        self.plot_bound = np.array([-10, 10])
        self.beta = beta
        self.m = m
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = np.exp( -np.sum( np.power(X / self.beta, 2 * self.m), axis=1 ) ) - \
            ( 2 * np.exp( -np.sum( np.power(X, 2), axis=1 ) ) * np.prod( np.power( np.cos(X), 2 ), axis=1 ) )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of the Xin-She Yang N. 4 function.
% SCORES = XINSHEYANGN4FCN(X) computes the value of the Xin-She Yang N. 4
% function at point X. XINSHEYANGN4FCN accepts a matrix of size M-by-N and 
% returns a vetor SCORES of size M-by-1 in which each row contains the 
% function value for the corresponding row of X.
% For more information, please visit:
% benchmarkfcns.xyz/fcns/xinsheyangn4fcn
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = xinsheyangn4fcn(x)
     scores = (sum(sin(x) .^2, 2) - exp(-sum(x .^ 2, 2))) .* exp(-sum(sin(sqrt(abs(x))) .^2, 2));
end 
'''
class xinsheyangn4fcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-10, 10])
        self.plot_bound = self.boundaries
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        scores = ( np.sum( np.power( np.sin(X), 2 ), axis=1 ) - np.exp( -np.sum( np.power(X, 2), axis=1 ) ) ) * \
            np.exp( -np.sum( np.power( np.sin( np.sqrt( np.abs(X) ) ), 2 ), axis=1 ) )
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()

'''ORIGINAL MATLAB IMPLEMENTATION
% Computes the value of Zakharov benchmark function.
% SCORES = ZAKHAROVFCN(X) computes the value of the Zakharov function at 
% point X. ZAKHAROVFCN accepts a matrix of size M-by-N and returns a vetor 
% SCORES of size M-by-1 in which each row contains the function value for
% each row of X.
% 
% Author: Mazhar Ansari Ardeh
% Please forward any comments or bug reports to mazhar.ansari.ardeh at
% Google's e-mail service or feel free to kindly modify the repository.
function scores = zakharovfcn(x)

    n = size(x, 2);
    comp1 = 0;
    comp2 = 0;
    
    for i = 1:n
        comp1 = comp1 + (x(:, i) .^ 2);
        comp2 = comp2 + (0.5 * i * x(:, i));
    end
     
    scores = comp1 + (comp2 .^ 2) + (comp2 .^ 4);
end
'''
class zakharovfcn():
    def __init__(self, n_var=10):
        self.boundaries = np.array([-5, 10])
        self.plot_bound = np.array([-10, 10])
        self.n_var = n_var
        self.optimalX = np.zeros(self.n_var)
        self.optimalF = self.f(self.optimalX)

    def F(self, X):
        comp1 = 0
        comp2 = 0

        for i in range(self.n_var):
            comp1 = comp1 + np.power(X[:, i], 2)
            comp2 = comp2 + 0.5 * (i + 1) * X[:, i]

        scores = comp1 + np.power(comp2, 2) + np.power(comp2, 4)
        return scores

    def f(self, x):
        return self.F(x[None, :]).item()