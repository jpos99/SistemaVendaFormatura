from flask import render_template, redirect, flash, url_for, request
from app import db, app_variable
from app.forms import LoginForm, UserRegistrationForm#, PersonRegistrationForm
from flask_login import current_user, login_user, logout_user
from app.models import User#, Person
from werkzeug.urls import url_parse


@app_variable.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app_variable.route('/user_register', methods=['GET', 'POST'])
def user_register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register_user.html', title='Register', form=form)

'''@app_variable.route('/person_register', methods=['GET', 'POST'])
def person_register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = PersonRegistrationForm()
    if form.validate_on_submit():
        person = Person(
            first_name=form.first_name.data,
            last_name=form.first_name.data,
            email=form.email.data,
            CPF=form.CPF.data,
            birth_date=form.birth_date.data,
            bond=form.bond.data
        )

        db.session.add(person)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register_user.html', title='Register', form=form)
'''
@app_variable.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app_variable.route('/index')
def index():
    return render_template('index.html', title='Home')

