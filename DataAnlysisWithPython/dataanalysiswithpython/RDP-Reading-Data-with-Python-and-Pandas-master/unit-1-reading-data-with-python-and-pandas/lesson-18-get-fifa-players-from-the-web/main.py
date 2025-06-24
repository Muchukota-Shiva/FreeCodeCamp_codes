import numpy as np
import pandas as pd
import requests
import html5lib

dfs = pd.read_html('files/fifa_players.html', encoding='utf-8')

fifa_df = dfs[0]

fifa_df = fifa_df.iloc[:, 2:-1]

most_hits_player = fifa_df.sort_values('Hits', ascending=False).head(1)

print(most_hits_player)