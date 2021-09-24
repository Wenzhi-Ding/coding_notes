# https://stackoverflow.com/questions/53439133/python-pandas-balance-an-unbalanced-dataset-for-panel-analysis/68158944#68158944
# https://stackoverflow.com/questions/35491274/split-a-pandas-column-of-lists-into-multiple-columns/69148256#69148256

import itertools

import pandas as pd

df = pd.DataFrame()

# Method 1: Monthly level and above
balanced_idx = pd.DataFrame(
    itertools.product(
        set(df['ctry_iso']),  # Dimension 1: All country codes
        range(1970, 2021),   # Dimension 2: All years
        range(1, 13)  # Dimension 3: All months
    )
    , columns=['ctry_iso', 'year', 'month']  # Assign column names
)


## Method 2: More general

# Generate consecutive time indicators
df_lst = []

for ent, cur, s, e in df.groupby(['user_no', 'currency'])['date'].agg(['min', 'max']).reset_index().values:
    ents = [ent]
    curs = [cur]
    times = [s]

    while times[-1] < e:
        times.append(times[-1] + pd.Timedelta(1, 'D'))
        ents.append(ent)
        curs.append(cur)
        
    df_lst.append(pd.DataFrame({'user_no': ents, 'currency': curs, 'date': times}))

dfs = pd.concat(df_lst)
dfs.shape