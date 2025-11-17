import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

#读取数据
df = pd.read_csv('./data/player_stats.csv')

#清洗%列函数
def clean_percentage(column):
    return (
        df[column]
        .astype(str)
        .str.replace('%', '', regex=False)
        .str.replace('\xa0', '', regex=False)
        .str.strip()
        .replace(['', ' ', 'nan', 'NaN', 'None'], np.nan)
        .astype(float)
    )

#清洗数据
df['kast'] = clean_percentage('kast%')
df['hs'] = clean_percentage('hs%')
df['adr'] = pd.to_numeric(df['adr'].astype(str).str.replace('\xa0', '').str.strip(), errors='coerce')
df['fk'] = pd.to_numeric(df['fk'].astype(str).str.replace('\xa0', '').str.strip(), errors='coerce')
df['fd'] = pd.to_numeric(df['fd'].astype(str).str.replace('\xa0', '').str.strip(), errors='coerce')

print(df[['player', 'map', 'kill', 'death', 'adr', 'kast', 'hs', 'fk', 'fd']].head())

#筛选手&地图的数据
players = ['Mazin', 'zekken', 'Cryocells', 'Victor', 'DubsteP']
maps = ['Fracture', 'Icebox', 'Haven', 'Pearl']
player_df = df[(df['player'].isin(players)) & (df['map'].isin(maps))]

#计算平均表现,player&map分组
avg_stats = (
    player_df.groupby(['player', 'map'])[['kill', 'death', 'adr', 'kast', 'hs']]
    .mean()
    .reset_index()
)

#参数
maps = ['Fracture', 'Icebox', 'Haven', 'Pearl']
metrics = ['kill', 'death', 'adr', 'kast', 'hs']
players = ['Mazin', 'zekken', 'Cryocells', 'Victor', 'DubsteP']

#风格
sns.set(style="whitegrid")
palette = sns.color_palette("Set2", len(players))

#每张地图生成一张图
for game_map in maps:
    map_df = avg_stats[avg_stats['map'] == game_map]

    #数据to长格式
    long_df = map_df.melt(id_vars=['player'], value_vars=metrics, var_name='Metric', value_name='Value')

    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=long_df,
        x='Metric',
        y='Value',
        hue='player',
        palette=palette
    )

    plt.title(f'Player Performance on {game_map}')
    plt.ylabel('Average Value')
    plt.xlabel('Metric')
    plt.legend(title='Player', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

    metrics = ['kill', 'death', 'adr', 'kast', 'hs']
    players = ['Mazin', 'zekken', 'Cryocells', 'Victor', 'DubsteP']
    maps = ['Fracture', 'Icebox', 'Haven', 'Pearl']

#热力图
for metric in metrics:
    #数据透视表
    pivot_table = avg_stats.pivot(index='player', columns='map', values=metric).reindex(players)[maps]

    plt.figure(figsize=(8, 5))
    sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=0.5, cbar_kws={'label': metric})
    plt.title(f'Player {metric.capitalize()} across Maps')
    plt.xlabel("Map")
    plt.ylabel("Player")
    plt.tight_layout()
    plt.show()