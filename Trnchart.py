import sys

import matplotlib.pyplot as plt

DataChart = dict()


def Quantification(A, B, C):
    if A > B > C:
        print("Item not match!")
    elif A == B:
        print("Item not match!")
    elif A == C:
        print("Item not match!")
    else:
        for x in range(0, A):
            y = 0
            DataChart[x] = y
        for x in range(A, B):
            y = (x - A) / (B - A)
            if 0 <= y <= 1:
                DataChart[x] = y
        for x in range(B, C):
            y = (C - x) / (C - B)
            if 0 <= y <= 1:
                DataChart[x] = y
        for x in range(C, C + 5):
            y = 0
            DataChart[x] = y
    return DataChart


def DrawChart(Xlist, YList):
    plt.plot(Xlist, YList, color='pink')
    plt.xlabel("X")
    plt.ylabel("MF")
    plt.title("This is Triangle Chart ")
    plt.show()


def start():
    print("Behnam Bashiri - SC:98405016")
    selector = int(input("1. Quantification\n2. Auto Draw 1\n3. Auto Draw 2\n4. Exit\n->"))
    if selector == 1:
        A = int(input("Enter A (int value) :\n"))
        B = int(input("Enter B (int value) :\n"))
        C = int(input("Enter C (int value) :\n"))
        ResultDict = Quantification(A=A, B=B, C=C)
        x = list(ResultDict.keys())
        y = list(ResultDict.values())
        DrawChart(Xlist=x, YList=y)
        start()

    elif selector == 2:
        ResultDict = Quantification(A=1, B=3, C=5)
        x = list(ResultDict.keys())
        y = list(ResultDict.values())
        DrawChart(Xlist=x, YList=y)
        start()

    elif selector == 3:
        ResultDict = Quantification(A=2, B=5, C=9)
        x = list(ResultDict.keys())
        y = list(ResultDict.values())
        DrawChart(Xlist=x, YList=y)
        start()

    elif selector == 4:
        sys.exit()


start()
