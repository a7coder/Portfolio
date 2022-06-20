from flask import Flask, render_template, request, redirect
import csv
import os
# def write_head():


def write_to_csv(data):
    file_exsist = os.path.isfile('database.csv')

    with open('database.csv', mode='a',newline='') as database:
        if not file_exsist:
            csv_writer = csv.writer(database)

            csv_writer.writerow(['email', 'subject', 'message'])
        email = data['email']
        msg = data['message']
        sub = data['subject']
        csv_writer = csv.writer(database)
        csv_writer.writerow([email, sub, msg])


app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<page_name>")
def about(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)

            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return "Data has not been saved"
    else:
        return "Error"


# @app.route("/works")
# def works():
#     return "hi "
