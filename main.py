from flask import Flask
from flask_migrate import Migrate
from flask.templating import render_template

from database import db
from users import bp_users

app = Flask(__name__)

conection = 'sqlite:///mydatabase.sqlite'  # stream de conexão, definida como sqlite
app.config[
    'SECRET_KEY'] = 'my-key'  # palavra de acesso para seguran̨ca do código
app.config[
    'SQLALCHEMY_DATABASE_URI'] = conection  # URL do banco de dados, usando como chav SQL-Alchemy
app.config[
    'SQLALCHEMY_TRACKMODIFICATIONS'] = False  # Bloqueio do track de inform̨acões do sistema

db.init_app(app)
with app.app_context():
  db.create_all()

app.register_blueprint(bp_users, url_prefix='/users')

migrate = Migrate(app, db)


@app.route('/')
def index():
  return render_template('index.html')


app.run(host='0.0.0.0', port=81)
