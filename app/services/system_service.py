import platform
import psutil
import socket
from datetime import datetime
from app.database import get_connection

def get_system_info():

    return{

    "python": platform.python_version(),

    "os": platform.system(),

    "hostname": socket.gethostname(),

    "ip": socket.gethostbyname(socket.gethostname()),

    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

    "cpu": psutil.cpu_percent(interval=1),

    "cpu_count": psutil.cpu_count(),

    "memory": psutil.virtual_memory().percent,

    "memory_total": round(
        psutil.virtual_memory().total / (1024**3), 2
    ),

    "disk": psutil.disk_usage("/").percent

    }

def save_system_log(cpu, memory, disk):

    conn = get_connection()
    cursor = conn.cursor()

    sql="""
        INSERT INTO system_logs
        (created_at, cpu, memory, disk)
        VALUES (%s,%s,%s,%s)
        """

    cursor.execute(
        sql,
        (
            datetime.now(),
            cpu,
            memory,
            disk
        )
    )
    conn.commit()
    cursor.close()
    conn.close()

def get_recent_logs(limit=10):

    conn = get_connection()
    cursor = conn.cursor()

    sql ="""
        SELECT *
        FROM system_logs
        ORDER BY created_at DESC
        LIMIT %s
        """

    cursor.execute(sql, (limit,))
    logs = cursor.fetchall()

    cursor.close()
    conn.close()

    return logs