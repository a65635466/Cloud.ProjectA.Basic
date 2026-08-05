import pymysql

# MariaDB 연결 함수
def get_connection():
    return pymysql.connect(
        host="db",
        user="root",
        password="2@dlwndud2@",
        database="cloud_project",
        port=3306,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )