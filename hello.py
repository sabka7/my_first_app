from flask import Flask, render_template, request

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

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"]) # post method is necessary because it is recieving data
def sign_up():
    form_data = request.form
    print form_data["email"] #prints the email in the terminal
    return "All OK"

app.run(debug=True) # runs the application, at this point if nothing else is written, it is waiting for a web browser
# can also use localhost:5000 to run on browser
