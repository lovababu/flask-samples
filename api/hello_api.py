from flask import Flask
app = Flask(__name__)


@app.route('/')   # '/' url binding, and optional options to bind parameters.
def hello():
    return "Hello, Avol."


def greet():
    return "hi welcome."


app.add_url_rule('/', 'greet', greet)


if __name__ == '__main__':
    app.run(debug=True)    # run also takes hot, port and options.

# host=os.environ.get('IP', '0.0.0.0')
# port=int(os.environ.get('PORT', 8080))
# app.run(host=host, port=port)
