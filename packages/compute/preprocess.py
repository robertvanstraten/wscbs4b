import pandas as pd


def one_hot(data_path):
    if train in data_path:
        #data_path = f"{dataset_path}/train.csv"
        file_path = f"/result/train.csv"
    else:
        #data_path = f"{dataset_path}/test.csv"
        file_path = f"/result/test.csv"

    df = pd.read_csv(data_path)
    features = ["Pclass", "Sex", 'Embarked']
    df_out = pd.get_dummies(df, columns=features, drop_first=True)
    
    df_out.to_csv(file_path, index=False)

    return file_path


def drop_columns(data_path):
    cols = ['Survived', 'Name', 'Ticket', 'Cabin']
    df = pd.read_csv(data_path)

    to_drop = set(df.columns) & set(cols)
    df_out = df.drop(columns=list(to_drop))

    file = data_path.split('/')[-1]
    file_path = f"/result/{file}"
    df_out.to_csv(file_path, index=False)
    return file_path


def impute_median(data_path):
    cols = ['Age', 'Fare']
    df = pd.read_csv(data_path)

    for col in cols:
        df[col] = df[col].fillna(df[col].median())

    file = data_path.split('/')[-1]
    file_path = f"/result/{file}"
    df.to_csv(file_path, index=False)
    return file_path


def standardize(data_path):
    cols = ['Age', 'Fare', 'SibSp']
    df = pd.read_csv(data_path)

    for col in cols:
        df[col] = (df[col] - df[col].mean()) / df[col].std()

    file = data_path.split('/')[-1]
    file_path = f"/result/{file}"
    df.to_csv(file_path, index=False)
    return file_path
