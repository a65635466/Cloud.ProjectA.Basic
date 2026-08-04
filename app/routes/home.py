from flask import Blueprint, render_template
import platform
from datetime import datetime

# home Blueprint 생성
home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():

    server_info = {
        "project": "Cloud.ProjectA.Basic",
        "python": platform.python_version(),
        "os": platform.system(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "flask_status": "Running"
    }

    return render_template("index.html", info=server_info)