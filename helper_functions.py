"""
Helper functions for use with data science and machine learning projects

"""

__date__ = "2023-05-09"
__author__ = "SamKemp"


# %% --------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% --------------------------------------------------------------------------
# Data Summary
# -----------------------------------------------------------------------------

def data_summary(df):
        print(f"Dataset has {df.shape[1]-1} features and {df.shape[0]} samples")
        summary = pd.DataFrame(index=df.columns)
        desc = pd.DataFrame(df.describe(include='all').transpose())
        summary["Count"] = desc['count'].values
        summary["Unique"] = df.nunique().values
        summary["Missing"] = df.isnull().sum().values
        summary["Duplicated"] = df.duplicated().sum()
        summary['Std'] = desc['std'].values
        summary["Mode"] = df.mode().values[0]
        summary["Median"] = df.median()
        summary['Mean'] = desc['mean'].values
        summary['Min'] = desc['min'].values
        summary['Max'] = desc['max'].values
        summary["First Value"] = df.loc[0].values
        summary["Last Value"] = df.loc[df.shape[0]-1].values
        summary["Types"] = df.dtypes
        return summary


# %% --------------------------------------------------------------------------
# Show Outliers
# -----------------------------------------------------------------------------
def show_outliers(df, threshold):
        
        plt.figure(figsize=(20, 10))
        sns.set_theme(style="whitegrid", font_scale=0.9)
        
        features = df.columns.to_list()
        num_cols = len(features)

        for i, feature in enumerate(features):
                ax = plt.subplot(num_cols//3+1, 3, i+1)
                sns.boxplot(x=feature, data=df, ax=ax, palette='gnuplot2', whis=threshold)

        plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9, hspace=.8, wspace=0.2)
       
        plt.show()

# %% --------------------------------------------------------------------------
# Remove Outliers
# -----------------------------------------------------------------------------
def remove_outliers(df, threshold):

        features = df.columns.to_list()

        for feature in features:
                q1, q3 = np.percentile(df[feature], [25, 75])
                iqr = q3-q1
                lower_bound = q1 - (threshold * iqr)
                upper_bound = q3 + (threshold * iqr)

                df = df.loc[df[feature].between(lower_bound, upper_bound)]

        return df

# %% --------------------------------------------------------------------------
# Correlation Heatmap
# -----------------------------------------------------------------------------

def corr_heatmap(df, corr_type):

        corr = df.corr(method=corr_type)

        mask = np.triu(np.ones_like(corr, dtype=bool))

        plt.figure(figsize=(12, 8))
        
        sns.set_theme(style="white", font_scale=0.8)
        sns.heatmap(corr, cmap="YlOrBr", linewidths=2, mask=mask, vmin=-1, vmax=1, annot=True, fmt=".2f")

        plt.show()
# %%
