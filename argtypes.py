import argparse

def positive_int(s):
    x = int(s)
    if x <= 0:
        raise argparse.ArgumentTypeError(f'{s} is not positive')
    return x

def non_negative_int(s):
    x = int(s)
    if x < 0:
        raise argparse.ArgumentTypeError(f'{s} is negative')
    return x

def positive_float(s):
    x = float(s)
    if x <= 0:
        raise argparse.ArgumentTypeError(f'{s} is not positive')
    return x

def non_negative_float(s):
    x = float(s)
    if x < 0:
        raise argparse.ArgumentTypeError(f'{s} is not positive')
    return x