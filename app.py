#imports
from flask import Flask, render_template, request
from flask_restful import Resource, Api

#Create the app
app = Flask(__name__) #create flask app
api = Api(app) #create restful

#Routes - for rendering HTML documents
@app.route("/")
def index():
    return render_template("index.html")

#Rest APIs
class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'World'}


#main
if __name__ == "__main__":
    #Add rest API and define its route
    api.add_resource(HelloWorld,'/getHelloWorld') # you can access this resource through <baseURL>:<port>/getHelloWorld
    #i kept debug at true for dev purpose. set to false when in prod.
    app.run(host="0.0.0.0", port=8001,debug=True)
