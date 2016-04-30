from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()




class User(db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))

  resume_id = db.Column(db.Integer, db.ForeignKey("resume.id"))
  resume = db.relationship('Resume',
        backref=db.backref('users', lazy='dynamic'))
  
  def __init__(self, firstname, lastname, email, password):
    _fullname()
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)

  def fullname(self):
    fullname = self.firstname + " " + self.lastname
    return fullname
    
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)
  
  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)


class Resume(db.Model):
  __tablename__ = 'resume'
  id = db.Column(db.Integer, primary_key = True)
  phone = db.Column(db.Integer)
  email = db.Column(db.String(100))
  street_address = db.Column(db.String(100))
  city = db.Column(db.String(100))
  state = db.Column(db.String(100))
  zipcode = db.Column(db.Integer)
  website = db.Column(db.String(100))
  github = db.Column(db.String(100))

  schools = db.relationship('School', backref='resume')
  experiences = db.relationship('Experience', backref='resume')

  def __init__(self, uid, phone=None, email=None, street_address=None, city=None, state=None, zipcode=None, website=None, github=None):
    self.uid = uid
    self.phone = phone
    self.email = email
    self.street_address = street_address
    self.city = city
    self.state = state
    self.zipcode = zipcode
    self.website = website
    self.github = github

  def get_address(self):
    address = self.street_address + " " + self.city + ", " + self.state + " " + str(self.zipcode)
    return address


class School(db.Model):
  __tablename__ = 'school'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100))
  url = db.Column(db.String(100))
  degree = db.Column(db.String(100))
  field_study = db.Column(db.String(100))
  city = db.Column(db.String(100))
  state = db.Column(db.String(100))
  start_date = db.Column(db.String(100))
  end_date = db.Column(db.String(100))
  concentration = db.Column(db.String(100))
  gpa = db.Column(db.Float)
  maxgpa = db.Column(db.Float)
  resume_id = db.Column(db.Integer, db.ForeignKey('resume.id'))

  descriptions = db.relationship('Description', backref='school')
  courses = db.relationship('Course', backref='school')
  technologies = db.relationship('Technology', backref='school')

class Experience(db.Model):
  __tablename__ = 'experience'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100))
  url = db.Column(db.String(100))
  title = db.Column(db.String(100))
  city = db.Column(db.String(100))
  state = db.Column(db.String(100))
  start_date = db.Column(db.String(100))
  end_date = db.Column(db.String(100))
  resume_id = db.Column(db.Integer, db.ForeignKey('resume.id'))

  descriptions = db.relationship('Description', backref='experience')
  technologies = db.relationship('Technology', backref='experience')

class Description(db.Model):
  __tablename__ = 'description'
  id = db.Column(db.Integer, primary_key = True)
  description = db.Column(db.String(100))
  school_id = db.Column(db.Integer, db.ForeignKey('school.id'))
  experience_id = db.Column(db.Integer, db.ForeignKey('experience.id'))

class Course(db.Model):
  __tablename__ = 'course'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100))
  school_id = db.Column(db.Integer, db.ForeignKey('school.id'))

class Technology(db.Model):
  __tablename__ = 'technology'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100))
  school_id = db.Column(db.Integer, db.ForeignKey('school.id'))
  experience_id = db.Column(db.Integer, db.ForeignKey('experience.id'))