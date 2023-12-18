from database import db


class user(db.Model):
  __tablename__ = "user"  # Cria uma tabela de usuário no banco de dados e as associa
  id = db.Column(db.Integer,primary_key=True)  # Define como chave primária do banco de dados
  name = db.Column(db.String(100))
  cpf = db.Column(db.String(100))
  gender = db.Column(db.String(100))
  age = db.Column(db.Integer)
  
  
  def __init__(self, name, cpf, gender, age):
    self.name = name
    self.cpf = cpf
    self.gender = gender 
    self.age = age
  
  def __repr__(self):
    return f'user:{self.name}'
