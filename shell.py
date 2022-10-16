from flask import Flask, redirect, url_for, request, jsonify
#import generate
import main
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)



@app.route('/success/<topic>')
def success(topic):
   return jsonify({"Message":"Hello there"})
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST': 
      user = request.form['nm']
      print("Get")
      return redirect(url_for('success',topic = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',topic = user))

if __name__ == '__main__':
   app.run(debug = True)