from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')
"""
@app.route('/mail_sent', methods=["POST"])
def mail():

    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")
    if not name or email or subject or message:
        error_statment = "Enter all the information"

    return render_template('mail.html')
"""



if __name__ == "__main__":
    app.run(debug=True)
