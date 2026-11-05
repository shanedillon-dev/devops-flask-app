import socket

from flask import Flask
from redis import Redis
from redis.exceptions import RedisError

app = Flask(__name__)

# "the-redis-server" is the name of the Service in redis-service.yaml.
# Kubernetes DNS resolves it to whichever Redis pod is running.
redis_client = Redis(host='the-redis-server', port=6379, socket_connect_timeout=2)


def visit_count():
    """Count this visit in Redis, shared by all 5 Flask replicas."""
    try:
        return redis_client.incr('visits')
    except RedisError:
        return 'unavailable (cannot reach Redis)'


@app.route('/')
def say_hello():
    return ('<p>Welcome, This is another string</p>'
            f'<p>Visits: {visit_count()}</p>'
            f'<p>Served by pod: {socket.gethostname()}</p>'
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
