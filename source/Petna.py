import numpy as np
import pandas as pd
import seaborn as sns

def missingvalues(sheet_name,spreadsheet):
    """
    Outputs missing values percentage and a heatmap for a an Excel spreadsheet sheet
    
    input:  sheet_name (use the .sheet_name option on a ExcelFile object to get the list)
            spreadsheet
    """
    df = spreadsheet.parse(sheet_name,header=[0,1])
    return sns.heatmap(df.isnull(),
                       cmap=sns.color_palette('Set2',2),
                       cbar=False,
                       xticklabels=[f'{col} - {round(np.mean(df[col].isnull())*100)}% missing' for col in df.columns],
                       yticklabels=False
                      ).set_title(f'Missing values for {sheet_name}');