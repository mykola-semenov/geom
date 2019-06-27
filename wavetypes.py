import math

def circle(x, l, h):
    if l <= 2 * h:
        raise ValueError('l / 2 must be greater than h')

    r = 0.125 * l ** 2 / h + 0.5 * h
    return abs(r ** 2 - x ** 2) ** 0.5 - r

def smooth_cos(x, l, h):
    return 0.5 * h * (math.cos(2 * math.pi * x / l) - 1)

def sharp_cos(x, l, h):
    return h * (math.cos(math.pi * x / l) - 1)

def saw(x, l, h):
    return - abs(2 * h * x / l)

def cos(x, l, h, alpha=90):
    """ 
    Волна с заданным углом стыка, нужно численно решать
    алгебраическое уравнение вида:
                x * sin(x) = C * (cos(x) - 1) 
    """
    pass


curves = {
    'circle': circle,
    'smooth-cos': smooth_cos,
    'sharp-cos': sharp_cos,
    'saw': saw,
}