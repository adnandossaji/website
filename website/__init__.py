from flask import Flask

app = Flask(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'nan.dossaji@gmail.com'
app.config["MAIL_PASSWORD"] = 'X!t4k3y0m0nyx'

from routes import mail
mail.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:102137@127.0.0.1/development'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from models import db
db.init_app(app)

import website.routes
