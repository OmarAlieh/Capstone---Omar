from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = 'JoeSmith'
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///kpis.db"
app.secret_key = "this is a secret key"

#heroku = Heroku(app)
db = SQLAlchemy(app)
