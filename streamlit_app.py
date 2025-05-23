import streamlit as st
import pandas as pd

df = pd.read_csv("IMDB_2024_Movies.csv")

st.title("IMDb 2024 Movie Dashboard")

rating_filter = st.sidebar.slider("Minimum Rating", 0.0, 10.0, 5.0)
duration_filter = st.sidebar.slider("Duration (min)", 0, 300, (90, 180))
votes_filter = st.sidebar.number_input("Minimum Votes", 0, 1000000, 1000)
genre_filter = st.sidebar.multiselect("Genres", options=df['Genre'].unique(), default=list(df['Genre'].unique()))

filtered_df = df[
    (df["Rating"] >= rating_filter) &
    (df["Votes"] >= votes_filter) &
    (df["Duration"] >= duration_filter[0]) &
    (df["Duration"] <= duration_filter[1]) &
    (df["Genre"].isin(genre_filter))
]

st.dataframe(filtered_df)

st.subheader("Top 10 Rated Movies")
top10 = df.sort_values(by=["Rating", "Votes"], ascending=False).head(10)
st.table(top10[["Movie Name", "Genre", "Rating", "Votes"]])

st.subheader("Genre Distribution")
genre_counts = df["Genre"].value_counts()
st.bar_chart(genre_counts)
