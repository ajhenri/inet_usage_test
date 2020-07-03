import io
import os
import time
import psutil

current_dir = os.environ.get('INET_USAGE_PATH', os.getcwd())

def format_bytes(bytes_count):
    """
    Convert byte count formatted to largest unit.

    Params
    ------
    bytes_count : int
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_count < 1000:
            return f"{bytes_count} {unit}"
        bytes_count /= 1000
    return f"{bytes_count} TB"

def update_bytes(bytes_count):
    """
    Update usage.txt file with latest network I/O count, formatted
    to the largest unit byte.

    Params
    ------
    bytes_count : int
    """
    try:
        with open(f"{current_dir}/usage.txt", "w+") as f:
            f.seek(io.SEEK_SET)
            f.write(f"{format_bytes(bytes_count)}")
            f.truncate()
    except Exception as e:
        print(str(e))

def internet_usage():
    """
    Use psutil to determine latest bytes I/O count, starting from `initial_netio`.
    """
    initial_netio = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    while True:
        netio = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        bytes_count = netio - initial_netio
        update_bytes(bytes_count)
        time.sleep(1)

internet_usage()