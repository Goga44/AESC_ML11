import numpy as np
import math

def prod_non_zero_diag(x):
    ans = 1
    if x.size()==0:
        return ans
    
    for i in range(min(len(x), len(x[0]))):
        if x[i][i] != 0:
            ans *= x[i][i]
    return ans

def prod_non_zero_diag(x):
    return np.prod(np.diag(x)[np.diag(x) != 0])


def are_multisets_equal(x, y):
    return np.array_equal(np.sort(x), np.sort(y))


def max_after_zero(x):
    res = np.argwhere(x == 0) + 1
    res = res[res < len(x)]
    a = np.take(x, res)
    if(len(a)>0):
        return a.max() 
    else:
        return None



def convert_image(img, coefs):
    return np.dot(img, coefs)


def run_length_encoding(x):
    d = np.diff(x)
    pos = [0]
    pos = np.append(pos, np.reshape(np.where(d != 0)[0], -1) + 1)
    pos = np.append(pos, len(x))
    counts = np.diff(pos)
    
    pos = np.delete(pos, -1)
    values = x[pos]
    
    return values, counts


def pairwise_distance(x, y):
    return np.linalg.norm(x[:, np.newaxis] - y, axis=2)
