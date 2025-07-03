import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
#first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. 
#If that value is > 25 then the person is overweight. 
#Use the value 0 for NOT overweight and the value 1 for overweight
df['overweight'] = df["weight"] / (df["height"]/100)**2
df.loc[df["overweight"] > 25, "overweight"] = 1
df.loc[df["overweight"] !=1, "overweight"] = 0

# 3
df['cholesterol']=df['cholesterol'].apply(lambda x: 0 if x==1 else 1)
df['gluc']=df['gluc'].apply(lambda x: 0 if x==1 else 1)

# 4
def draw_cat_plot():
    # 5
    #Create a DataFrame for the cat plot using pd.melt 
    #with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    # Group and reformat the data in df_cat to split it by cardio. 
    #Show the counts of each feature. 
    #You will have to rename one of the columns for the catplot to work correctly.
    # Group and count
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    

    # 7
    fig = sns.catplot(
        x='variable',
        y='total',
        data=df_cat,
        kind='bar',
        hue='value',
        col='cardio'
    ).fig


    # 8
    #fig = sns.catplot(x = 'variable', y = 'total', data = df_cat, kind = 'bar', hue = 'value', col = 'cardio').fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12, 10))


    # 15
    sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    fmt='.1f',
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={'shrink': 0.5},
    ax=ax
    )


    # 16
    fig.savefig('heatmap.png')
    return fig
