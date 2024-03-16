import numpy as np
import matplotlib.pyplot as plt

def xyplot(start: float, end: float, num: int):
    x = np.linspace(start, end, num)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()
    
def hello(x: int) -> int:
    print("Hello, World!")
    print("x = ", x)
    
    return x + 1
