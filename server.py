from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect ('/users')

@app.route('/users')
# displays all users
def users():
    # reference the User class and the method get_all_users
    all_users=User.get_all_users()
    return render_template("read(all).html", users = all_users)

@app.route('/user/new')
# form to create a new user
def new():
    return render_template("create.html")

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True, port=5001)