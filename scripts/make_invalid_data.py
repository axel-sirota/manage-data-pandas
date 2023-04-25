import datetime
import random

import numpy as np
import pandas as pd

number_of_rows = 10000
sensor_type = ["temperature", "weight", "light", "humidity"]
sensor_ranges = {
    "temperature": [0, 200],
    "weight": [0, 200],
    "light": [0, 6000],
    "humidity": [0, 100]
}
errors = [f"E{i}" for i in range(10)] + [np.nan, "&^%$", "Test"]
dataset = []

for row_index in range(number_of_rows):
    sensor = random.choice(sensor_type)
    ranges = sensor_ranges[sensor]
    date = datetime.datetime.utcnow()
    if random.random() < 0.1:
        value = random.choice(errors)
    else:
        value = random.randint(*ranges)
    measurement = {"sensor": sensor, "date": date, "measurement": value}
    dataset.append(measurement)
df = pd.DataFrame(dataset)
df.to_csv('../data/drinks_invalid.csv', index=False)

