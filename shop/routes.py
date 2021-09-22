from .forms import RegistrationForm
from flask import render_template, session, request, url_for, flash, redirect
from shop import app, db, bcrypt
from .models import User


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register(): 
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)   ## generate hash pasword from the registration form dataq
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title="Registration page")


