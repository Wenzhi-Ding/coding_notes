# https://stackoverflow.com/questions/53439133/python-pandas-balance-an-unbalanced-dataset-for-panel-analysis/68158944#68158944

import itertools

import pandas as pd

balanced_idx = pd.DataFrame(
    itertools.product(
        set(dfm['ctry_iso']),  # Dimension 1: All country codes
        range(1970, 2021),   # Dimension 2: All years
        range(1, 13)  # Dimension 3: All months
    )
    , columns=['ctry_iso', 'year', 'month']  # Assign column names
)