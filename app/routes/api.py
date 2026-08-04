from flask import Blueprint, jsonify
from app.services.system_service import get_system_info

api_bp = Blueprint("api",__name__)

@api_bp.route("/api/system")
def system_api():

    return jsonify(get_system_info())