from flask import Flask, request,render_template, Response, make_response

app = Flask(__name__) 

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

if __name__ == '__main__':
    app.run(debug=True)