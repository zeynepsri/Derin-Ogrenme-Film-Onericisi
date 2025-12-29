from preprocess import load_and_preprocess
from vectorizer import vectorize_text
from train import train_model
from recommender import recommend

def main():
    print("Veriler yükleniyor...")
    df = load_and_preprocess(
        "data/tmdb_5000_movies.csv",
        "data/tmdb_5000_credits.csv"
    )

    X = vectorize_text(df["clean_text"])
    model = train_model(X, epochs=10)

    movie = input("\nFilm adı girin: ")
    recs, matched = recommend(movie, df, model, X)

    if not recs:
        print("Film bulunamadı.")
        return

    print(f"\nEn yakın eşleşme: {matched}")
    print("Önerilen filmler:")
    for r in recs:
        print("-", r)

if __name__ == "__main__":
    main()
