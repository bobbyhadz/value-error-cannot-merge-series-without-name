# ValueError: Cannot merge a Series without a name

import pandas as pd

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

series = pd.Series([5, 6])

df2 = df.merge(
    series.rename('C'),
    left_index=True,
    right_index=True
)
print(df2)