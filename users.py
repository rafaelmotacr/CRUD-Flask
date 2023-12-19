from flask import Blueprint, redirect
from flask.templating import render_template, request

from database import db
from models import user

bp_users = Blueprint("users", __name__, template_folder="templates")


@bp_users.route('/create', methods=['GET', 'POST'])
def create():
  if request.method == 'GET':
    return render_template('users_create.html', u=user)

  if request.method == 'POST':
    name = request.form.get('name')
    cpf = request.form.get('cpf')
    gender = request.form.get('gender')
    age = request.form.get('age')

    u = user(name, cpf, gender, age)
    db.session.add(u)
    db.session.commit()
    return redirect('/')


@bp_users.route('/read')
def recovery():
  users = user.query.all()
  return render_template('users_read.html', users=users)


@bp_users.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
  u = user.query.get(id)
  if request.method == 'GET':
    return render_template('users_update.html', u=u)

  if request.method == 'POST':

    name = request.form.get('name')
    age = request.form.get('age')
    cpf = request.form.get('cpf')
    gender = request.form.get('gender')

    u.name = name
    u.age = age
    u.cpf = cpf
    u.gender = gender

    db.session.add(u)
    db.session.commit()
    return redirect('/users/read')


@bp_users.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  u = user.query.get(id)

  if (request.method == 'GET'):
    return render_template('users_delete.html', u=u)

  if request.method == 'POST':
    db.session.delete(u)
    db.session.commit()
    return redirect('/')
