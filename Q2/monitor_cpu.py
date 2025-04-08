
import psutil

def monitor_cpu_usage(threshold):
    print("Monitoring CPU usage... \n")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=0.5)

            if cpu_usage > threshold :
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
    except Exception as e:
        print(f"Error occured : {e}")

monitor_cpu_usage(8)