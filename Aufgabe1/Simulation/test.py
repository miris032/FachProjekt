import itertools
import numpy as np

pointsList = list(itertools.product(range(0, 150, 10), repeat=3))
pointsList = np.array(pointsList).flatten()

if __name__ == '__main__':
    print(pointsList)
