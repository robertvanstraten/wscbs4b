from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle


def train_model(train_path):
    train_data = pd.read_csv(train_path)
    y = train_data["Survived"]

    model = RandomForestClassifier(n_estimators=100, max_depth=5,
                                   random_state=1)
    model.fit(train_data, y)

    file_path = f"/result/model.pickle"
    with open(file_path, "wb") as f:
        pickle.dump(model, f)
    return file_path


def predict(model_path, test_path):
    test_data = pd.read_csv(test_path)

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    predictions = model.predict(test_data)
    output = pd.DataFrame({'PassengerId': test_data.PassengerId,
                           'Survived': predictions})

    file_path = f"/result/submission.csv"
    output.to_csv(file_path, index=False)
    return file_path
