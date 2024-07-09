# Supply Chain Data Analysis

This repository contains a script for performing various analyses on supply chain data. The analyses include data cleaning, exploratory data analysis (EDA), and visualization of key metrics such as the number of products supplied by each supplier, the number of products from each location, inspection results, and products below stock levels.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Overview

The script performs the following tasks:
1. Imports necessary libraries.
2. Connects to Google Drive to access the dataset.
3. Loads and displays the supply chain data.
4. Performs data cleaning by checking for missing and duplicate values.
5. Analyzes and visualizes the number of products supplied by each supplier and the number of products from each location.
6. Identifies products that failed inspection and calculates the failure rate for each supplier.
7. Identifies products that are below stock levels.

## Installation

To install the necessary libraries, run the following commands:

```bash
pip install pandas numpy matplotlib seaborn
#connect to google drive
from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)
root_dir = "/content/gdrive/My Drive/"

# load the dataset
df = pd.read_csv(r'/content/gdrive/My Drive/supply_chain_data.csv')

#Usage
#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load and display data
df = pd.read_csv(r'/content/gdrive/My Drive/supply_chain_data.csv')
df.head()
df.info()
display(df.describe())
df.describe(include=['O'])

# clean the dataset
df.isnull().sum()
df.duplicated().sum()

#analyze and visualize the data
#Products Supplied by Each Supplier
suppliers = df[['Supplier name']].value_counts().to_frame('supply items').reset_index()
suppliers_sorted = suppliers.sort_values(by='supply items', ascending=False)

fig, ax1 = plt.subplots(figsize=(6, 3))
sns.barplot(suppliers_sorted, y='Supplier name', x='supply items', ax=ax1, palette='Blues')
ax1.set_title('Number of products supply by each supplier')
ax1.bar_label(ax1.containers[0], fontsize=8)

#Products from Each Location
locations = df[['Location']].value_counts().to_frame('items').reset_index()
locations_sorted = locations.sort_values(by='items', ascending=False)

fig, ax = plt.subplots(figsize=(6, 3))
sns.barplot(locations_sorted, y='Location', x='items', ax=ax, palette='RdPu')
ax.set_title('Number of products from each location')
ax.bar_label(ax.containers[0], fontsize=8)

#Products that Failed Inspection
fail = df.loc[df['Inspection results']=='Fail']
fail_s = fail[['Supplier name']].value_counts().to_frame('fail count').reset_index()
fail_s = pd.merge(fail_s, suppliers, on='Supplier name')
fail_s['fail rate'] = fail_s['fail count'] / fail_s['supply items']
fail_s.sort_values(by='fail rate', ascending=False)

#Products Below Stock Level
need_order = df.loc[df['Availability'] < df['Stock levels']]
need_order
#dependencies
pip install pandas numpy matplotlib seaborn
# This `README.md` file provides a comprehensive guide to setting up and using the script, including installation steps, setup instructions, and usage examples. Adjust the file paths and any specific details as needed.

