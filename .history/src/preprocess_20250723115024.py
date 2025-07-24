import pandas as pd
import os

def clean_data():
    raw_path = "data/raw/students.csv"

    # Try reading it as tab-separated
    df = pd.read_csv(raw_path, sep="\t")

    # Show what columns it read
    print("✅ Raw columns:", df.columns.tolist())

    # Drop missing values
    df.dropna(inplace=True)

    # Map gender if present
    if "gender" in df.columns:
        df["gender"] = df["gender"].map({"Male": 1, "Female": 0})
    else:
        raise KeyError("❌ 'gender' column not found in dataset!")

    # Save cleaned file
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/cleaned.csv", index=False)
    print("✅ Cleaned data saved to data/processed/cleaned.csv")

if __name__ == "__main__":
    clean_data()
