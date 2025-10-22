import pandas as pd
import numpy as np

data = {
    'color': ['red', 'blue', 'green', 'blue', 'green', 'red']
}
df = pd.DataFrame(data)

categories = df['color'].unique()

for cat in categories:
    df[cat] = [1 if x == cat else 0 for x in df['color']]
print(df)
