import pandas as pd
import numpy as np
import random

drinks = pd.read_csv("../data/drinks.csv")
new_df_list = []
for row in drinks.iterrows():
    if random.random() > 0.7:
        number_of_duplicates = random.randint(2, 5)
        for _ in range(number_of_duplicates):
            new_df_list.append(list(row[1]))
    else:
        new_df_list.append(list(row[1]))
new_df = pd.DataFrame(new_df_list, columns=drinks.columns).sample(frac=1).reset_index()
new_df.to_csv('../data/drinks_duplicated.csv')
