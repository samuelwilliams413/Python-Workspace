from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : "SMW"}
    posts = [
        {
            'author' : {'username' : "Alice"},
            'body' : 'Post A'
        },
        {
            'author' : {'username' : "Bob"},
            'body' : 'Post B'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)