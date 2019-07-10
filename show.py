#!/bin/env python3

from argparse import ArgumentParser
from matplotlib import pyplot as plt

def parse_args():
    parser = ArgumentParser(description='Plot boundary geometry from file.')
    parser.add_argument('filename', metavar='filename',
                        help='an input TSV file with boundary points')
    return parser.parse_args()

if __name__ == '__main__':
    
    args = parse_args()
    
    X = []
    Y = []
    with open(args.filename, 'r') as f:
        for line in f:
            x, y = tuple(map(float, line.split('\t')[:2]))
            X.append(x)
            Y.append(y)
    
    X.append(X[0])
    Y.append(Y[0])
    
    plt.plot(X, Y)
    plt.show()