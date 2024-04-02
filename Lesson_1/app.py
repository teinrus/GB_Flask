from flask import Flask, request,render_template, Response, make_response , url_for , redirect,flash
from models import db, User 
from werkzeug.security import generate_password_hash
app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.secret_key = 'cbec138c4aa00e7afa391be9a9c6bfadd464b6e6773e4456'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/' , methods=['post', 'get'])
def index():
    return render_template ('index.html')

@app.route('/getcookie', methods = ['POST', 'GET'])
def getcookie():
    if request.method == 'POST':
        user = request.form['username']
        email = request.form['email']
        resp = make_response(render_template('getcookie.html',user=user))
        resp.set_cookie('userName', user)
        resp.set_cookie('email', email)

        return resp

@app.route('/del', methods = ['POST', 'GET'])
def delete_cookie():
    resp = Response ("Удалить cookie")
    resp = make_response(render_template('index.html'))
    resp.delete_cookie('userName')
    return resp

@app.route('/Clothes')
def Clothes():
    return render_template ('Products/Clothes.html')
@app.route('/Footwear')
def Footwear():
    return render_template ('Products/Footwear.html')

@app.route('/Jacket')
def Jacket():
    return render_template ('Products/Jacket.html')



@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        user = request.form['username']
        family = request.form['family']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        new_user = User(username=user, family=family, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Пользователь успешно добавлен!', 'success')
        return redirect(url_for('registration'))
    else:
        # Это GET-запрос, поэтому вы можете вернуть форму для регистрации
        return render_template('LogIn.html')
    


if __name__ == '__main__':
    app.run(debug=True)