"""
To run this app, in your terminal:
> python connexion_demo.py
"""

import connexion

# Create the Flask application instance.
app = connexion.FlaskApp(__name__, port=8080, specification_dir='swagger/')
application = app.app


def health():
    """Simple health check function (GET)."""
    if multiply(2, 1) == {"product": 2}:
        return {"Message": "Service is OK"}
    else:
        return {"Message": "Service is crazy and can't do multiplication"}, 500


def multiply(multiplicand, multiplier):
    """Multiplication function (POST)."""
    product = multiplier * multiplicand
    return {"product": product}


# Read the API definition to configure the service endpoints.
app.add_api("demo_api.yaml")

# Run the application.
if __name__ == "__main__":
    app.run()
