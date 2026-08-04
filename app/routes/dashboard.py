from flask import Blueprint, render_template
from app.services.system_service import get_system_info

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
    system_info = get_system_info()

    print (system_info)

    return render_template(
        "dashboard.html",
        info=system_info
    )