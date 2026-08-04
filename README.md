# Cloud.ProjectA.Basic

Cloud.ProjectA.Basic는 **클라우드 및 서버 기술을 학습하기 위한 개인 프로젝트**입니다.

이 프로젝트를 통해 Flask 기반 웹 애플리케이션을 시작으로 Docker, MariaDB, Linux, Nginx, AWS 등을 단계적으로 적용하여 최종적으로 클라우드 관리 대시보드를 구현하는 것을 목표로 합니다.

---

# 프로젝트 목표

- Flask 웹 애플리케이션 개발
- Git & GitHub를 활용한 버전 관리
- Docker 컨테이너 환경 구축
- MariaDB 데이터베이스 연동
- Linux(Ubuntu) 서버 운영
- Nginx Reverse Proxy 구성
- AWS EC2 배포
- 실시간 서버 모니터링 Dashboard 구현

---

# 개발 환경

| 항목 | 내용 |
|------|------|
| Language | Python 3.14 |
| Framework | Flask |
| IDE | Visual Studio Code |
| Version Control | Git / GitHub |
| OS | Windows 10 (Development) |

---

# 프로젝트 구조

```text
Cloud.ProjectA.Basic
│
├── app/
│   ├── routes/
│   ├── models/
│   ├── services/
│   └── __init__.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── about.html
│
├── static/
│   └── css/
│       └── style.css
│
├── config/
├── docs/
├── tests/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 현재 구현 기능

- Flask 프로젝트 생성
- GitHub 연동
- Blueprint(Route) 구조 적용
- Template Inheritance(base.html) 적용
- Home 페이지
- About 페이지
- CSS 적용
- 기본 Dashboard UI 구성

---

# 개발 예정 기능

- Navigation Bar
- Dashboard 기능 확장
- 시스템 정보 표시
- Docker 상태 확인
- MariaDB 연동
- REST API
- 사용자 로그인
- 서버 로그 관리
- AWS EC2 배포
- Nginx Reverse Proxy 적용

---

# 학습 목적

이 프로젝트는 다음 기술을 직접 구현하며 학습하는 것을 목표로 합니다.

- Python
- Flask
- HTML / CSS
- Git / GitHub
- Linux
- Docker
- MariaDB
- Nginx
- AWS
- REST API

---

# 진행 현황

| 단계 | 상태 |
|------|------|
| 개발 환경 구축 | ✅ |
| Flask 기본 구조 | ✅ |
| Blueprint 적용 | ✅ |
| Template 상속 | ✅ |
| Dashboard UI | 진행 중 |
| Docker | 예정 |
| MariaDB | 예정 |
| Linux | 예정 |
| Nginx | 예정 |
| AWS | 예정 |

---

# 최종 목표

웹 애플리케이션을 Docker 환경에서 실행하고, MariaDB 및 AWS와 연동하여 서버 상태를 실시간으로 확인할 수 있는 **클라우드 관리 대시보드**를 구현하는 것입니다.
