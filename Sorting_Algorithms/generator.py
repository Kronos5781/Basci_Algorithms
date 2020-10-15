import numpy as np


# Random Gen Class
class RandomArrayGenerator:

    def gen_array(self, range, size):
        arr = np.random.randint(1, range, size)
        return arr