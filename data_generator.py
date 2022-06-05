from numpy.random import choice
import pandas as pd


heads_tails = ["heads", "tails"]

def add_data(heads_outcome, tails_outcome, count):

    with open("data\experiment_outcome.csv", "a") as data_file:
        data_file.write(f"{count},{heads_outcome},{tails_outcome}\n")


with open("data\experiment_outcome.csv", "w") as f:
    f.write(f"Trials,Heads,Tails\n")


for i in range(1, 5):
    tails, heads = 0, 0
    
    for j in range(100):
        computers_choice = choice(heads_tails)

        if computers_choice == heads_tails[0]:
            heads += 1
        else:
            tails += 1
    
    add_data(heads, tails, i)
df = pd.read_csv("data\experiment_outcome.csv")

with open("data\experiment_outcome.csv", "a") as data_file:
    data_file.write(f"Average,{(df['Heads'].sum() / 400) * 100},{(df['Tails'].sum() / 400) * 100}\n")


print(df)