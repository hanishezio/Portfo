from flask import Flask,render_template,request,redirect
from pip._internal import index
import csv

app = Flask(__name__)

@app.route('/index')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def writetocsv(data):
    with open("database.csv",mode="a",newline='') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csvwriter=csv.writer(database,delimiter=",",quotechar="|",quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email,subject,message])





@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =="POST":
        data=request.form.to_dict()
        writetocsv(data)
        return redirect("/thanku.html")
    else:
        return 'something went wrong.try again!'




# @app.route('/about.html')
# def my_about():
#     return render_template('about.html')
#
# @app.route('/works.html')
# def my_works():
#     return render_template('works.html')
#
# @app.route('/contact.html')
# def my_contact():
#     return render_template('contact.html')
#
# @app.route('/components.html')
# def my_components():
#     return render_template('components.html')


