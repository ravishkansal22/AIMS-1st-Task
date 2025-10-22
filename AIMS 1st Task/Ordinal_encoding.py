import pandas as pd 
import numpy as np

# Adding a sample data
data = {
    'Movies Rating': ['Interstellar', 'Inception', 'The Dark Knight', 'Pulp Fiction', 'The Godfather', 'Fight Club'],
    'preference': ['low', 'medium', 'high', 'high', 'medium', 'low']
}
df = pd.DataFrame(data)

preference_mapping = {
    'low': 1,
    'medium': 2,
    'high': 3
}
df['preference_encoded'] = df['preference'].map(preference_mapping)

print(df)
