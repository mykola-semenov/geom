def gridgen(f, X, Y, X_min, X_max, Y_min, Y_max):
    f.write('{}\t{}\t"1"\n'.format(X_min, Y_min))
    for x, y in zip(X, Y):
        f.write('{}\t{}\t""\n'.format(x, y))
    f.write('{}\t{}\t"1"\n'.format(X_max, Y_min))
    f.write('{}\t{}\t"1"\n'.format(X_max, Y_max))
    f.write('{}\t{}\t"1 *"\n'.format(X_min, Y_max))


def segment(f, X, Y):
    f.write('\n'.format(len(X)))
    for x, y in zip(X, Y):
        f.write('{}\t{}\t""\n'.format(x, y))

formats = {
    'gridgen': gridgen,
    'segment': segment,
}