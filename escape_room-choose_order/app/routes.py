from flask import render_template, url_for, flash, redirect, request, Blueprint
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, Stage1Form, Stage2Form, Stage3Form, Stage4Form, Stage5Form
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('index.html', title='Home', login_form=login_form, register_form=register_form)

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
        return redirect(url_for('main.home'))
    login_form = LoginForm()
    return render_template('register.html', title='Register', form=form, login_form=login_form)

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
            return redirect(next_page) if next_page else redirect(url_for('main.ready'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    register_form = RegistrationForm()
    return render_template('login.html', title='Login', form=form, register_form=register_form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route("/ready")
@login_required
def ready():
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('ready.html', title='Ready', login_form=login_form, register_form=register_form)

@main.route("/account")
@login_required
def account():
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('account.html', title='Account', login_form=login_form, register_form=register_form)

@main.route("/stage1", methods=['GET', 'POST'])
@login_required
def stage1():
    form = Stage1Form()
    if form.validate_on_submit():
        if form.answer1.data:
            current_user.stage = max(current_user.stage, 1)
            current_user.points += 50  # Add points
            current_user.completed_stage1 = True  # Mark stage 1 as completed
            db.session.commit()
            flash('Correct! You earned 50 points.', 'success')
            return redirect(url_for('main.home'))
        elif form.answer2.data:
            flash('Incorrect. Try again.', 'danger')
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('stage1.html', title='Stage 1', form=form, login_form=login_form, register_form=register_form)

@main.route("/stage2", methods=['GET', 'POST'])
@login_required
def stage2():
    form = Stage2Form()
    if form.validate_on_submit():
        if form.answer1.data:
            current_user.stage = max(current_user.stage, 2)
            current_user.points += 50  # Add points
            current_user.completed_stage2 = True  # Mark stage 2 as completed
            db.session.commit()
            flash('Correct! You earned 50 points.', 'success')
            return redirect(url_for('main.home'))
        elif form.answer2.data:
            flash('Incorrect. Try again.', 'danger')
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('stage2.html', title='Stage 2', form=form, login_form=login_form, register_form=register_form)

@main.route("/stage3", methods=['GET', 'POST'])
@login_required
def stage3():
    form = Stage3Form()
    if form.validate_on_submit():
        if form.answer1.data:
            current_user.stage = max(current_user.stage, 3)
            current_user.points += 50  # Add points
            current_user.completed_stage3 = True  # Mark stage 3 as completed
            db.session.commit()
            flash('Correct! You earned 50 points.', 'success')
            return redirect(url_for('main.home'))
        elif form.answer2.data:
            flash('Incorrect. Try again.', 'danger')
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('stage3.html', title='Stage 3', form=form, login_form=login_form, register_form=register_form)

@main.route("/stage4", methods=['GET', 'POST'])
@login_required
def stage4():
    form = Stage4Form()
    if form.validate_on_submit():
        if form.answer1.data:
            current_user.stage = max(current_user.stage, 4)
            current_user.points += 50  # Add points
            current_user.completed_stage4 = True  # Mark stage 4 as completed
            db.session.commit()
            flash('Correct! You earned 50 points.', 'success')
            return redirect(url_for('main.home'))
        elif form.answer2.data:
            flash('Incorrect. Try again.', 'danger')
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('stage4.html', title='Stage 4', form=form, login_form=login_form, register_form=register_form)

@main.route("/stage5", methods=['GET', 'POST'])
@login_required
def stage5():
    form = Stage5Form()
    if form.validate_on_submit():
        if form.answer1.data:
            current_user.stage = max(current_user.stage, 5)
            current_user.points += 50  # Add points
            current_user.completed_stage5 = True  # Mark stage 5 as completed
            db.session.commit()
            flash('Correct! You earned 50 points.', 'success')
            return redirect(url_for('main.home'))
        elif form.answer2.data:
            flash('Incorrect. Try again.', 'danger')
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('stage5.html', title='Stage 5', form=form, login_form=login_form, register_form=register_form)

@main.route("/current_stage")
@login_required
def current_stage():
    if current_user.stage == 1:
        return redirect(url_for('main.stage1'))
    elif current_user.stage == 2:
        return redirect(url_for('main.stage2'))
    elif current_user.stage == 3:
        return redirect(url_for('main.stage3'))
    elif current_user.stage == 4:
        return redirect(url_for('main.stage4'))
    elif current_user.stage == 5:
        return redirect(url_for('main.stage5'))
    else:
        flash('Invalid stage.', 'danger')
        return redirect(url_for('main.home'))

@main.route("/leaderboard")
def leaderboard():
    users = User.query.order_by(User.points.desc(), User.stage.desc()).limit(3).all()
    all_users = User.query.order_by(User.username).all()  # Retrieve all users, ordered by username
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('leaderboard.html', title='Leaderboard', users=users, all_users=all_users, login_form=login_form, register_form=register_form)
