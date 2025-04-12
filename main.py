# Import the OpenCV library
import cv2

# Initialize video capture using the default camera (usually webcam at index 0)
cap = cv2.VideoCapture(0)

# Define the codec and create a VideoWriter object to save the output video
# 'XVID' is a common codec for .avi files
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))  # 20 FPS, 640x480 resolution

# Prompt the user
print("Press 's' to stop recording....")

# Start capturing video frame-by-frame
while cap.isOpened():
    ret, frame = cap.read()  # Read a frame from the camera
    
    if ret:
        out.write(frame)  # Write the frame to the output video file
        cv2.imshow("Recording", frame)  # Display the recording in a window
        
        # Stop recording if the user presses the 's' key
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else:
        # Exit loop if frame capture fails
        break

# Release the camera and file resources
cap.release()
out.release()
# Close all OpenCV windows
cv2.destroyAllWindows()
