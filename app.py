from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/submit',methods=['POST', 'GET'])
def submit():
    total = 0
    if request.method == 'POST':
        a = eval(request.form['a'])
        b = eval(request.form['b'])
        c = eval(request.form['c'])
        delta = b**2 - 4*a*c
        root1 = 0
        root2 = 0
        if delta >= 0:
        # Real roots
            root1 = round((-b + math.sqrt(delta)) / (2*a),2)
            root2 = round((-b - math.sqrt(delta)) / (2*a),2)
        else:
            real_part = -b / (2*a)
            imaginary_part = round(math.sqrt(abs(delta))/ (2*a),2)
            root1 = complex(real_part, imaginary_part)
            root2 = complex(real_part, -imaginary_part)
            
    return render_template('result.html', result=root1, result2 = root2)


if __name__ =="__main__":
    app.run()