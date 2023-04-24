import pandas as pd
import numpy as np
import random

drinks = pd.read_csv("../data/drinks.csv")

columns = ['beer_servings','spirit_servings','wine_servings','total_litres_of_pure_alcohol']
for row in drinks.iterrows():
    column = np.random.choice(columns)
    row[1][column] = np.nan
    drinks.iloc[row[0]] = row[1]
drinks.to_csv('../data/drinks_mixed.csv')
