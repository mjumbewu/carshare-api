from flask import Flask
import json
app = Flask(__name__)

from locations import get_pcs_locations

@app.route("/pcs_locations")
def _():
    return json.dumps(get_pcs_locations())

if __name__ == "__main__":
    app.run()
