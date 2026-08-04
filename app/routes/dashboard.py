from flask import Blueprint, render_template

import platform
import psutil

from datetime import datetime

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():

    system_info = {

        "python": platform.python_version(),

        "os": platform.system(),

        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "cpu": psutil.cpu_percent(interval=1),

        "memory": psutil.virtual_memory().percent

    }

    return render_template(
        "dashboard.html",
        info=system_info
    )