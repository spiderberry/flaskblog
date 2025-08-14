from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'spiderberry'}
    posts = [
        {
            'author': {'username': 'antapple'},
            'body': 'Rainy day in Atlanta! :('
        },

        {
            'author': {'username': 'beeorange'},
            'body': 'Fantastic Four was mid.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)