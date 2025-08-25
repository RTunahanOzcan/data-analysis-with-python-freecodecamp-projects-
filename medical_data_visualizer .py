import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('medical_examination.csv')
bmi = df['weight'] / ((df['height'] / 100) ** 2)

df['overweight'] = (bmi > 25).astype(int)


df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    features = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=features,
        var_name='variable',
        value_name='value'
    )

    
    df_cat = (
        df_cat
        .groupby(['cardio', 'variable', 'value'], as_index=False)
        .size()
        .rename(columns={'size': 'total'})
    )

    
    g = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    )


    fig = g.fig


    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    df_heat = df.copy()
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    

    corr = df_heat.corr(numeric_only=True)

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 9))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",   
        center=0,
        vmax=0.3,
        vmin=-0.08,
        square=True,
        cbar_kws={"shrink": 0.5}
    )

    fig.savefig('heatmap.png')
    return fig
