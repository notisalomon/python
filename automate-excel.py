import pandas as pd
import numpy as np
import glob

files = glob.glob('*.csv')

df_list = []

for f in files:
    csv = pd.read_csv(f)
    df_list.append(csv)

sales = pd.concat(df_list)
sales['Date'] = pd.to_datetime(sales['Date'])

total_sales = pd.pivot_table(sales, index='item', values='qty', aggfunc=np.sum)

print(total_sales)