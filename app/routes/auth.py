from . import bcrypt
from flask import Blueprint, url_for, redirect, render_template, flash, jsonify, Response, request
from models.user import User, db
from forms.auth_forms import RegistrationForm, LoginForm
from flask_login import login_required, login_user, logout_user, current_user
from typing import Optional

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """A route responsible for user registration"""
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for('business.dashboard'))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            print('User found: {user}')
            flash('A user with that email already exists.', 'danger')
        hashed_password = bcrypt.generate_password_hash(
                form.password.data).decode('utf-8')
        user = User(
            full_name = form.full_name.data,
            username = form.username.data,
            phone = form.phone.data,
            password = hashed_password,
            email = form.email.data,
            is_admin = form.is_admin.data
        )
        try:
            db.session.add(user)
            db.session.commit()
            flash('Your account has been successfully created!', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred while creating your account: {str(e)}', 'danger')
    # Render the registration form for GET or invalid POST
    return render_template('register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """A route for user login"""
    print('--------login hit-------')
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for('business.dashboard'))
    form = LoginForm()

    print(f"{form.email.data}---------------")
    if form.validate_on_submit:
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            print(f'User found: {user}')
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                print('Password check passed')
                login_user(user, remember=form.remember.data)
                next_page: Optional[str] = request.args.get('next')
                print(f"Next page: {next_page}")
                if next_page and next_page.startswith('/'):
                    return redirect(next_page)
                return redirect(url_for('business.dashboard'))

                # return redirect(next_page) if next_page else redirect(url_for('user.dashboard'))
            print("Login unsuccessful. Invalid email or password.")  # Debug statement
            flash('Login Unsuccessful. Please check email and password', 'danger')
        else:
            flash('Login to access this page... Thank you')
    else:
        print("Form validation failed.")  # Debug statement
    
    next_page: Optional[str] = request.args.get('next')
            
    return render_template('login.html',
                           title='Login',
                           form=form,
                           next_page=next_page
                           )


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
    return jsonify({"message": "Logged out successfully"}), 200