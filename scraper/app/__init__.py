from flask import Flask
from config import Config
from flask_cors import CORS


# Create an instance of the flask class
app = Flask(__name__)

# Configure out app with a secret key
app.config.from_object(Config)

# add CORS to app
CORS(app, resources={r"/api/*": {'origins':'*'}})

from app.blueprints.api import api
app.register_blueprint(api)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001)

# import all of the routes from the routes files
from app import routes