from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "My First Flask App!"
  

app.run()
