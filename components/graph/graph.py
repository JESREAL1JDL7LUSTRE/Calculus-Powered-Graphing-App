import matplotlib.pyplot as plt
import numpy as np

class Graph:
    @staticmethod
    def plot_graph(x, y, title='Graph', xlabel='X-axis', ylabel='Y-axis'):
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, marker='o', label="Function")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.legend()
        plt.show()
