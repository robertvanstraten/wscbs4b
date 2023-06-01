from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle


def train_model(train_path):
    train_path = f"{train_path}/dataset.csv"
    train_data = pd.read_csv(train_path)
    y = train_data["Survived"]
    train_data = train_data.drop(columns="Survived")

    model = RandomForestClassifier(n_estimators=100, max_depth=5,
                                   random_state=1)
    model.fit(train_data, y)

    file_path = "/result/model.pickle"
    with open(file_path, "wb") as f:
        pickle.dump(model, f)
    return file_path


def predict(model_path, test_path):
    test_path = f"{test_path}/dataset.csv"
    test_data = pd.read_csv(test_path)

    model_path = f"{model_path}/model.pickle"

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    predictions = model.predict(test_data)
    output = pd.DataFrame({'PassengerId': test_data.PassengerId,
                           'Survived': predictions})

    file_path = "/result/submission.csv"
    output.to_csv(file_path, index=False)

    return file_path

def combine(submission, test_path):
    test_path = f"{test_path}/dataset.csv"
    test_data = pd.read_csv(test_path)
    submission = f"{submission}/submission.csv"
    prediction = pd.read_csv(submission)
    
    test_full = pd.merge(test_data, prediction, on='PassengerId')
    file_path = "/result/test_complete.csv"
    test_full.to_csv(file_path, index=False)

    return file_path