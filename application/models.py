from .database import db

class User(db.Model):
  __tablename__ = "users"
  u_id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(), nullable=False)
  email = db.Column(db.String(), nullable=False, unique=True)
  password = db.Column(db.String(), nullable=False)
  type = db.Column(db.String(), default = "general", nullable=False)
  
class Section(db.Model):
  __tablename__ = "section"
  s_id = db.Column(db.Integer(), primary_key=True)
  s_name = db.Column(db.String(), nullable=False, unique=True)
  s_date = db.Column(db.String(), nullable=False)
  description = db.Column(db.String())
  
class Books(db.Model):
  __tablename__ = "books"
  b_id = db.Column(db.Integer(), primary_key=True)
  b_title = db.Column(db.String(), nullable=False, unique=True)
  b_author = db.Column(db.String(), nullable=False)
  description = db.Column(db.String())
  link = db.Column(db.String(), nullable=False)
  b_section = db.Column(db.String(), nullable=False)


class Issues(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  book_id = db.Column(db.Integer(), db.ForeignKey('books.b_id'), nullable=False)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.u_id'), nullable=False)
  lib_status = db.Column(db.String(), default='pending', nullable=False)
  user_status = db.Column(db.String(), default='requested' ,nullable=False)
  book = db.relationship("Books", backref="issue") #relationship to link books related to each issue using books table
  user = db.relationship("User", backref = "issues") #relationship to link user related to each issue using books table
  issued_on = db.Column(db.String, nullable=False)  # Define the created_at column