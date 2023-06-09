import pandas as pd


def one_hot(data_path):
    data_path = f"{data_path}/dataset.csv"
    file_path = "/result/dataset.csv"

    df = pd.read_csv(data_path)
    features = ["Pclass", "Sex", 'Embarked']
    df_out = pd.get_dummies(df, columns=features, drop_first=True)
    
    df_out.to_csv(file_path, index=False)

    return file_path


def drop_columns(data_path):
    data_path = f"{data_path}/dataset.csv"
    file_path = "/result/dataset.csv"

    cols = ['Name', 'Ticket', 'Cabin']
    df = pd.read_csv(data_path)

    to_drop = set(df.columns) & set(cols)
    df_out = df.drop(columns=list(to_drop))
    df_out.to_csv(file_path, index=False)
    return file_path


def impute_median(data_path):
    data_path = f"{data_path}/dataset.csv"
    file_path = "/result/dataset.csv"

    cols = ['Age', 'Fare']
    df = pd.read_csv(data_path)

    for col in cols:
        df[col] = df[col].fillna(df[col].median())

    df.to_csv(file_path, index=False)
    return file_path


def standardize(data_path):
    data_path = f"{data_path}/dataset.csv"
    file_path = "/result/dataset.csv"
        
    cols = ['Age', 'Fare', 'SibSp']
    df = pd.read_csv(data_path)

    for col in cols:
        df[col] = (df[col] - df[col].mean()) / df[col].std()

    df.to_csv(file_path, index=False)
    return file_path
