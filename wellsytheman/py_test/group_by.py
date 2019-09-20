import pandas as pd
import numpy as np
path = '/Users/wells_wang/PycharmProjects/Python/wellsytheman/py_test/data/nba.csv'
files = pd.read_csv(path,header=0)
# print(files.head())
files = files.sort_values('Salary')
# print(files)
g = files.groupby('Team').Name
# for name, group in g:
#     print(name)
# BC = g.get_group()
gg = list(g.groups.keys())

df = pd.DataFrame(g.agg(lambda x: ','.join(x)))
df.reset_index(level=0, inplace=True)
aa = df.Name.iloc[4]
a = list(aa.split(","))
print(aa)
print(a)
# print(df)
# print(gg[7])
del(files)
# print(BC)
# CC = []
# for i in gg[3:]:
#     a = list(g.get_group(i))
#     CC.append(a)
# print(CC)
