from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv("data.csv")

df_average = df[df["Trials"] == "Average"]
df = df[df["Trials"] != "Average"]

trials = np.arange(1, 3, 0.5)
bar_width = .2
x_axis_naming = [1, 2, 3, 4, "Average"]

range = [0.8, 3.5]

def graph_representation():
    plt.title("Coin outcomes", fontdict={"fontweight": "bold", "fontsize": 20})
    plt.ylabel("Number of heads/tails (per 100 draws)", fontdict={"fontweight": "bold"})
    plt.xlabel("Trials", fontdict={"fontweight": "bold"})

    # Trial bars
    plt.bar(trials, df["Heads"], width=bar_width, label="Heads", color="grey")
    plt.bar(trials + bar_width, df["Tails"], width=bar_width, label="Tails", color="blue")

    #Average bars
    plt.bar([3], df_average["Heads"], bar_width, label="Av. Heads", color="yellow")
    plt.bar([3 + bar_width], df_average["Tails"], bar_width, label="Av. Tails", color="purple")

    # X and Y labels
    plt.xticks(np.arange(1, 3.5, 0.5) + bar_width/2, x_axis_naming)
    plt.yticks(np.arange(10, 70, 10))

    # Minimum and maximum values
    plt.plot(range, [40, 40], "r--")
    plt.plot(range, [60, 60], "r--")

    # Theoretical probability line
    plt.plot(range, [50, 50], "g")

    plt.legend(bbox_to_anchor=(1,1))
    plt.show()
