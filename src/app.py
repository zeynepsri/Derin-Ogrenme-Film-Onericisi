import streamlit as st
from preprocess import load_and_preprocess
from vectorizer import vectorize_text
from train import train_model
from recommender import recommend

st.title("🎬 Film Öneri Sistemi")

@st.cache_data
def load_data():
    return load_and_preprocess(
        "data/tmdb_5000_movies.csv",
        "data/tmdb_5000_credits.csv"
    )

@st.cache_resource
def load_model(df):
    X = vectorize_text(df["clean_text"])
    model = train_model(X, epochs=5)
    return model, X

df = load_data()
model, X = load_model(df)

movie = st.text_input("Film adı girin:")

if movie:
    recs, matched = recommend(movie, df, model, X)
    if recs:
        st.success(f"En yakın eşleşme: {matched}")
        for r in recs:
            st.write("🎥", r)
    else:
        st.error("Film bulunamadı.")



