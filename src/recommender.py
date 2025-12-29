import torch
from sklearn.metrics.pairwise import cosine_similarity
import difflib

def recommend(title, df, model, X, top_n=5):
    titles = df["title"].str.lower().tolist()
    closest = difflib.get_close_matches(title.lower(), titles, n=1)

    if not closest:
        return [], None

    idx = titles.index(closest[0])

    with torch.no_grad():
        _, embeddings = model(
            torch.tensor(X.toarray(), dtype=torch.float32)
        )

    sims = cosine_similarity(
        embeddings[idx].unsqueeze(0),
        embeddings
    )[0]

    indices = sims.argsort()[::-1][1:top_n+1]
    return df.iloc[indices]["title"].tolist(), df.iloc[idx]["title"]

