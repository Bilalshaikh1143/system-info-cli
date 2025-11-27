import platform
import socket
import psutil
import cpuinfo

print("Operating System:", platform.system())
print("OS Version:", platform.version())
print("Architecture:", platform.machine())
print("Computer Name:", socket.gethostname())

def new_func():
    ram = psutil.virtual_memory()
    return ram

ram = new_func()
print("Total RAM (GB):", round(ram.total / 1024**3, 2))
print("Used RAM (GB):", round(ram.used / 1024**3, 2))

cpu = cpuinfo.get_cpu_info()
print("CPU Name:", cpu['brand_raw'])