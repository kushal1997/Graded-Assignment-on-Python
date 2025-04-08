
import psutil # import psutil library to access system details

# function to monitor CPU usage indefinitely until stopped
def monitor_cpu_usage(threshold):
    print("Monitoring CPU usage... \n")
    try:
        while True:
            # get current usage percentage every 0.5 sec
            cpu_usage = psutil.cpu_percent(interval=0.5)

            # check if CPU usage is greater than given threshold
            if cpu_usage > threshold :
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

    # if user stops using (Ctrl + C) rather showing errors with a simple clean exit            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

    # for any unexpected errors it will display the message
    except Exception as e:
        print(f"Error occured : {e}")

# call the function with threshold value
monitor_cpu_usage(80)