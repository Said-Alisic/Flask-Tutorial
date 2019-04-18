# Import Flask module from flask package - creating Flask web server
from flask import Flask, render_template

# Creating instance of Flask class and naming it app - "__name__" refers to the current file
app = Flask(__name__)


@app.route("/")     # Represents default page
def home():         # Function activated after going to default page
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


# Python assigns the name "__main__" to script when executed
# if-statement prevents other scripts (python files) from running
if __name__ == "__main__":
    app.run(debug=True)     # Runs app and debug=True allows Python errors to appear on the web page

