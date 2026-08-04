import platform
import psutil
import socket
from datetime import datetime
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