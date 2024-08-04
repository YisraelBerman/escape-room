from flask import render_template, url_for, flash, redirect, request, Blueprint
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, Stage1Form
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('index.html', title='Home')

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@main.route("/stage1", methods=['GET', 'POST'])
@login_required
def stage1():
    form = Stage1Form()
    if form.validate_on_submit():
        if form.answer1.data:
            current_user.stage = 2
            db.session.commit()
            flash('Correct! Proceed to Stage 2.', 'success')
            return redirect(url_for('main.stage2'))
        elif form.answer2.data:
            flash('Incorrect. Try again.', 'danger')
    return render_template('stage1.html', title='Stage 1', form=form)

@main.route("/stage2", methods=['GET', 'POST'])
@login_required
def stage2():
    return render_template('stage2.html', title='Stage 2')

@main.route("/leaderboard")
def leaderboard():
    users = User.query.order_by(User.stage.desc()).limit(3).all()
    return render_template('leaderboard.html', title='Leaderboard', users=users)

@main.route("/current_stage")
@login_required
def current_stage():
    if current_user.stage == 1:
        return redirect(url_for('main.stage1'))
    elif current_user.stage == 2:
        return redirect(url_for('main.stage2'))
    # Add more stages as needed
    else:
        flash('Invalid stage.', 'danger')
        return redirect(url_for('main.home'))
