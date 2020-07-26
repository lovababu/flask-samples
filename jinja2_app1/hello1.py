from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hello/<name>')
def hello(name):
    return render_template('template.html', name=name)  # html templates should be inside the /templates directory.


if __name__ == '__main__':
    app.run(debug=True)    # run also takes hot, port and options.
