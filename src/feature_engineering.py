import pandas as pd


def build_genre_training_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Build training dataset where:
    - Features = user history
    - Target = next liked book genre
    """

    rows = []

    for user_id, group in data.groupby("user_id"):
        group = group.sort_values("timestamp").reset_index(drop=True)

        for i in range(1, len(group)):
            history = group.iloc[:i]
            current = group.iloc[i]

            # Only consider strong positive signals
            if current["rating"] < 4:
                continue

            fav_genre = (
                history["genre"].mode().iloc[0]
                if not history["genre"].mode().empty
                else None
            )

            fav_author = (
                history["author"].mode().iloc[0]
                if not history["author"].mode().empty
                else None
            )

            rows.append(
                {
                    "age": current["age"],
                    "country": current["country"],
                    "books_read_count": len(history),
                    "avg_rating_so_far": history["rating"].mean(),
                    "fav_genre_so_far": fav_genre,
                    "fav_author_so_far": fav_author,
                    "target_genre": current["genre"],
                }
            )

    return pd.DataFrame(rows)
