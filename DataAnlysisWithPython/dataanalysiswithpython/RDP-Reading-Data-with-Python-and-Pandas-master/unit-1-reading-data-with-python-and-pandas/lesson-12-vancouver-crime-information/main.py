import numpy as np
import pandas as pd
import sqlite3

# create a new connection to a db in memory
conn = sqlite3.connect(':memory:')

# create a cursor
c = conn.cursor()

# restore the given van_crime_2003.sql dump
c.executescript(open('files/van_crime_2003.sql', 'r').read())

# your code goes here

van_crimes_df = pd.read_sql('SELECT * FROM van_crimes WHERE hour > 14', conn)

late_crimes = van_crimes_df.loc[van_crimes_df['HOUR'] > 18]

print("late crimes - \n",late_crimes)

dangerous_month_crimes = van_crimes_df.loc[:, 'MONTH'].value_counts().head(1)

print("dangerous months - \n",dangerous_month_crimes)