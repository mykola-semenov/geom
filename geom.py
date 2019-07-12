#!/bin/env python3

import argparse
import json

from argtypes import *
from wavetypes import *
from outformat import *

def parse_args():
    parser = argparse.ArgumentParser(description='Wavy boundary geometry generator.',
                                     add_help=False)
    
    parser.add_argument('filename', help='an output TSV file')
    
    parser.add_argument('-N', metavar='N', type=non_negative_int, default=8, dest='N',
                        help='number of waves, default 8')
    parser.add_argument('-n', metavar='n', type=positive_int, default=24, dest='n',
                        help='wave resolution, desirable to be even, default 24')
    
    parser.add_argument('-l', '--length', metavar='l', type=non_negative_float, default=0.06, dest='l',
                        help='wave length, default 0.06')
    parser.add_argument('-h', '--height', metavar='h', type=positive_float, default=0.009, dest='h',
                        help='wave height, default 0.009')
    
    parser.add_argument('-L', '--model-length', metavar='L', type=non_negative_float, default=1, dest='L',
                        help='model length, default 1.0')
    parser.add_argument('-H', '--grid-height', metavar='H', type=non_negative_float, default=0.21, dest='H',
                        help='height of area of calculation (for gridgen output format), default 0.21')    
    parser.add_argument('-d', '--distance', metavar='d', type=non_negative_float, default=0.26, dest='d',
                        help='distance from leading edge, default 0.26')

    parser.add_argument('-t', '--type', type=str, choices=curves.keys(), default='circle', 
                        dest='type', help='wave type, default circle')
    parser.add_argument('-f', '--output-format', type=str, choices=formats.keys(), default='gridgen', 
                        dest='format', help='output format, default gridgen')

    parser.add_argument('--load-settings', action='store_true', dest='load_settings',
                        help='load settings from settings.json')
    parser.add_argument('--save-settings', action='store_true', dest='save_settings',
                        help='save settings to settings.json')

    parser.add_argument('--help', action='help', help='show this help message and exit')
    
    return parser.parse_args()

def process(args):
    if args.save_settings:
        settings = {
            'N': args.N,
            'n': args.n,
            'l': args.l,
            'h': args.h,
            'L': args.L,
            'd': args.d,
            'type': args.type,
        }
        with open('settings.json', 'w') as f:
            json.dump(settings, f, indent=4, sort_keys=True) # in python2.7 indent='\t' does not work
    
    if args.load_settings:
        with open('settings.json', 'r') as f:
            settings = json.load(f)
        args.N = settings['N']
        args.n = settings['n']
        args.l = settings['l']
        args.h = settings['h']
        args.L = settings['L']
        args.d = settings['d']
        args.type = settings['type']

    if args.n % 2 != 0:
        print('Consider using even n.')


if __name__ == '__main__':
    args = parse_args()
    process(args)
    
    N = args.N
    n = args.n
    l = args.l
    h = args.h
    
    y = curves[args.type]
    
    X_0 = args.d
    X_max = args.L
    Y_max = args.H
    
    X = [X_0 + i * float(l) / float(n) for i in range((N + 1) * n + 1)]
    
    Y = [y(x, l, h) for x in [0.5 * i * l / (n // 2 + n % 2) for i in range(n // 2 + n % 2)]]
    Y += [y(x, l, h) for x in [(float(i) / float(n) - 0.5) * l for i in range(n)]] * N # float for Python 2 support
    Y += [y(x, l, h) for x in [(0.5 * i / (n // 2) - 0.5) * l for i in range(n // 2 + 1)]]

    with open(args.filename, 'w') as f:
        if args.format == 'gridgen':
            gridgen(f, X, Y, 0.0, X_max, 0.0, Y_max)
        elif args.format == 'segment':
            segment(f, X, Y)
        else:
            pass