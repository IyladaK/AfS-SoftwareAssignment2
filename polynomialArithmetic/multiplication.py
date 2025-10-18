from utils import Poly, modP, leadingZerosArr

def multiplication(f: Poly, g: Poly, p: int) -> Poly:
    f = modP(f, p)
    g = modP(g, p)

    if f==[0] or g==[0]:
        return [0]
    
    res_len = len(f) + len(g) - 1
    res = [0] * res_len
    for i, a in enumerate(f):
        if a == 0:
            continue
        for j, b in enumerate(g):
            if b == 0:
                continue
            res[i + j] = (res[i + j] + a * b) % p

    return leadingZerosArr(res)