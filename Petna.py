import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
matplotlib.rcParams['figure.figsize'] = (50,50)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 2000)

def missingvalues(sheet_name,spreadsheet):
    """
    Outputs missing values percentage and a heatmap for a an Excel spreadsheet sheet
    
    input:  sheet_name (use the .sheet_name option on a ExcelFile object to get the list)
            spreadsheet
    """
    df = spreadsheet.parse(sheet_name,header=[0,1])
    cols = df.columns
    ax = sns.heatmap(df[cols].isnull(), cmap=sns.color_palette('Set2',2))
    ax.set_title(f'Missing values for {sheet_name}')

    for col in df.columns:
        pct_missing = np.mean(df[col].isnull())
        print(f'{col} - {round(pct_missing*100)}% missing')