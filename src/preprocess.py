import pandas as pd
import json
import re

def parse_names(text):
    try:
        data = json.loads(text)
        return " ".join([d["name"] for d in data])
    except:
        return ""

def get_director(text):
    try:
        data = json.loads(text)
        for d in data:
            if d["job"] == "Director":
                return d["name"]
    except:
        pass
    return ""

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

def load_and_preprocess(movies_path, credits_path):
    movies = pd.read_csv(movies_path)
    credits = pd.read_csv(credits_path)

    df = movies.merge(credits, left_on="id", right_on="movie_id")

    # title_x = movies.csv'den gelen gerçek film adı
    df = df.rename(columns={"title_x": "title"})

    df["genres"] = df["genres"].apply(parse_names)
    df["keywords"] = df["keywords"].apply(parse_names)
    df["cast"] = df["cast"].apply(parse_names)
    df["director"] = df["crew"].apply(get_director)

    df["combined"] = (
        df["overview"].fillna("") + " " +
        df["genres"] + " " +
        df["keywords"] + " " +
        df["cast"] + " " +
        df["director"]
    )

    df["clean_text"] = df["combined"].apply(clean_text)

    return df[["title", "clean_text"]]






