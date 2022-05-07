import sys

import matplotlib.pyplot as plt
import math

DataChart = dict()


def Quantification(Delta, C):
    for x in range(0, 2 * C + 1):
        y = math.exp(-0.5 * ((x - C) / Delta) ** 2)
        DataChart[x] = y
    return DataChart


def DrawChart(Xlist, YList):
    plt.plot(Xlist, YList, color='purple')
    plt.xlabel("X")
    plt.ylabel("MF")
    plt.title("This is Gussy Chart ")
    plt.show()


def start():
    print("Behnam Bashiri - SC:98405016")
    selector = int(input("1. Quantification\n2. Auto Draw 1\n3. Auto Draw 2\n4. Exit\n->"))
    if selector == 1:
        C = int(input("Enter C (int value) :\n"))
        Delta = int(input("Enter Delta (int value) :\n"))
        ResultDict = Quantification(Delta=Delta, C=C)
        x = list(ResultDict.keys())
        y = list(ResultDict.values())
        DrawChart(Xlist=x, YList=y)
        start()

    elif selector == 2:
        ResultDict = Quantification(Delta=1, C=5)
        x = list(ResultDict.keys())
        y = list(ResultDict.values())
        DrawChart(Xlist=x, YList=y)
        start()

    elif selector == 3:
        ResultDict = Quantification(Delta=2, C=4)
        x = list(ResultDict.keys())
        y = list(ResultDict.values())
        DrawChart(Xlist=x, YList=y)
        start()

    elif selector == 4:
        sys.exit()


start()
