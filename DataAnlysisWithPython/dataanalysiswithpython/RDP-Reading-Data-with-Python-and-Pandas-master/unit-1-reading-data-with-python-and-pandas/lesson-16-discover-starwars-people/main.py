import numpy as np
import pandas as pd
import requests

# r = requests.get("https://swapi.co/api/people/?format=json")

# print(r.status_code,"\n")

# swapi = r.json()
# print(swapi)


url = "https://swapi.dev/api/people/?format=json"
response = requests.get(url, verify=False)

if response.status_code == 200:
    data = response.json()

    starwars_people_df = pd.DataFrame(data['results'])
    print("All people:\n", starwars_people_df[['name', 'eye_color']])


    blue_eyed_people_df = starwars_people_df[starwars_people_df['eye_color'].str.contains('blue', case=False)]
    print("\nBlue-eyed people:\n", blue_eyed_people_df[['name', 'eye_color']])
else:
    print("Failed to fetch data. Status code:", response.status_code)