from flask import Flask
app = Flask(__name__)

from locations import get_locations_js

@app.route("/pcs_locations_js")
def _():
    return get_locations_js()

if __name__ == "__main__":
    app.run()
