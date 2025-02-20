def _approx_f_dderiv(f_deriv, x, xp):
    """
    Private function to compute approximation of double derivative of f

    Parameters:
    f_deriv (function)  : Derivative of f
    x (double)          : iterate k
    xp (double)         : iterate k-1

    Returns:
    double : Approximation of second derivative
    """
    return (f_deriv(x) - f_deriv(xp)) / (x - xp)


def solve (f_deriv, x_init1=0, x_init0=.1, TOL=1e-6, MAX_ITER=1000, verbose=0):
    """
    Solve one-dimensional minimization problem using Newton's method.

    Parameters:
    f_deriv (function)  : Derivative of f
    f_dderiv (function) : Second derivative of f
    x_init0 (double)    : First initial guess of minimum
    x_init1 (double)    : Second initial guess of minimum
    TOL (double)        : Stopping tolerance of ||x_{k+1} - x_k||
    MAX_ITER (int)      : Maximal number of iterations
    verbose (0/1)       : Whether to print information

    Returns:
    double : Minimum
    """
    xp = x_init0
    xk = x_init1
    k = 0
    # Check if we by some amazing luck already found the solution
    if f_deriv(xk) == 0:
        print("The initial guess was actually minimum!")
        return xk

    while (k < MAX_ITER):

        #Write your code here
        xk1 = xk - f_deriv(xk) / _approx_f_dderiv(f_deriv, xk, xp)

        if abs(f_deriv(xk1)) < TOL:
            break
        
        xk, xp = xk1, xk
        k += 1
        # END OF MY CODE

        if verbose == 1:
            print("After {} iteration(s), the estimate xk = {}".format(k, xk))

    print("Maximum is reached! The estimate of the minimmum is : {}".format(xk))
    return xk # maximum iteration reached


if __name__ == '__main__':
    def f(x):
        return (x-1)**4
    
    def dfdx(x):
        return 4*(x-1)**3
    
    def d2fd2x(x):
        return 12*(x-1)**2
    
    solve(dfdx, verbose=True)