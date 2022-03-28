import numpy as np
import math
import itertools

arr = np.array([[1,3,6], [2,3,4], [8,2,1]])

def dele(num):
    global arr
    if num in arr:
        arr = np.setdiff1d(arr, num)
        return arr


def get_diff2d(A, B):
    global arr
    nrows, ncols = A.shape
    dtype = {'names': ['f{}'.format(i) for i in range(ncols)], 'formats': ncols * [A.dtype]}
    arr = np.setdiff1d(A.copy().view(dtype), B.copy().view(dtype))
    return arr



def generate(n):
    pointsList = np.array(list(itertools.product(range(0, n, 1), repeat=3)))

    print(pointsList)
    print(pointsList.shape)

    pointsListNew = pointsList.reshape((-1, n, 3))
    print(pointsListNew)

    print("----------------")
    pointsListNew2 = np.split(pointsListNew, 2, axis=1)
    print(pointsListNew2[0])


if __name__ == '__main__':
    '''# diff 2d test
    print(arr)
    get_diff2d(arr, np.array([2,3,4]))
    print("----------")
    print(arr)
    print(type(arr))'''

    '''print(arr)
    # print(np.where(arr == (2, 3, 4)))
    i = arr.tolist().index([8, 2, 1])
    print(i)'''








