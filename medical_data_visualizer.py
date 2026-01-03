# 1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 2: Load the data
df= pd.read_csv('medical_examination.csv')

# 3: Add the 'overweight' Column
df['overweight'] = (df['weight'] /((df['height']/100)**2)>25).astype(int)

#4: Normalize data by making '0' always good and '1' always bad. 
# If the value of 'cholesterol' or 'gluc' is 1, set it to 0. 
# If the value is greater than 1, set it to 1.
df['cholesterol'] =(df['cholesterol']>1).astype(int)
df['gluc'] = (df['gluc']>1).astype(int)

def draw_cat_plot():
    # 5: Create DataFrame for cat plot using `pd.melt`
    # This turns your wide table into a long "tidy" table
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # 6: Group and reformat the data to split it by 'cardio'. 
    # This calculates the 'total' counts for each category.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7: Draw the catplot with 'sns.catplot()'
    # We grab the '.fig' so the grader can check the image
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig

    # 8: Save the output and return the figure
    # 9: The "Do not modify" lines: fig.savefig and return fig.
    fig.savefig('catplot.png')
    return fig
    
    #10
def draw_heat_map():
    # 11 : clean the data
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= df['height'].quantile(0.025)) & 
    (df['height'] <= df['height'].quantile(0.975)) & 
    (df['weight'] >= df['weight'].quantile(0.025)) & 
    (df['weight'] <= df['weight'].quantile(0.975))]
    # 12: Perform the correlation matrix
    corr = df_heat.corr()
    # 13 : Create the triangle mask
    mask = np.triu(np.ones_like(corr, dtype=bool))


    # 14 : Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,12))
    # 15 : Draw the heat map with 'sns.heatmap'
    sns.heatmap(corr, mask=mask, 
            annot=True, 
            fmt='.1f', 
            center=0, 
            square=True, 
            linewidths=.5, 
            cbar_kws={'shrink': .5}
            )
     # 16: Save the heat map and return
    fig.savefig('heatmap.png')
    return fig

