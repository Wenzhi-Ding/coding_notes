# https://stackoverflow.com/questions/53439133/python-pandas-balance-an-unbalanced-dataset-for-panel-analysis/68158944#68158944
# https://stackoverflow.com/questions/35491274/split-a-pandas-column-of-lists-into-multiple-columns/69148256#69148256

import itertools

import pandas as pd

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
start = pd.Timestamp('2017-12-09 00:00:00')
end = pd.Timestamp('2020-03-27 00:00:00')

idx = []
while start < end:
    idx.append(start)
    start += pd.Timedelta(1, 'D')

balanced_idx = pd.DataFrame(
    itertools.product(
        df[['user_no', 'currency']].drop_duplicates().values,  # Dimension 1: Combination of keys
        idx  # Dimension 2: All dates
    )
    , columns=['user_no_currency', 'date']  # Assign column names
)

# Unpack the combined keys
balanced_idx['user_no'], balanced_idx['currency'] = zip(*list(balanced_idx['user_no_currency'].values))