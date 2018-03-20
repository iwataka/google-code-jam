import numpy as np

def solve(admat):
    det = np.linalg.det(admat - np.transpose(admat))
    if det != 0:
        return None
    return [1,2,3]

T = int(input())
for i in range(T):
    F, P = input().split(' ')
    F, P = int(F), int(P)
    admat = np.zeros(shape=(F, F))
    for j in range(P):
        fa, fb = input().split(' ')
        fa, fb = int(fa), int(fb)
        admat[fa - 1, fb - 1] = 1
    mags = solve(admat)
    result = ' '.join([str(m) for m in mags]) if mags else 'IMPOSSIBLE'
    print("Case #%d: %s" % (i + 1, result))
