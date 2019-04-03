# For feeding variables to templates.
from jinja2 import StrictUndefined

# For helpful debugging.
from flask import Flask, redirect, render_template, request, session, flash
from flask import jsonify
from flask_paginate import Pagination, get_page_args
from flask_debugtoolbar import DebugToolbarExtension

# Create Flask app.
app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required for Flask sessions and debug toolbar use
app.secret_key = "ABC"

@app.route("/")
def index():
    """Show homepage."""

    return render_template("homepage.html")


################################################################################

if __name__ == "__main__":
    # debug=True as it has to be True at when DebugToolbarExtension is invoked.
    
    app.debug = True

    connect_to_db(app)

    # Using the DebugToolbar.
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")