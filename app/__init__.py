from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

# import routes goes at bottom to solve circular routes problem
from app import routes
