# Import Flask module from flask package - creating Flask web server
from flask import Flask

# creating instance of Flask class and naming it app - "__name__" refers to the current file
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"

    
if __name__ == "__main__":
    app.run(debug=True)

