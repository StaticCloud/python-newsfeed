from flask import Blueprint, render_template

# this is similar to router in Javascript
bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('homepage.html')

@bp.route('/login')
def login():
    return render_template('login.html')

# for routes with parameters, we surround the parameter with opening and closing tags
@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')