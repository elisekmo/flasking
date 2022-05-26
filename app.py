from flask import Flask

app = Flask(__name__)
print(app)
@app.route('/')
def hello():
    return "Hello World, this is me 2.0!!"

