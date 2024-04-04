'''
pip install opencv-contrib-python==4.6.0.66

pip install mediapipe==0.9.3.0

pip install pyautogui==0.9.53
'''

import cv2
import mediapipe as mp
import pyautogui

# Capture video feed
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    # Retrieve one frame from camera feed
    _, frame = cam.read()
    # Invert frame vertically
    frame = cv2.flip(frame, 1)
    # Get screen height and width
    frame_h, frame_w, _ = frame.shape
    # Convert frame from BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Process RGB frame to detect face
    output = face_mesh.process(rgb_frame)
    # Get landmark points of all faces detected
    landmark_points = output.multi_face_landmarks
    if landmark_points:
        # Get landmark points of single face
        landmarks = landmark_points[0].landmark
        # Mouse mover
        for id, landmark in enumerate(landmarks[474:478]):
            # x, y coordinates for center of landmark
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            # Draw a green circle around each landmark
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            # print(x, y)
            # Individual landmark of the left eye
            if id == 1:
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x, screen_y)
        # Click logic
        left = [landmarks[145], landmarks[159]]
        right = [landmarks[374], landmarks[386]]
        for i in range(2):
            left_x = int(left[i].x * frame_w)
            left_y = int(left[i].y * frame_h)
            right_x = int(right[i].x * frame_w)
            right_y = int(right[i].y * frame_h)
            cv2.circle(frame, (left_x, left_y), 3, (0, 255, 0))
            cv2.circle(frame, (right_x, right_y), 3, (0, 0, 255))
        # print((left[0].y - left[1].y), (right[0].y - right[1].y))
        if (left[0].y - left[1].y < 0.009) and (right[0].y - right[1].y < 0.009):
           print("Blink")
           pyautogui.sleep(1)
        elif (left[0].y - left[1].y < 0.009):
           pyautogui.click()
           pyautogui.sleep(1)
           print("Wink")
        elif (right[0].y - right[1].y < 0.009):
           print("New Wink")
           pyautogui.sleep(1)

    # print(landmark_points)
    # cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)
