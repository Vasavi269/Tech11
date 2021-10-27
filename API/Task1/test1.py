from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def Home():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': some_json}), 201
    else:
        return 'Welcome to Home Page! To view the message use /hello in the URL'

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({"Hello World!"})

app.run(host='0.0.0.0', port='5003')
        