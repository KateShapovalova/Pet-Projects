from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kate'}
    posts = [
        {
            'author': {'username': 'Ichigo'},
            'body': 'Beautiful day in Tokyo!'
        },
        {
            'author': {'username': 'Mark'},
            'body': 'The Spiderman movie was so cool!'
        }
    ]
    title = 'Practice Home Page - Ichigo page '

    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run()
