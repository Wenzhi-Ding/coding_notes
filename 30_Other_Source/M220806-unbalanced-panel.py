# Suppose we have a table idx: id, min_year_month, max_year_month
# We want to generate an unbalanced panel such that: 
# id, year_month (between min and max)

# This way is not efficient but easy to understand and implement
import pandas as pd

idx = pd.read_csv('xxx.csv')

idx['idx'] = 1

dt = pd.DataFrame({
    'idx': 1,
    'ym': [100 * y + m for y in range(1949, 2022) for m in range(1, 13)]})
dt['idx'] = 1

idxm = pd.merge(idx, dt, on='idx')
idxm = idxm.loc[
    (idxm['ym'] >= idxm['min_year_month'])
    & (idxm['ym'] <= idxm['max_year_month'])]


### Use pd.period_range is better
t = tmp.groupby(['currency'])['1min_tick'].agg(['min', 'max']).reset_index()
tmp_lst = []
for i in t.values:
    ts = pd.period_range(i[1], i[2], freq='1min')
    ts = pd.DataFrame(ts, columns=['1min_tick'])
    ts['currency'] = i[0]
    tmp_lst.append(ts)

ts = pd.concat(tmp_lst)
ts.shape
ts.sample(3)
    