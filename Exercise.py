import matplotlib.pyplot as plt

import sys

DataChart = dict()
X2 = list()
Y2 = list()


def Quantification(L, R):
    if L > R:
        print("Item not match!")
    elif L == R:
        print("Item not match!")
    else:
        for x in range(0, L):
            y = 0
            DataChart[x] = y
        for x in range(L, int((L + R) / 2)):
            y = (2 * ((x - L) / (R - L)) ** 2)
            if 0 <= y <= 1:
                DataChart[x] = y
                if y == 0.5:
                    X2.append(x)
                    Y2.append(y)
        for x in range(R, R + 5):
            y = L - (2 * ((R - x) / (R - L)) ** 2)
            if 0 <= y <= 1:
                DataChart[x] = y
                if y == 0.5:
                    X2.append(x)
                    Y2.append(y)

    return DataChart


def DrawChart(Xlist, YList):
    plt.plot(Xlist, YList, color='green',label="this is chart")
    plt.plot(X2, Y2, marker='o', markerfacecolor='orange', label="CrossOverPoint")
    plt.xlabel("X")
    plt.ylabel("MF")
    plt.title("This is Exercise Chart ")
    plt.legend()
    plt.show()


def start():
    print("Behnam Bashiri - SC:98405016")
    selector = int(input("1. Quantification\n2. Auto Draw 1\n3. Auto Draw 2\n4. Exit\n->"))
    if selector == 1:
        L = int(input("Enter L (int value) :\n"))
        R = int(input("Enter R (int value) :\n"))
        ResultDict = Quantification(L=L, R=R)
        x = list(ResultDict.keys())
        y = list(ResultDict.values())
        DrawChart(Xlist=x, YList=y)
        start()

    elif selector == 2:
        ResultDict = Quantification(L=1, R=9)
        x = list(ResultDict.keys())
        y = list(ResultDict.values())
        DrawChart(Xlist=x, YList=y)
        start()

    elif selector == 3:
        ResultDict = Quantification(L=2, R=10)
        x = list(ResultDict.keys())
        y = list(ResultDict.values())
        DrawChart(Xlist=x, YList=y)
        start()

    elif selector == 4:
        sys.exit()


start()
