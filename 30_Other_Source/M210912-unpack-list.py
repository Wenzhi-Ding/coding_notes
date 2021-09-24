# https://stackoverflow.com/questions/35491274/split-a-pandas-column-of-lists-into-multiple-columns/


from operator import itemgetter

import pandas as pd

# 定义数据
df = pd.DataFrame({"teams": [["SF", "NYG"] for _ in range(1000)]})

# 方法一：827微秒
df2 = df['teams'].transform({'item1': itemgetter(0), 'item2': itemgetter(1)})

# 方法二：570微秒
df['team1'], df['team2'] = zip(*list(df['teams'].values))

# 方法三：335微秒
df2 = pd.DataFrame(df["teams"].to_list(), columns=['team1', 'team2'])