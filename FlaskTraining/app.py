from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
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


if __name__ == '__main__':
    app.run()
