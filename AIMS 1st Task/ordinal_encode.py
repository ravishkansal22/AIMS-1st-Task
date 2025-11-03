import pandas as pd
import numpy as np

data = {
    'Movies Rating': ['Interstellar', 'Inception', 'The Dark Knight', 'Pulp Fiction', 'The Godfather', 'Fight Club'],
    'preference': ['low', 'medium', 'high', 'high', 'medium', 'low']
}
df = pd.DataFrame(data)

mapdict = {
    'low': 1,
    'medium': 2,
    'high': 3
}

encoded_preference = []

for pref in df['preference']:
    if (pref == 'low'):
        encoded_preference.append(1)
    elif (pref == 'medium'):
        encoded_preference.append(2)
    elif (pref == 'high'):
        encoded_preference.append(3)
    else:
        encoded_preference.append(np.nan)

df['encoded_preference'] = encoded_preference

print(df)
