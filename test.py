from flask import Flask, render_template, request
app = Flask(__name__)
 
@app.route('/')
def student():
    return render_template('index.html')
 
@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form['Curtain_OPENTIME']
        print(result)
        return "thank you for filling out this form"
 
if __name__ == '__main__':
    app.run(debug = True)