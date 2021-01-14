from flask import Flask
from gevent.pywsgi import WSGIServer


app = Flask(__name__)


@app.route('/api/v1/hello-world-1')
def hello_world():
    return 'Hello World - 1'

if __name__ == 'main':
    app.run(debug=True)

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()