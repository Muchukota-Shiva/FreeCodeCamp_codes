import numpy as np
import pandas as pd
import json
from pandas import json_normalize

with open('files/artists.json') as file:
    json_dict = json.load(file)

artists = json_normalize(json_dict)

biography = json_normalize(json_dict, record_path='bio', meta=['name'])

print(biography.head())

print(artists.head())