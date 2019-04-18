"""
To run this app, in your terminal:
> python iris_classification_api.py

Access the Swagger UI at:
http://0.0.0.0:8080/ui
"""
import connexion
from sklearn.externals import joblib

# Create the Flask application instance.
app = connexion.FlaskApp(__name__, port=8080, specification_dir='swagger/')
application = app.app

# Load the pre-trained model.
clf = joblib.load('./model/iris_classifier.joblib')


def health():
    """Simple health check function (GET)."""
    try:
        predict(1, 1, 1, 1)
    except:
        return {"Message": "Service is unhealthy"}, 500

    return {"Message": "Service is OK"}


def predict(sepal_length, sepal_width, petal_length, petal_width):
    """Predict function. Accept the features as POST text values."""
    pred = clf.predict([[sepal_length, sepal_width,
                         petal_length, petal_width]])

    # Map the predicted value to a class.
    if pred[0] == 0:
        pred_class = "Iris-Setosa"
    elif pred[0] == 1:
        pred_class = "Iris-Versicolour"
    else:
        pred_class = "Iris-Virginica"

    # Return the prediction as JSON.
    return {"prediction": pred_class}


# Read the API definition to configure the service endpoints.
app.add_api("iris_classification_api.yaml")

# Run the application.
if __name__ == "__main__":
    app.run()
