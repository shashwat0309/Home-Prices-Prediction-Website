from flask import Flask, request, jsonify
  
app = Flask(__name__)
 
@app.route('/') #decorator drfines the   
def home():  
    return "hello, this is our first flask website";  

@app.route('/get_location_names') #decorator drfines the   
def get_location_names():  
    response =  jsonify([
        'locations': util.get_location_names()
    ])
    response.headers.add('Location', '*')
    return "hi"
  
if __name__ =='__main__':  
    app.run(debug = True)  