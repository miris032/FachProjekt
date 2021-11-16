import pandas as pd


def getPosFromCsv():
    file = pd.read_csv("nc_tasche.csv", sep=' ', header=None)
    csvlist = file.values.tolist()

    """xList = []
    yList = []
    zList = []"""
    posList = []

    for i in range(len(csvlist)):
        """xList.append(csvlist[i][0])
        yList.append(csvlist[i][1])
        zList.append(csvlist[i][2])"""
        posList.append((csvlist[i][0], csvlist[i][1], csvlist[i][2]))

    return posList

if __name__ == '__main__':
    print(getPosFromCsv())



