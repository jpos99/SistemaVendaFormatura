from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # person_id = db.Column(db.Integer, db.ForeignKey('Persons.id'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


'''class Person(db.Model):
    __tablename__ = 'Persons'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Integer)
    last_name = db.Column(db.Integer)
    email = db.Column(db.String(120), index=True, unique=True)
    birth_date = db.Column(db.String)
    bond = db.Column(db.String)
    #user = db.relationship('Users', backref='user', lazy='dynamic')


class Formando(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer)
    process_id = db.Column(db.Integer)
    quantity_of_photos = db.Column(db.Integer)
    position_id = db.Column(db.Integer)
    situation_id = db.Column(db.Integer)


class Company(db.Model):
    id = 0
    name = ''
    phone_id = 0
    address_id = 0
    contac_name1 = ''
    contact_phone1= 0
    contac_name2 = ''
    contact_phone2 = 0
    contac_name3 = ''
    contact_phone3 = 0


class Process(db.Model):
    id = 0
    code = 0
    degree_institution =''
    course = ''
    company_id = 0


class Position(db.Model):
    pass


class Situation(db.Model):
    pass


class Adresses(db.Model):
    pass
'''
