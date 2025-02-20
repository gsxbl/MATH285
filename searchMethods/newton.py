def solve (f_deriv, f_dderiv, x_init=0, TOL=1e-6, MAX_ITER=1000, verbose=0):
    """
    Solve one-dimensional minimization problem using Newton's method.

    Parameters:
    f_deriv (function)  : Derivative of f
    f_dderiv (function) : Second derivative of f
    x_init (double)     : Initial guess of minimum
    TOL (double)        : Stopping tolerance of ||x_{k+1} - x_k||
    MAX_ITER (int)      : Maximal number of iterations
    verbose (0/1)       : Whether to print information

    Returns:
    double: Minimum
    """
    xk = x_init
    k = 0
    # Check if we by some amazing luck already found the solution
    if f_deriv(xk) == 0:
        print("The initial guess was actually minimum!")
        return xk

    while (k < MAX_ITER):

        #Write your code here:
        xk = xk - f_deriv(xk) / f_dderiv(xk)
        if abs(dfdx(xk)) < TOL:
            break

        k += 1
        # END OF MY CODE

        if verbose == 1:
            print("After {} iteration(s), the estimate xk = {}".format(k, xk))

    print("Maximum is reached! The estimate of the minimmum is : {}".format(xk))
    return xk # maximum iteration reached

if __name__ == '__main__':
    # implement newtons method
    '''For f(x) = (x-1)**4, the true min is at x=1'''
    
    def f(x):
        return (x-1)**4
    
    def dfdx(x):
        return 4*(x-1)**3
    
    def d2fd2x(x):
        return 12*(x-1)**2
    
    solve(dfdx, d2fd2x, verbose=True)
