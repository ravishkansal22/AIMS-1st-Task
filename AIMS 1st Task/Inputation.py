import pandas as pd
import numpy as np

data = {
    'age': [22, np.nan, 28, 28, np.nan, 31],
    'salary': [55000, 65000, np.nan, 53000, 49000, np.nan],
    'city': ['New Delhi', 'Mumbai', np.nan, 'Indore', 'Vadodara', np.nan]
}

df = pd.DataFrame(data)

for mean_imputation in ['age', 'salary']:
    mean_value = df[mean_imputation].mean()
    df[mean_imputation].fillna(mean_value, inplace=True)

df['city'].fillna('Unknown', inplace=True)
print(df)
