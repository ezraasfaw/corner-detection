import cv2

# region Read image from default webcam using OpenCV convert to grayscale and then apply a colormap before displaying.
video_capture = cv2.VideoCapture(2, cv2.CAP_DSHOW)
while True:
    return_code, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dst = cv2.cornerHarris(gray, 10, 5, 0.01)
    frame[dst > 0.1 * dst.max()] = [0, 255, 0]
    cv2.imshow(‘Output’, frame)
    if cv2.waitKey(1) & 0xFF == ord(‘q’):
        break
# endregion

# region Release the camera resources.
video_capture.release()
cv2.destroyAllWindows()
# endregion
