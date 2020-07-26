from flask import Flask, render_template_string
app = Flask(__name__)


@app.route('/hello/<name>')
def hello(name):
    html = """"
     <html>
       <h2>Hello, {{ name }}</h2>
     </html>
    """
    return render_template_string(html, name=name)  # string as template


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)    # run also takes hot, port and options.
