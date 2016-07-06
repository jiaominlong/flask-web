from app import app
from flask import render_template, request, redirect
from app.models import User, db

@app.route('/')
def index():
    return render_template('index.html', title='首页')



@app.route('/reg', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        #form = request.form
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('register.html', title='register')


@app.errorhandler(404)
def not_found(error):
    return '<h2>页面找不到了！</h2>'