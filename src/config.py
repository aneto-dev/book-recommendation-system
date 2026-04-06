from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = BASE_DIR / "models"

USERS_FILE = RAW_DATA_DIR / "users.csv"
BOOKS_FILE = RAW_DATA_DIR / "books.csv"
INTERACTIONS_FILE = RAW_DATA_DIR / "interactions.csv"

GENRE_MODEL_FILE = MODELS_DIR / "genre_model.pkl"
