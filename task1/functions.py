from math import *

def prod_non_zero_diag(x):
    ans = 1
    if len(x)==0:
        return ans
    
    for i in range(min(len(x), len(x[0]))):
        if x[i][i] != 0:
            ans *= x[i][i]
    return ans


def are_multisets_equal(x, y):
    if len(x) != len(y):
        return False
    return sorted(x) == sorted(y)


def max_after_zero(x):
    max_val = None
    
    for i in range(len(x) - 1):
        if x[i] == 0:
            if max_val is None or x[i + 1] > max_val:
                max_val = x[i + 1]
    
    return max_val if max_val is not None else 0


def convert_image(img, coefs):
    res = []
    
    for i in range(len(img)):
        new_row = []
        for j in range(len(img[i])):
            total = 0
            for k in range(len(coefs)):
                total += img[i][j][k] * coefs[k]
            new_row.append(total)
        res.append(new_row)
    
    return res


def run_length_encoding(x):
    if len(x)==0:
        return [], []
    
    values = [x[0]]
    counts = [1]
    
    for num in x[1:]:
        if num == values[-1]:
            counts[-1] += 1
        else:
            values.append(num)
            counts.append(1)
    
    return values, counts


def pairwise_distance(x, y):
    result = []
    
    for i in range(len(x)):
        row_distances = []
        for j in range(len(y)):
            dx = x[i][0] - y[j][0]
            dy = x[i][1] - y[j][1]
            distance = sqrt(dx*dx + dy*dy)
            row_distances.append(distance)
        result.append(row_distances)
    
    return result