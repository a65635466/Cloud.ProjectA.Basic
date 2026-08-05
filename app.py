from flask import Flask
from app.routes.home import home_bp
from app.routes.about import about_bp
from app.routes.dashboard import dashboard_bp
from app.routes.api import api_bp

# Flask 애플리케이션 생성
app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(api_bp)

# 서버 실행
if __name__=="__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

