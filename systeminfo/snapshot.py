import psutil
import json
import argparse
import time
from datetime import datetime

number = 0

parser = argparse.ArgumentParser(description='parser of arguments')
parser.add_argument("-t", help="Interval between snapshots", type=int, default=30)
parser.add_argument("-d", help="Output file type txt or json", default="txt")
args = parser.parse_args()


def get_cpu():
    return psutil.cpu_percent()


def get_mem():
    return psutil.disk_usage("/").percent


def get_vmem():
    return psutil.virtual_memory().percent


class Monitor:
    def __init__(self):
        self.cpu = get_cpu()
        self.mem = get_mem()
        self.vmem = get_vmem()


def ctime():
    return str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def output():
    if args.d == "json":
        data = {
            "snapshot": str(number),
            "timestamp": ctime(),
            "CPU load": Monitor().cpu,
            "memory": Monitor().mem,
            "virtual memory": Monitor().vmem
        }
        f = open("monitor.json", "a")
        json.dump(data, f, indent=3)
        f.write("\n")
        f.close()
        print("monitor.json is creating ...")
        return None
    else:
        n = number
        timestamp = ctime(),
        CPU_load = Monitor().cpu,
        memory = Monitor().mem,
        virtual_memory = Monitor().vmem
        f = open("monitor.txt", "a")
        f.write("snapshot %s timestamp %s CPU load %s memory %s virtual_memory %s\n" % (
            n, timestamp, CPU_load, memory, virtual_memory))
        f.close()
        print("monitor.txt is creating ...")
        return None


while True:
    number += 1
    output()
    time.sleep(args.t)

