import pandas as pd

path = '/Users/wells_wang/Desktop/nba.csv'
files = pd.read_csv(path,header=0)
print(files.head())

g = files.groupby('Team')
BC = g.get_group('Boston Celtics').Name
print(BC)
