import pandas as pd
import os


def clean_data():
    # Load CSV - use tab delimiter if needed
    df = pd.read_csv("data/raw/students.csv", sep="\t")

    # Drop missing values
    df.dropna(inplace=True)

    # Check if expected columns exist
    if "gender" not in df.columns:
        raise ValueError("❌ 'gender' column not found in data!")

    # Convert gender to numeric
    df["gender"] = df["gender"].map({"Male": 1, "Female": 0})

    # Save processed data
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/cleaned.csv", index=False)
    print("✅ Data cleaned and saved at data/processed/cleaned.csv")
    return df


def load_and_clean():
    # Load with tab delimiter
    df = pd.read_csv("data/raw/students.csv", sep="\t")

    # Drop nulls
    df.dropna(inplace=True)

    # Convert categorical to dummy variables
    df = pd.get_dummies(df, drop_first=True)

    # Save to processed
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/cleaned.csv", index=False)
    print("✅ Data cleaned and saved at data/processed/cleaned.csv")


if __name__ == "__main__":
    load_and_clean()
