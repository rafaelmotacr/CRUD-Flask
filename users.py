from flask import Blueprint
from flask.templating import render_template, request

from database import db
from models import user

bp_users = Blueprint("users", __name__, template_folder="templates")


@bp_users.route('/create', methods=['GET', 'POST'])
def create():
  if request.method == 'GET':
    return render_template('users_create.html')

  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    cpassword = request.form.get('cpassword')

    u = user(name, email, password)
    db.session.add(u)
    db.session.commit()
    return 'Data registered successfully.'


@bp_users.route('/recovery')
def recovery():
  users = user.query.all()
  return render_template('users_recovery.html', users=users)
