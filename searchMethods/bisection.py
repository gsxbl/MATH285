def solve (f_deriv, a, b, TOL=1e-6, MAX_ITER=1000, verbose=0):
    """
    minimize f(x) over domain [a, b]

    Parameters:
    f_deriv (function)  : Derivative f' of f
    a (double)          : Left endpoint of domain [a, b]
    b (double)          : Right endpoint of domain [a, b]
    TOL (double)        : Stopping tolerance of b_k - a_k
    MAX_ITER (int)      : Maximal number of iterations

    Returns:
    double : Minimum
    """
    k = 0
    d = b - a
    xk = (a + b) / 2

    # Check if we by some amazing luck already found the solution
    if f_deriv(xk) == 0:
        return xk

    while (k < MAX_ITER and d > TOL):

        #Write your code here
        if f_deriv(xk) < 0:
            a, xk = xk, (xk + b) / 2
        if f_deriv(xk) > 0:
            b, xk = xk, (a + xk) / 2
        
        d = b - a
        k += 1
        # END OF MY CODE

        if verbose == 1:
            print("After {} iteration(s), the estimate xk = {}".format(k, xk))

    if k == MAX_ITER:
        print("Maximum is reached! The estimate of the minimmum is : {}".format(xk))
    if k < MAX_ITER:
        print("Solution found to tolerance level! The estimate of the minimmum is : {}".format(xk))
    return xk # maximum iteration reached


if __name__ == '__main__':
    # f(x) = x**2 -> dfdx = 2*x:
    # min f(x**2) over [-1, 5], true solution is 0:

    def dfdx(x):
        return 2*x
    
    solve(dfdx, -1, 5, verbose=True)
