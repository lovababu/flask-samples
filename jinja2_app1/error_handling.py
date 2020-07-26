from flask import Flask, render_template, abort
app = Flask(__name__)


@app.route('/hello/<string:name>')
def hello(name):
    if name == 'notfound':
        abort(404)
    return "Success {}".format(name)


@app.route('/restricted')
def restricted():
    abort(401)


@app.errorhandler(404)
def not_fount(error):
    print error
    return render_template('error/404.html'), 404


@app.errorhandler(401)
def not_authroized(error):
    print error
    return render_template('error/401.html'), 401


if __name__ == '__main__':
    app.run(debug=True)    # run also takes hot, port and options.
