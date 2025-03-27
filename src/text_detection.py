import cv2

video = cv2.VideoCapture("input.mp4")

if not video.isOpened():
    print("Error: Could not open video file.")
else:
    success, frame = video.read()
    count = 0

    while success:
        cv2.imwrite(f"frames/frame_{count}.jpg", frame)
        success, frame = video.read()
        count += 1

    video.release()
    print(f"Extracted {count} frames successfully.")
