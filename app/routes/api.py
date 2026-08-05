from flask import Blueprint, jsonify
from app.services.system_service import get_system_info, save_system_log

api_bp = Blueprint("api",__name__)

@api_bp.route("/api/system")
def system_api():

    info = get_system_info()

    save_system_log(
        info["cpu"],
        info["memory"],
        info["disk"]
    )

    return jsonify(info)