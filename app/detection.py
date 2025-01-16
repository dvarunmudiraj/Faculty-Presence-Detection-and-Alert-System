import cv2
import time
from app.notification import send_telegram_notification  # Ensure the alert system is in place

cap = None  # Webcam capture object

def monitor_faculty(stop_event):
    global cap
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access the webcam")
        return

    print("Monitoring started...")

    # Load the face detection classifier
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

    last_seen = time.time()
    alert_interval = 30

    while not stop_event.is_set():  # Run until stop_event is set
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            last_seen = time.time()  # Reset the timer if faces are detected

        # If no faces are detected, check absence duration
        if len(faces) == 0:
            absence_duration = time.time() - last_seen
            if absence_duration >= alert_interval:
                minutes = int(absence_duration // 60)
                seconds = int(absence_duration % 60)
                message = f"Faculty is absent for {minutes} minutes and {seconds} seconds."
                print(message)

                try:
                    send_telegram_notification(message)  # Send notification
                except Exception as e:
                    print(f"Error sending alert: {e}")

                # Sleep to avoid repeated alerts for the same absence duration
                time.sleep(alert_interval)

        # Draw rectangles around faces and display the frame
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Faculty Monitoring', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Monitoring stopped.")