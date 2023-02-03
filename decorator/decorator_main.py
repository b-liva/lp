"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Is the User Logged In?
The final example before moving on to some fancier decorators is commonly used when working
with a web framework. In this example, we are using Flask to set up a /secret web page that should only be visible to 
users that are logged in or otherwise authenticated

While this gives an idea about how to add authentication to your web framework, you should usually not write these
types of decorators yourself. For Flask, you can use the Flask-Login extension instead, which adds more security and
functionality """
from flask import Flask

from decorator.decorators import login_required

app = Flask(__name__)


@app.route("/secret")
@login_required
def secret():
    ...
