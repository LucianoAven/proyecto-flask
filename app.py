import time

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    count = str(redis.get('hits'),'utf-8')
    return f'Hello World! I have been seen {count} times.\n' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
