import pandas as pd

from src.config import USERS_FILE, BOOKS_FILE, INTERACTIONS_FILE


def load_users() -> pd.DataFrame:
    return pd.read_csv(USERS_FILE)


def load_books() -> pd.DataFrame:
    return pd.read_csv(BOOKS_FILE)


def load_interactions() -> pd.DataFrame:
    df = pd.read_csv(INTERACTIONS_FILE)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def load_all_data():
    users = load_users()
    books = load_books()
    interactions = load_interactions()
    return users, books, interactions
