

import time
import datetime

LOG_FILE = "runner_logs.txt"

def log_message():
    """Appends a timestamped message to the log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"Log entry at: {timestamp}\n"
    try:
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)
        print(f"Successfully wrote to {LOG_FILE}")
    except IOError as e:
        print(f"Error writing to file {LOG_FILE}: {e}")

def main():
    """Main loop to run the logging task every 30 seconds."""
    print("Runner bot started. Logging every 30 seconds.")
    while True:
        log_message()
        time.sleep(30)

if __name__ == "__main__":
    main()

