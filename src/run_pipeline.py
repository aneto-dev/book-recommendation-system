from src.data_loader import load_all_data
from src.preprocessing import merge_datasets
from src.feature_engineering import build_genre_training_data


def main():
    users, books, interactions = load_all_data()
    merged = merge_datasets(users, books, interactions)
    df = build_genre_training_data(merged)

    print(df.head())


if __name__ == "__main__":
    main()
