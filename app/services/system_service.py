import platform
import psutil
from datetime import datetime
def get_system_info():

    return{

        "python": platform.python_version(),
        "os": platform.system(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent
    }