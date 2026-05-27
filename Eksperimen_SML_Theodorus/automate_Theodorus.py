import pandas as pd

def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)

    df = df.drop(columns=["Cabin"])

    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    df = pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True)

    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data(
        "titanic.csv",
        "dataset_preprocessing.csv"
    )

    print("Preprocessing selesai")