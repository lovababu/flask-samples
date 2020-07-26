from flask import Flask
app = Flask(__name__)


@app.route('/hello/<name>')   # '/' url binding, and optional options to bind parameters.
def hello(name):
    return "Hello, {}.".format(name)


@app.route('/sum/<int:num1>/<int:num2>')  # datatypes in request params.
def sum(num1, num2):
    return "Sum is {}".format((num1 + num2))


if __name__ == '__main__':
    app.run(debug=True)    # run also takes hot, port and options.
