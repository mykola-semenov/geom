import argparse

def positive_int(s):
    x = int(s)
    if x <= 0:
        raise argparse.ArgumentTypeError('{} is not positive'.format(s))
    return x

def non_negative_int(s):
    x = int(s)
    if x < 0:
        raise argparse.ArgumentTypeError('{} is negative'.format(s))
    return x

def positive_float(s):
    x = float(s)
    if x <= 0:
        raise argparse.ArgumentTypeError('{} is not positive'.format(s))
    return x

def non_negative_float(s):
    x = float(s)
    if x < 0:
        raise argparse.ArgumentTypeError('{} is not positive'.format(s))
    return x