from flask import Blueprint, jsonify
from app.services.system_service import (
    get_system_info,
    save_system_log,
    get_recent_logs
    )

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

@api_bp.route("/api/logs")
def logs_api():

    return jsonify(get_recent_logs())