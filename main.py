# import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)
root_dir = "/content/gdrive/My Drive/"
df = pd.read_csv(r'/content/gdrive/My Drive/supply_chain_data.csv')
# import dataset
df = pd.read_csv(r'/content/gdrive/My Drive/supply_chain_data.csv')
df.head()
df.info()
display(df.describe())
df.describe(include=['O'])
#cleanig dataset
df.isnull().sum()
df.duplicated().sum()
# products supply by each supplier
suppliers = df[['Supplier name']].value_counts().to_frame('supply items').reset_index()
suppliers_sorted = suppliers.sort_values(by='supply items',ascending=False)

fig, ax1 = plt.subplots(figsize=(6, 3))
sns.barplot(suppliers_sorted,y='Supplier name', x='supply items',ax=ax1,palette='Blues')
ax1.set_title('Number of products supply by each supplier')
ax1.bar_label(ax1.containers[0],fontsize=8)

# products from each location
locations = df[['Location']].value_counts().to_frame('items').reset_index()
locations_sorted = locations.sort_values(by='items',ascending=False)

fig, ax = plt.subplots(figsize=(6, 3))
sns.barplot(locations_sorted,y='Location', x='items', ax=ax, palette='RdPu')
ax.set_title('Number of products from each location')
ax.bar_label(ax.containers[0],fontsize=8)
# products have failed in inspection
fail = df.loc[df['Inspection results']=='Fail']
fail_s = fail[['Supplier name']].value_counts().to_frame('fail count').reset_index()
fail_s = pd.merge(fail_s, suppliers,on='Supplier name')
fail_s['fail rate']=fail_s['fail count']/fail_s['supply items']
fail_s.sort_values(by='fail rate',ascending=False)
# products below stock levels
need_order = df.loc[df['Availability']<df['Stock levels']]
need_order
