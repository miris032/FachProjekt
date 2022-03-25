import numpy as np

def check0(p1, p2, r, q):
    vec = p2 - p1
    const = r * np.linalg.norm(vec)
    return (np.dot(q - p1, vec) >= 0 and np.dot(q - p2, vec) <= 0) and (np.linalg.norm(np.cross(q - p1, vec)) <= const)


def check(p1, p2, r, q):
    vec = p2 - p1
    const = r * np.linalg.norm(vec)
    return (np.dot(q - p1, vec) >= 0 and np.dot(q - p2, vec) <= 0) and (np.linalg.norm(np.cross(q - p1, vec)) <= const)


def set_diff2d(A, B):
    nrows, ncols = A.shape
    dtype = {'names': ['f{}'.format(i) for i in range(ncols)], 'formats': ncols * [A.dtype]}
    C = np.setdiff1d(A.copy().view(dtype), B.copy().view(dtype))
    return C


if __name__ == '__main__':
    '''p1 = np.array([0, 0, 0])
    p2 = np.array([0, 0, 3])
    q = np.array([0, 0, 30])
    print(check(p1, p2, 2, q))'''

    '''cylinderPosition = [1, 0, 0]

    p1 = cylinderPosition
    p2 = [p1[0], p1[1], p1[2]+30]
    print(p2)'''

    import numpy as np

    a = np.array([[1, 2, 3], [3, 4, 3], [3, 5, 3], [4, 1, 3], [4, 6, 3]])
    b = np.array([[3, 4, 3], [4, 6, 3]])

    '''a1_rows = a.view([('', a.dtype)] * a.shape[1])
    a2_rows = b.view([('', b.dtype)] * b.shape[1])
    c = np.setdiff1d(a1_rows, a2_rows).view(a.dtype).reshape(-1, a.shape[1])
    print(c)'''

    print(set_diff2d(a, b))


