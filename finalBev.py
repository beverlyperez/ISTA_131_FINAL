import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd, numpy as np

def SalesInRegion():
    df = pd.read_csv('vgsales.csv', index_col=0)
    dfM = df.mean()
    mod = dfM[1:]
    data = mod.T
    plt.title("Popular Region")
    plt.ylabel("Sales (in Millions)", fontsize=20)
    plt.xlabel("Regions", fontsize=20)
    data.plot.bar(rot=0)

def PopularGenre():
    df3 = pd.read_csv('vgsales.csv', index_col=0)
    temp = df3.nlargest(3, ['Global_Sales'])
    dfT = pd.DataFrame(temp, columns = ["Genre", "Global_Sales"])
    genre = list(dfT["Genre"])
    glo = list(dfT["Global_Sales"])
    df2 = pd.DataFrame(glo, genre)
    plt.title("Customer Popular Genre")
    plt.ylabel("Sales (in Millions)", fontsize=20)
    plt.xlabel("Genre", fontsize=20)
    df2.plot.bar(rot=4)

def AmountOfGenres():
    df = pd.read_csv('vgsales.csv', index_col=0)
    li = []
    cou = []
    temp = list(df["Genre"].values)
    for i in temp:
        if i not in li:
            li.append(i)
        
    for i in li:
        te = temp.count(i)
        cou.append(te)
    #df2 = pd.DataFrame(cou, li)
    #df2.plot.bar()
    plt.plot
    plt.title("Popular Genre Among Companies")
    plt.ylabel("Number Released", fontsize=20)
    plt.xlabel("Genre", fontsize=20)


def main():
    SalesInRegion()
    PopularGenre()
    AmountOfGenres()