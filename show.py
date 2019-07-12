#!/bin/env python3

from argparse import ArgumentParser
from matplotlib import pyplot as plt

def parse_args():
    parser = ArgumentParser(description='Plot boundary geometry from file.')
    parser.add_argument('filename', metavar='filename',
                        help='an input segment of gridgen file with boundary points')
    return parser.parse_args()

if __name__ == '__main__':
    
    args = parse_args()
    
    X = []
    Y = []
    gridgen = True
    with open(args.filename, 'r') as f:
        for line in f:
            if (len(line.split()) <= 1):
                gridgen = False
                continue
            x, y = tuple(map(float, line.split()[:2]))
            X.append(x)
            Y.append(y)
    if gridgen:
        X.append(X[0])
        Y.append(Y[0])
    
    plt.plot(X, Y)
    plt.show()