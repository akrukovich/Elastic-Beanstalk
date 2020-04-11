import flask


application = flask.Flask(__name__)


@application.route('/')
def hello_world():
    message = "Hello, World!!!"
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
