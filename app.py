from flask import Flask
from app.routes.home import home_bp

# Flask 애플리케이션 생성
app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(home_bp)

# 서버 실행
if __name__=="__main__":
    app.run(debug=True)

