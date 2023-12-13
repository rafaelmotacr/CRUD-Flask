from flask import Blueprint
from flask.templating import render_template

bp_users = Blueprint('users', __name__, template_folder="template")

@bp_users.route('/create')

def create():
  return render_template('users_create.html')


