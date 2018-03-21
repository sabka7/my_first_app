from flask import Flask, render_template

app = Flask("MyApp") #all @... after this line must be @app because that is how you defined stuff at the start

@app.route("/")
def hello():
    return "Hello World! Hola!"

@app.route("/idontexist")
def idontexist():
    return "I do exist now"

@app.route("/saba")
def saba():
    return "affogato"

app.run(debug=True) # runs the application, at this point if nothing else is written, it is waiting for a web browser
# can also use localhost:5000 to run on browser
