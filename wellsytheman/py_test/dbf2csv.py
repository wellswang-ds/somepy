import pandas as pd

from simpledbf import Dbf5
path = '/Users/wells_wang/Desktop/WPI_Shapefile/WPI.dbf'
dbf = Dbf5(path)
df = dbf.to_dataframe()
df.to_csv('/Users/wells_wang/Desktop/WPI.csv',index = False)
