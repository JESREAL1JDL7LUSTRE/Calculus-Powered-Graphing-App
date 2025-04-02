import scipy.integrate as spi

class integral:
    def __init__(self, function, lower_bound, upper_bound, num_points=1000):
        self.function = function
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.num_points = num_points

    def calculate(self):
        result, _ = spi.quad(lambda x: self.function.subs('x', x), self.lower_bound, self.upper_bound)
        return result
