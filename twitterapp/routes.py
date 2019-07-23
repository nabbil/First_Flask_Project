from flask import render_template, redirect, url_for
from twitterapp import app
from twitterapp.forms import SignUpForm, LoginForm
from twitterapp.models import db

# Importing Database Model
from twitterapp.models import User, check_password_hash


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def createUser():
    form = SignUpForm()
    if form.validate_on_submit():
        print("The username is {}".format(form.username.data))
        user = User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    else:
        print("Not valid")
        print(form.errors)
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    user_email = form.email.data
    password = form.password.data
    user = User.query.filter(User.email == user_email).first()
    if user and check_password_hash(user.password, password):
        return redirect(url_for('hello_world'))
    print(form.email.data, form.password.data)
    return render_template("login.html", form=form)
