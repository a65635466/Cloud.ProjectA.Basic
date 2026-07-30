from flask import Flask

# Flask 애플리케이션 생성
app = Flask(__name__)      # Flask 애플리케이션 생성

# 메인 페이지(/) 요청 처리
@app.route("/")            # 브라우저에서 / 주소로 접속하면 아래 함수를 실행
def home():                # 메인 페이지 함수
    return "Hello Cloud,ProjectA.Basic!"     # 문자열 출력, return -> 브라우저에 응답 전송

# 프로그램 시작
if __name__== "__main__":
    app.run(debug=True)                      # 개발 서버 실행

# Step4의 핵심은 Flask가 어떻게 웹 서버를 띄우는지 경험하는 것