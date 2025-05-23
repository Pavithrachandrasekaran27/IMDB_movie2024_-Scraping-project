from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv("IMDB_2024_Movies.csv")
engine = create_engine('sqlite:///imdb_2024.db')
df.to_sql('movies', engine, if_exists='replace', index=False)
