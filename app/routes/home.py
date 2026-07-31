from flask import Blueprint, render_template

# home Blueprint 생성
home_bp = Blueprint("home", __name__)

# 메인 페이지
@home_bp.route("/")
def home():
    return render_template("index.html")  # render_template() -> Html 파일을 브라우저에 보내는 Flask 함수
                                          #       문자열 대신 실제 웹페이지를 보여주기 위함

