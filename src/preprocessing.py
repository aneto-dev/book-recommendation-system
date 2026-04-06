import pandas as pd


def merge_datasets(
    users: pd.DataFrame, books: pd.DataFrame, interactions: pd.DataFrame
) -> pd.DataFrame:
    df = interactions.merge(books, on="book_id", how="left")
    df = df.merge(users, on="user_id", how="left")

    df = df.sort_values(["user_id", "timestamp"]).reset_index(drop=True)
    return df
