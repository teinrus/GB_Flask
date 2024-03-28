from flask import Flask, redirect,render_template

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template ('index.html')

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