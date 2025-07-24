import pandas as pd
import os


def clean_data():
    df = pd.read_csv("data/raw/students.csv")
    print(f"✅ Raw columns: {list(df.columns)}")

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Convert gender to numeric
    df["gender"] = df["gender"].map({"Male": 1, "Female": 0})

    # Ensure processed directory exists
    os.makedirs("data/processed", exist_ok=True)

    # Save cleaned data
    df.to_csv("data/processed/cleaned.csv", index=False)
    print("✅ Cleaned data saved to data/processed/cleaned.csv")
    
    return df  # ✅ Important for test to access the DataFrame


def load_and_clean():
    df = pd.read_csv("data/raw/students.csv")
    df = df.dropna()

    # One-hot encode categorical columns
    df = pd.get_dummies(df, drop_first=True)

    # Save cleaned data
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/cleaned.csv", index=False)
    print("✅ Data cleaned and saved at data/processed/cleaned.csv")


# Only run when this script is executed directly
if __name__ == "__main__":
    clean_data()
