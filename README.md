# Flask Starter Code
Example for getting your first python Flask application running!

## Prerequisites
>- Installation of python (Preferrably latest version)
>- Installation of pip (Preferrably latest version)
>- Installation of flask (`pip install flask`) in the terminal

## Code breakdown

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "My First Flask App!"
  

app.run()
```

>- `from flask import Flask` import the Flask class so you can use it
>- `app = Flask(__name__)` instantiating the class of Flask
>- `@app.route('/')` Clarifying where in the url this will show up [In this case, '/' means the default root path]
>- `def index():` Declaring the function so the code inside can be run
>- `return "My First Flask App!"` What output you will see on that path [In this case, '/']
>- `app.run()` Run the app
