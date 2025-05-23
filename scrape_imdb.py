from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
url = "https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31"
driver.get(url)
time.sleep(5)

movie_data = []
movies = driver.find_elements(By.CLASS_NAME, "lister-item")
for movie in movies:
    try:
        name = movie.find_element(By.TAG_NAME, "h3").text.split("\n")[0]
        genre = movie.find_element(By.CLASS_NAME, "genre").text.strip()
        rating = movie.find_element(By.CLASS_NAME, "ratings-imdb-rating").get_attribute("data-value")
        votes = movie.find_element(By.CSS_SELECTOR, "span[name='nv']").text.replace(",", "")
        duration = movie.find_element(By.CLASS_NAME, "runtime").text.replace(" min", "")
        movie_data.append([name, genre, float(rating), int(votes), int(duration)])
    except Exception:
        continue

driver.quit()

df = pd.DataFrame(movie_data, columns=["Movie Name", "Genre", "Rating", "Votes", "Duration"])

for genre in df["Genre"].unique():
    genre_df = df[df["Genre"] == genre]
    genre_df.to_csv(f"{genre}_movies.csv", index=False)

df.to_csv("IMDB_2024_Movies.csv", index=False)
