from utils import modP, leadingZerosArr

def multiplication(f, g, p: int):
    #Reduce input coefficients modulo p to keep them in [0, p)
    f = modP(f, p)
    g = modP(g, p)

    #if either polynomial is zero, the product is zero
    if f==[0] or g==[0]:
        return [0]
    
    #Allocate a result buffer: degree(f*g) = (deg f) + (deg g)
    res_len = len(f) + len(g) - 1
    res = [0] * res_len

    #start a Schoolbook convolution with per-step mod reduction
    for i, a in enumerate(f):
        if a == 0:
            continue #skip zero coefficients
        for j, b in enumerate(g):
            if b == 0:
                continue #skip zero coefficients
            res[i + j] = (res[i + j] + a * b) % p

    #Trim leading high-degree zeros to return the canonical representation
    return leadingZerosArr(res)