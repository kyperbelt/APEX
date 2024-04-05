import pyautogui
import time

# Enable Macbook head pointer
def enable_head_pointer():
    # Open System Preferences
    # pyautogui.hotkey('command', 'space')
    pyautogui.keyDown('command')
    pyautogui.press('space')
    pyautogui.keyUp('command')

    time.sleep(1)  # Wait for the spotlight search to appear
    pyautogui.write('Head Pointer')
    pyautogui.press('enter')
    time.sleep(1)  # Wait for System Preferences to open

    # Click at the coordinates (1157, 533)
    pyautogui.moveTo(x=1157, y=533)
    time.sleep(1)
    pyautogui.click()

enable_head_pointer()

# Eye tracking
import cv2
import mediapipe as mp
import subprocess

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

        '''# Mouse mover
        for id, landmark in enumerate(landmarks[474:478]):
            # Draw a green circle around each landmark
            # cv2.circle(frame, (x, y), 3, (0, 255, 0))
            # Individual landmark of the left eye

            if id == 1:
                # x, y coordinates for center of landmark
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)

                # Current position
                cur_x = screen_w / frame_w * x
                cur_y = screen_h / frame_h * y

                pyautogui.moveTo(cur_x, cur_y)'''

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
        print("Left: " + str(left[0].y - left[1].y), "Right: " + str(right[0].y - right[1].y))
        if (left[0].y - left[1].y < 0.01) and (right[0].y - right[1].y < 0.01):
           print("Blink")
           pyautogui.sleep(1)
        elif (left[0].y - left[1].y < 0.009):
           pyautogui.click()
           pyautogui.sleep(1)
           print("Wink")
        elif (right[0].y - right[1].y < 0.004):
           print("New Wink")
           subprocess.run(['python3', 'newstt.py'])
           pyautogui.sleep(1)
    # print(landmark_points)
    # cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)

