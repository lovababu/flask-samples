from flask import Flask, request
app = Flask(__name__)


@app.route('/hello', methods=['POST', 'GET'])   # '/' url binding, and optional options to bind parameters.
def hello():
    if request.method == 'POST':
        return "Post"
    else:
        return "Get"


if __name__ == '__main__':
    app.run(debug=True)    # run also takes hot, port and options.
