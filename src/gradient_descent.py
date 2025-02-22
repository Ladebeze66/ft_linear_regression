import numpy as np
from cost_function import compute_cost

def gradient_descent(X, y, theta_0, theta_1, learning_rate, iterations):
    """Applique la descente de gradient et retourne les paramètres optimisés."""
    m = len(y)
    cost_history = [] # Historique des coûts pour visualisation
    
    for i in range(iterations):
        predictions = theta_0 + theta_1 * X
        error = predictions - y
        
        d_theta_0 = (1 / m) * np.sum(error)
        d_theta_1 = (1 / m) * np.sum(error * X)
        
        theta_0 -= learning_rate * d_theta_0
        theta_1 -= learning_rate * d_theta_1
        
        cost = compute_cost(theta_0, theta_1, X, y)
        cost_history.append(cost)
        
        if i % 100 == 0:
            print(f"Iteration {i} : theta_0 = {theta_0}, theta_1 = {theta_1}, cost = {cost}")
    
    return theta_0, theta_1, cost_history