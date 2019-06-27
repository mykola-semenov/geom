import argparse
import json

from argtypes import *
from wavetypes import *

def parse_args():
    parser = argparse.ArgumentParser(description='Wavy boundary geometry generator.',
                                     add_help=False)
    
    parser.add_argument('filename', help='an output TSV file')
    
    parser.add_argument('-N', metavar='N', type=non_negative_int, default=8, dest='N',
                        help='number of waves, default 8')
    parser.add_argument('-n', metavar='n', type=positive_int, default=24, dest='n',
                        help='wave resolution, desirable to be even, default 24')
    
    parser.add_argument('-l', '--length', metavar='l', type=non_negative_float, default=12, dest='l',
                        help='wave length, default 12')
    parser.add_argument('-h', '--height', metavar='h', type=positive_float, default=1.8, dest='h',
                        help='wave height, default 1.8')

    parser.add_argument('-t', '--type', type=str, choices=curves.keys(), default='circle', 
                        dest='type', help=f'wave type, default circle')

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
            'type': args.type,
        }
        with open('settings.json', 'w') as f:
            json.dump(settings, f, indent='\t')
    
    if args.load_settings:
        with open('settings.json', 'r') as f:
            settings = json.load(f)
        args.N = settings['N']
        args.n = settings['n']
        args.l = settings['l']
        args.h = settings['h']
        args.type = settings['type']


    if args.n % 2 != 0:
        print('Consider using even n.')

    X_max = 200.0
    Y_max = 42.0

    model_length = 310.0 # ?
    dist = 154.0 # dist from rear
    wavy_len = (args.N + 0.5) * args.l # Why 0.5?
    shift = 2.0 # shift from the sketch (?)
    
    X_0 = model_length - dist - wavy_len - shift
    print(f'X_0 = {X_0}')
        
    return (
        args.N, args.n,
        args.l, args.h, 
        X_0, X_max, Y_max,
        curves[args.type]
    )

if __name__ == '__main__':
    args = parse_args()

    N, n, l, h, X_0, X_max, Y_max, y = process(args)

    X = [X_0 + i * l / n for i in range((N + 1) * n + 1)]
    
    Y = [y(x, l, h) for x in [0.5 * i * l / (n // 2 + n % 2) for i in range(n // 2 + n % 2)]]
    Y += [y(x, l, h) for x in [(i / n - 0.5) * l for i in range(n)]] * N
    Y += [y(x, l, h) for x in [(0.5 * i / (n // 2) - 0.5) * l for i in range(n // 2 + 1)]]

    # de-dimensionalize
    X = [x / 100.0 for x in X]
    Y = [y / 100.0 for y in Y]
    X_max /= 100.0
    Y_max /= 100.0

    with open(args.filename, 'w') as f:
        f.write(f'{0.0}\t{0.0}\t"1"\n')
        for x, y in zip(X, Y):
            f.write(f'{x}\t{y}\t""\n')
        f.write(f'{X_max}\t{0.0}\t"1"\n')
        f.write(f'{X_max}\t{Y_max}\t"1"\n')
        f.write(f'{0.0}\t{Y_max}\t"1 *"\n')