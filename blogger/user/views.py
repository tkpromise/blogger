from flask import Blueprint, render_template, url_for, redirect, flash

from blogger.user.models import User
from blogger.app import db, bcrypt
from blogger.user.forms import SignUpForm, LoginForm

user_page = Blueprint('user_page', __name__)

@user_page.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.session.add(user)
        db.session.commit()
        flash('Thanks for signing up!', 'success')
        return redirect(url_for('user_page.login'))
    return render_template('user/signup.html', form=form)

@user_page.route('/login')
def login():
    form = LoginForm()
    return render_template('user/login.html', form=form)
