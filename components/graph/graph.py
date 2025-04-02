import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def plot_graph(x, y, title='Graph', xlabel='X-axis', ylabel='Y-axis'):
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, marker='o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()
