from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mail_sent', methods=["POST"])
def mail():

    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")
    print(name)
    print(email)
    print(subject)
    print(message)
    if not name or not email or not subject or not message:
        error_statment = "Enter all the information"

        return render_template('index.html', error_statment=error_statment)
    else:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("johas1997nov@gmail.com", "")
        server.sendmail("johas1997nov@gmail.com", "johan.jigsved@yahoo.se", name + ": \n" + email +": \n" + subject + ": \n" + message)
        return render_template('index.html', error_statment="Email sent!")







if __name__ == "__main__":
    app.run(debug=True)
