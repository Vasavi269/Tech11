from flask import Flask, Request
from Flask-RESTful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get():
        return 'Hello World!'

@app.route('/')
def Home():
    return 'Welcome to Home Page! To view the message use /hello in the URL'        

api.add_resource(Hello,'/hello')

if __name__== '__main__':
    app.run(host='0.0.0.0', port='5002')
