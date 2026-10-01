import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def train_model():

    # Load dataset
    data = pd.read_csv("career_dataset.csv")

    # Input features
    X = data[
        [
            "Python",
            "Mathematics",
            "Data_Analysis",
            "Communication",
            "Web_Development"
        ]
    ]

    # Target
    y = data["Career"]

    # Create ML model
    model = DecisionTreeClassifier(random_state=42)

    # Train model
    model.fit(X, y)

    return model


# Test the model
if __name__ == "__main__":

    model = train_model()

    sample_student = pd.DataFrame(
        [[9, 9, 9, 6, 3]],
        columns=[
            "Python",
            "Mathematics",
            "Data_Analysis",
            "Communication",
            "Web_Development"
        ]
    )

    prediction = model.predict(sample_student)

    print("Machine Learning model trained successfully!")
    print("Predicted Career:", prediction[0])