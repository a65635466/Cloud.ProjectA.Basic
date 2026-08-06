# ☁️ Cloud.ProjectA.Basic

Docker, Flask, MariaDB를 활용하여 구축한 **클라우드 시스템 모니터링 프로젝트**입니다.

실시간으로 시스템(CPU, Memory, Disk) 정보를 조회하고, REST API를 통해 데이터를 제공하며, MariaDB에 시스템 로그를 저장하고 조회할 수 있도록 구현했습니다.

---

# 📌 프로젝트 목표

- Flask를 이용한 웹 서비스 개발
- REST API 설계 및 구현
- MariaDB 데이터베이스 연동
- Docker 및 Docker Compose 기반 개발 환경 구축
- Ubuntu(WSL2) 환경에서 프로젝트 실행
- GitHub를 활용한 프로젝트 관리

---

# 🏗 시스템 구조

```
Browser
    │
    ▼
 Flask Dashboard
    │
 REST API
    │
Flask Application
    │
    ▼
 MariaDB
    │
Docker Compose
    │
Ubuntu (WSL2)
```

---

# 🛠 기술 스택

## Backend

- Python 3
- Flask

## Database

- MariaDB
- PyMySQL

## DevOps

- Docker
- Docker Compose
- Ubuntu (WSL2)

## Version Control

- Git
- GitHub (SSH)

---

# 📂 프로젝트 구조

```
Cloud.ProjectA.Basic
│
├── app
│   ├── routes
│   │   ├── api.py
│   │   ├── dashboard.py
│   │   ├── home.py
│   │   └── about.py
│   │
│   ├── services
│   │   └── system_service.py
│   │
│   ├── templates
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── home.html
│   │   └── about.html
│   │
│   ├── static
│   │
│   └── database.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── app.py
└── README.md
```

---

# ✨ 주요 기능

## 1. 시스템 정보 조회

실시간으로 다음 정보를 조회합니다.

- Python Version
- Operating System
- Hostname
- IP Address
- CPU 사용률
- CPU Core 수
- Memory 사용률
- Total RAM
- Disk 사용률

---

## 2. REST API

### 시스템 정보

```
GET /api/system
```

JSON 형태로 시스템 정보를 제공합니다.

예시

```json
{
    "cpu": 12.5,
    "memory": 42.3,
    "disk": 28.7
}
```

---

### 시스템 로그 조회

```
GET /api/logs
```

MariaDB에 저장된 최근 시스템 로그를 반환합니다.

---

## 3. 실시간 Dashboard

Dashboard는 JavaScript Fetch API를 이용하여

- CPU
- Memory
- Disk

정보를 주기적으로 갱신합니다.

---

## 4. 시스템 로그 저장

시스템 정보를 조회할 때마다

MariaDB의

```
system_logs
```

테이블에

- 시간
- CPU
- Memory
- Disk

정보를 저장합니다.

---

# 🐳 Docker 실행

이미지 생성

```bash
docker compose build
```

컨테이너 실행

```bash
docker compose up -d
```

컨테이너 종료

```bash
docker compose down
```

---

# 💾 데이터베이스

테이블

```
system_logs
```

컬럼

| Column | Type |
|---------|------|
| id | INT |
| created_at | DATETIME |
| cpu | FLOAT |
| memory | FLOAT |
| disk | FLOAT |

---

# 프로젝트를 통해 배운 내용

이번 프로젝트를 진행하면서 다음 내용을 학습했습니다.

- Flask Blueprint 구조
- REST API 설계
- Jinja2 Template 사용
- JavaScript Fetch API
- MariaDB 연동
- PyMySQL 사용법
- Docker 이미지 생성
- Docker Compose 구성
- Ubuntu(WSL2) 환경 구축
- GitHub SSH 인증
- Docker 기반 개발 환경 구성
- 위에 기술들을 AI와 함께 진행함으로서 학습을 이어갔습니다. 

---

# 개발 환경

| 항목 | 내용 |
|------|------|
| OS | Windows 11 + Ubuntu (WSL2) |
| Language | Python 3 |
| Framework | Flask |
| Database | MariaDB |
| Container | Docker, Docker Compose |
| IDE | Visual Studio Code |
| Version Control | Git / GitHub |

---

# 프로젝트 화면
<img width="1911" height="682" alt="화면 캡처 2026-08-06 132607" src="https://github.com/user-attachments/assets/21edc461-8e3c-4a62-8f0f-5af80d086073" />
<img width="1912" height="905" alt="화면 캡처 2026-08-06 132542" src="https://github.com/user-attachments/assets/b10c873c-10bf-4c12-8cf2-3eec9f5422a5" />
<img width="1912" height="1006" alt="화면 캡처 2026-08-06 132356" src="https://github.com/user-attachments/assets/5ad16083-c5c5-4727-94ee-43521e4f5072" />
<img width="1912" height="1012" alt="도커 첫 실행" src="https://github.com/user-attachments/assets/c6716864-5bb5-4695-9ea7-c2323191dedb" />

---

# 향후 계획

- 브라우저 인터페이스 수정
- 구현했던 프로그램 복습, 수정

# 📄 라이선스

본 프로젝트는 학습 및 포트폴리오 목적으로 제작되었습니다.
