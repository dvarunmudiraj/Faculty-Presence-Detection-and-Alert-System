from flask import Flask, render_template
import threading
from app.detection import monitor_faculty  # Import the function from detection.py

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

# Global variables to track monitoring status
monitor_flag = threading.Event()
monitor_thread = None  # Thread reference for stopping the monitoring loop

@app.route('/')
def home():
    return render_template('home.html', monitoring_active=monitor_thread and monitor_thread.is_alive())

@app.route('/start-monitoring')
def start_monitoring():
    global monitor_flag, monitor_thread
    if not monitor_thread or not monitor_thread.is_alive():
        monitor_flag.clear()  # Ensure the flag is cleared before starting
        monitor_thread = threading.Thread(target=monitor_faculty, args=(monitor_flag,), daemon=True)
        monitor_thread.start()
    return render_template('home.html', monitoring_active=True)

@app.route('/stop-monitoring')
def stop_monitoring():
    global monitor_flag
    monitor_flag.set()  # Signal the monitoring thread to stop
    if monitor_thread and monitor_thread.is_alive():
        monitor_thread.join()  # Ensure thread is properly joined
    return render_template('home.html', monitoring_active=False)

if __name__ == "__main__":
    app.run(debug=True)
