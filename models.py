from database import db


class user(db.Model):
  __tablename__ = "user"  # Cria uma tabela de usuário no banco de dados e as associa
  id = db.Column(db.Integer,primary_key=True)  # Define como chave primária do banco de dados
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  password = db.Column(db.String(100))
  cpassword = db.Column(db.String(100))

  def __init__(self, name, email, password, cpassword = "NULL"):
    self.name = name
    self.email = email
    self.password = password
    self.cpassword = cpassword

  
  def __repr__(self):
    return f'user:{self.name}'
