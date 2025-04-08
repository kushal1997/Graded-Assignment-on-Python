
import psutil

def monitor_cpu_usage(threshold):
    print("Monitoring CPU usage... \n")
    while True:
        cpu_usage = psutil.cpu_percent(interval=0.5)

        if cpu_usage > threshold :
            print(f'Alert! CPU usage exceeds threshold: {cpu_usage}%')

monitor_cpu_usage(8)