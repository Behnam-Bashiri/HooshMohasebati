import sys

import matplotlib.pyplot as plt
import math

DataChart = dict()


def Quantification(A, C):
    for x in range(0, 2 * C + 1):
        y = 1 / (1 + (math.exp((-1 * A) * (x - C))))
        DataChart[x] = y
    return DataChart


def DrawChart(Xlist, YList):
    plt.plot(Xlist, YList, color='brown')
    plt.xlabel("X")
    plt.ylabel("MF")
    plt.title("This is Sigmoid Chart ")
    plt.show()


def start():
    print("Behnam Bashiri - SC:98405016")
    selector = int(input("1. Quantification\n2. Auto Draw 1\n3. Auto Draw 2\n4. Exit\n->"))
    if selector == 1:
        A = int(input("Enter A (int value) :\n"))
        C = int(input("Enter C (int value) :\n"))
        ResultDict = Quantification(A=A, C=C)
        x = list(ResultDict.keys())
        y = list(ResultDict.values())
        DrawChart(Xlist=x, YList=y)
        start()

    elif selector == 2:
        ResultDict = Quantification(A=1, C=5)
        x = list(ResultDict.keys())
        y = list(ResultDict.values())
        DrawChart(Xlist=x, YList=y)
        start()

    elif selector == 3:
        ResultDict = Quantification(A=2, C=4)
        x = list(ResultDict.keys())
        y = list(ResultDict.values())
        DrawChart(Xlist=x, YList=y)
        start()

    elif selector == 4:
        sys.exit()


start()
