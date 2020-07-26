from flask import Flask, render_template_string
app = Flask(__name__)


@app.route('/')
def hello():

    html = """"
     <html>
       <h2>Hello, Welcome to Jinja2</h2>
       <ul>
        {% for car in cars %}
        <li>{{ car }}</li>
        {% endfor %}
       </ul>
     </html>
    """
    cars = ["Hyundai", "Suzuki", "Renault"]
    return render_template_string(html, cars=cars)  # string as template


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)    # run also takes hot, port and options.
