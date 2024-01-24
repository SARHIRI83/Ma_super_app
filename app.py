from flask import Flask
app=Flask(__name__)
@app.route("/")
def Hello_world():
    return"<p>Bonjour, Bienvenue !</p>"