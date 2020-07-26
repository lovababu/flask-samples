from flask import Flask, redirect, url_for, render_template_string, render_template

app = Flask(__name__)


@app.route('/admin')
def admin():
    return "Hello, admin."


@app.route('/guest/<name>')
def guest(name):
    html = "<html>" \
           "<body>" \
           " <h1>Sample App. {{ name }}</h1>" \
           "</body>" \
           "</html>"
    return render_template_string(html, name=name) # "Hello guest, {}".format(name)


@app.route('/guest/<name>/details')
def details(name):
    html = "<html>" \
           "<body>" \
           " <h1>Sample App. {{ name }}, Hyderabad.</h1>" \
           "</body>" \
           "</html>"
    return render_template_string(html, name=name) # "Hello guest, {}".format(name)


@app.route('/guest/<name>/detailsv1')
def detailsv1(name):

    return render_template('biodata.html', name=name, address='Hyderabad', hobbies='Playing')
    # "Hello guest, {}".format(name)


@app.route('/login/<name>')
def login(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', name=name))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
