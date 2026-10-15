from flask import Flask

app = Flask(__name__)


@app.route('/')
def say_hello():
    return ('<p>Welcome, This is another string</p>'
            '<p><a href="/about">About</a></p>'
            '<p><a href="/contact">Contact</a></p>')


@app.route('/about')
def about():
    return ('<p>This application is running on the Flask web framework.</p>'
            '<p><a href="https://www.python.org/">Python website</a></p>'
            '<p><a href="https://flask.palletsprojects.com/">Visit the Flask website</a></p>'
            '<p><a href="/">Back to home</a></p>')


@app.route('/contact')
def contact():
    return ('<p>Contact me at: '
            '<a href="mailto:C24417854@mytudublin.ie">C24417854@mytudublin.ie</a></p>'
            '<p><a href="/">Back to home</a></p>')
