import pandas as pd

path = '/Users/wells_wang/PycharmProjects/Python/wellsytheman/py_test/data/nba.csv'
files = pd.read_csv(path,header=0)
print(files.head())

g = files.groupby('Team').Name
BC = g.get_group('Boston Celtics')
gg = list(g.groups.keys())
del(files)
print(BC)
# CC = []
# for i in gg[3:]:
#     a = list(g.get_group(i))
#     CC.append(a)
# print(CC)
