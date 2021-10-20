from flask import Flask, render_template
import jyserver.Flask as jsf

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('hellow.html')

@app.route('/contact/')
def contact():
    return render_template('https://www.linkedin.com/in/johan-jigsved-540a26201/')


if __name__ == "__main__":
    app.run(debug=True)
