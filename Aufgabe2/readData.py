import pandas as pd
import matplotlib.pyplot as plt




def getData():
    file = pd.read_csv("OberflächentopographieDatei.txt", sep=' ', header=None)
    dataList = file.values.tolist()
    return dataList
    # plt.imshow(dataList)


# 1373 x 1373


if __name__ == '__main__':

    '''list1 = getData()[0]
    n1 = len(getData()[0])
    print(list1)
    print(n1)
    print()

    plt.plot(list(range(1, n1+1)), list1)
    plt.show()'''

    print(getData())





    