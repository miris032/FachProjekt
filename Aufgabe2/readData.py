import pandas as pd
import matplotlib.pyplot as plt




def getData():
    file = pd.read_csv("OberflächentopographieDatei.txt", sep=' ', header=None)
    dataList = file.values.tolist()
    return dataList


def getData2():
    file = pd.read_csv("OberflächentopographieDatei2.txt", sep=' ', header=None)
    dataList = file.values.tolist()
    return dataList


if __name__ == '__main__':

    '''list1 = getData()[0]
    n1 = len(getData()[0])
    print(list1)
    print(n1)
    print()

    plt.plot(list(range(1, n1+1)), list1)
    plt.show()'''

    print(getData())





    