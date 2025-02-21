import numpy as np

def minimize (A, b, x_init=None, alpha=0, TOL=1e-6, rel_conv=True, MAX_ITER=100):
    """
    Minimizes the quadratic problem 1/2 x^T*A*x - b^T*x using steepest descent

    Parameters:
    A (np.array)        : Matrix A
    b (np.array)        : Vector b
    x_init (np.array)   : initial guess
    alpha (double)      : Step size. If alpha=0, we use steepest descent
    TOL (double)        : Stopping tolerance of ||x_{k+1} - x_k||
    rel_conv (bool)     : Whether to use relative convergence
    MAX_ITER (int)      : Maximal number of iterations

    Returns:
    array : Minimum
    """

    d = 2*TOL
    k = 0

    xks = []

    if x_init is None:
        x_init = np.zeros(A.shape[1])
    x = x_init

    while (d > TOL and k < MAX_ITER):

        #Write your code here
        grad = x.T@A - b
        
        if not alpha:
            a = (grad.T @ grad) / (grad.T @ A @ grad)
            x = x - a * grad
        else:
            x = x - alpha * grad

        k += 1
        d = np.linalg.norm(grad)
        
        xks.append(x)

    return xks

if __name__ == '__main__':
    def f(x:np.ndarray, A:np.ndarray, b:np.ndarray) -> np.float64:
        return 0.5 * x.T@A@x - x.T@b
    
    def grad_f(x:np.ndarray, A:np.ndarray, b:np.ndarray) -> np.ndarray:
        return x.T@A - b
    
    A = np.array([[4, 0],
                 [0, 1]])

    b = np.array([1, 2])

    x = np.ones_like(b)

    grad = grad_f(x, A, b)  # this is a vector
    alpha = (grad.T @ grad) / (grad.T @ A @ grad)
    print(grad_f(x, A, b))
    print(f(x, A, b))
    print(grad)
    print(alpha)

    print(minimize(A, b))