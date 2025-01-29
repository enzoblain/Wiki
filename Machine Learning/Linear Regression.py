import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class LinearRegression():
    def __init__(self: object, learning_rate : float = 0.01, max_iterations: int = 1000, convergence_treshold: int = 1e-6) -> None:
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.weights = None
        self.bias = None 
        self.convergence_threshold = convergence_treshold

    def derivativeWeight(self: object, data: pd.DataFrame) -> float:
        return ((data['predicted'] - data['y']) * data['x']).mean() * 2
    
    def derivativeBias(self: object, data: pd.DataFrame) -> float:
        return ((data['predicted'] - data['y']).mean()) * 2
    
    def adamUpdate(self: object, 
                   dW: float, dB: float, 
                   mW: float, mB: float, 
                   vW: float, vB: float, 
                   t: int = 1, 
                   beta1: float = 0.9, beta2: float = 0.999, 
                   epsilon: float = 1e-8) -> None:
        mW = beta1 * mW + (1 - beta1) * dW
        mB = beta1 * mB + (1 - beta1) * dB
        
        vW = beta2 * vW + (1 - beta2) * (dW ** 2)
        vB = beta2 * vB + (1 - beta2) * (dB ** 2)
        
        mW_hat = mW / (1 - beta1 ** t)
        mB_hat = mB / (1 - beta1 ** t)
        
        vW_hat = vW / (1 - beta2 ** t)
        vB_hat = vB / (1 - beta2 ** t)
        
        self.weights -= self.learning_rate * mW_hat / (np.sqrt(vW_hat) + epsilon)
        self.bias -= self.learning_rate * mB_hat / (np.sqrt(vB_hat) + epsilon)

    def loss(self: object, data: pd.DataFrame) -> float:
        return ((data['predicted'] - data['y']) ** 2).mean()
    
    def fit(self: object, data: pd.DataFrame) -> None:
        self.data = data

        self.weights, self.bias = 0.0, 0.0
        previous_loss = float('inf')
    
        beta1 = 0.9
        beta2 = 0.999
        epsilon = 1e-8
    
        mW, vW = 0, 0
        mB, vB = 0, 0
    
        i = 1
        while i <= self.max_iterations:
            data['predicted'] = self.weights * data['x'] + self.bias
            
            dW = self.derivativeWeight(data)
            dB = self.derivativeBias(data)
    
            self.adamUpdate(dW, dB, mW, mB, vW, vB, i, beta1, beta2, epsilon)
            
            current_loss = self.loss(data)
            
            if abs(previous_loss - current_loss) < self.convergence_threshold:
                break

            previous_loss = current_loss
            i += 1

        self.data['predicted'] = self.weights * self.data['x'] + self.bias

    def predict(self: object, value: float) -> pd.DataFrame:
        predicted = self.weights * value + self.bias

        return predicted
    
    def plot(self: object) -> None:
        plt.scatter(self.data['x'], self.data['y'])
        plt.plot(self.data['x'], self.data['predicted'], color='red')
        plt.show()

data = pd.read_csv('datasets/Linear Regression.csv')

model = LinearRegression()
model.fit(data)
print(model.predict(100))
model.plot()