import pyautogui
import time
import speech_recognition as sr
import webbrowser
from gtts import gTTS
import sys
import random
import requests
import os

# Speech to text implementation
def new_type():
    for i in range(2):
        print('clicked')
        pyautogui.press('command')
        pyautogui.press('command')
    time.sleep(1)
def text_to_number(text=''):
    if 'one' in text or 'won' in text or '1' in text:
        scale = 1
    elif 'two' in text or 'too' in text or 'to' in text or '2' in text:
        scale = 2
    elif 'three' in text or '3' in text:
        scale = 3
    elif 'four' in text or 'for' in text or '4' in text:
        scale = 4
    elif 'five' in text or '5' in text:
        scale = 5
    elif 'six' in text or 'sex' in text or '6' in text:
        scale = 6
    elif 'seven' in text or '7' in text:
        scale = 7
    else:
        scale = 1
    return scale
def open_gpt():
    url = 'https://chat.openai.com'
    # Open YouTube in the default web browser
    webbrowser.open(url)

def scroll_down(text):
    # Function to scroll down
    scale = text_to_number(text)
    pyautogui.scroll(20 * scale)

def scroll_up(text):
    # Function to scroll down
    scale = text_to_number(text)
    pyautogui.scroll(20 * scale)

def turn_up_volume():
    # Function to turn up the volume (For Mac, it simulates pressing the F12 key)
    pyautogui.press('f12')

def turn_down_volume():
    pyautogui.press('f11')

def zoom_in(scale=''):
    scale = scale.strip()
    if scale == 'one':
        zoom = 1
    elif scale == 'two':
        zoom = 2
    elif scale == 'three':
        zoom = 3
    elif scale == 'four':
        zoom = 4
    elif scale == 'five':
        zoom = 5
    elif scale == 'six':
        zoom = 6
    else:
        zoom = 1

    for _ in range(zoom):
        pyautogui.keyDown('command')
        pyautogui.press('+')
        pyautogui.keyUp('command')

def zoom_out(scale=''):
    scale = scale.strip()
    if scale == 'one':
        zoom = 1
    elif scale == 'two':
        zoom = 2
    elif scale == 'three':
        zoom = 3
    elif scale == 'four':
        zoom = 4
    elif scale == 'five':
        zoom = 5
    elif scale == 'six':
        zoom = 6
    else:
        zoom = 1

    for _ in range(zoom):
        pyautogui.keyDown('command')
        pyautogui.press('-')
        pyautogui.keyUp('command')


def open_youtube():
    # URL of YouTube
    youtube_url = "https://www.youtube.com"
    # Open YouTube in the default web browser
    webbrowser.open(youtube_url)

def search_youtube(query):
    # URL of YouTube
    youtube_url = "https://www.youtube.com"
    search_url = f"{youtube_url}/results?search_query={query}"
    # Open YouTube in the default web browser with search query
    webbrowser.open(search_url)

def open_netflix():
    # URL of Netflix
    netflix_url = "https://www.netflix.com"
    # Open Netflix in the default web browser
    webbrowser.open(netflix_url)

def spell_out(text):
    # Dictionary mapping letters to words that sound like that letter
    sound_dict = {
        'a': ['a', 'hey', 'may'],
        'b': ['b', 'be', 'bee', 'by'],
        'c': ['c', 'see', 'sea', 'key', 'knee'],
        'd': ['d', 'dee', 'die', 'do', 'did'],
        'e': ['e', 'eat', 'ear', 'east'],
        'f': ['f', 'eff', 'fee'],
        'g': ['g', 'gee', 'key'],
        'h': ['h', 'hay', 'he', 'hi'],
        'i': ['i', 'eye', 'aye', 'I'],
        'j': ['j', 'jay', 'g'],
        'k': ['k', 'kay', 'knee', 'key'],
        'l': ['l', 'ell', 'el'],
        'm': ['m', 'em', 'am', 'aim'],
        'n': ['n', 'en', 'end', 'in'],
        'o': ['o', 'oh', 'owe'],
        'p': ['p', 'pee', 'pea', 'pie'],
        'q': ['q', 'cue', 'queue'],
        'r': ['r', 'are', 'our'],
        's': ['s', 'ess', 'sea', 'see', 'yes'],
        't': ['t', 'tea', 'tee', 'tie'],
        'u': ['u', 'you', 'ewe'],
        'v': ['v', 'vee', 'vie'],
        'w': ['w', 'double you', 'we'],
        'x': ['x', 'ex', 'axe', 'box'],
        'y': ['y', 'why', 'eye', 'wye'],
        'z': ['z', 'zee', 'zed']
    }

    spell_out_text = ""
    # Split the input text into individual words
    words = text.split()
    print(words)
    for word in words:
        # Check if the word exists in the sound_dict values, if yes, append its corresponding key (letter)
        for letter, sound_words in sound_dict.items():
            if word in sound_words:
                spell_out_text += letter
                break
        else:
            # If the word is not found in the dictionary, append it as is
            spell_out_text += word

    pyautogui.typewrite(spell_out_text)

def type_text(text):
    pyautogui.typewrite(text)

def backspace(text):
    print("text:", text)
    loops = text_to_number(text)
    print(loops)
    for _ in range(loops):
        print('here')
        pyautogui.press('backspace')
        pyautogui.press('delete')

def space(text):
    loops = text_to_number()
    print(loops)
    for _ in range(loops):
        pyautogui.press('space')


def recognize_speech_from_microphone():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default system microphone as the audio source
    microphone = sr.Microphone()

    # Adjust for ambient noise before listening
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

        # Say assisting phrase
        phrases = [
            "How can I help you today?",
            "I'm here to assist you.",
            "What do you need assistance with?",
            "How may I be of service?",
            "How can I assist you today?",
            "What can I do for you?",
        ]
        # Select a random phrase from the list
        text = random.choice(phrases)

        # Convert text to speech
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save("listening.mp3")

        # Play the audio file
        os.system("afplay listening.mp3")

    while True:
        with microphone as source:
            audio_data = recognizer.listen(source)

        try:
            # Recognize the speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("Recognized speech:", text)

            text = text.lower()
            if 'luminous' in text or 'exit' in text or 'back' in text or 'bye' in text:
                return

            elif 'stingers up' in text:
                sys.exit()

            elif 'space' in text:
                space(text[len('space')+1:])

            elif 'scroll up' in text:
                scroll_up(text[len('scroll up')+1:])
                return

            elif 'scroll down' in text:
                scroll_down(text[len('scroll up')+1:])
                return

            elif 'delete' in text:
                print(text[len('delete')+1:])
                backspace(text[len('delete')+1:])
                return

            elif 'code' in text:
                print("Want to implement GPT4 soon")
                '''if text[len('code')+1:]:
                    gpt(text[len('code')+1:])'''
                return

            elif 'open ai' in text:
                open_gpt()
                return

            elif 'zoom in' in text:
                if 'one' in text or 'won' in text:
                    scale = 'one'
                elif 'two' in text or 'too' in text or 'to' in text:
                    scale = 'two'
                elif 'three' in text:
                    scale = 'three'
                elif 'four'in text or 'for' in text:
                    scale = 'four'
                elif 'five' in text:
                    scale = 'five'
                elif 'six' in text or 'sex' in text:
                    scale = 'six'
                else:
                    scale = ''

                zoom_in(scale)
                return

            elif 'zoom out' in text:
                if 'one' in text or 'won' in text:
                    scale = 'one'
                elif 'two' in text or 'too' in text or 'to' in text:
                    scale = 'two'
                elif 'three' in text:
                    scale = 'three'
                elif 'four' in text or 'for' in text:
                    scale = 'four'
                elif 'five' in text:
                    scale = 'five'
                elif 'six' in text or 'sex' in text:
                    scale = 'six'
                else:
                    scale = ''

                zoom_out(scale)
                return

            elif 'open youtube' in text:
                open_youtube()
                return

            elif 'search youtube' in text:
                if text[len('search youtube')+1:]:
                    # Extract the query from the recognized speech
                    query = text[len('search youtube')+1:]
                    search_youtube(query)
                else:
                    open_youtube()
                return

            elif 'open netflix' == text:
                open_netflix()
                return

            elif 'type' in text:
                if text[len('type') + 1:]:
                    type_text(text[len('type') + 1:])
                return

            elif 'spell' == text[:len('spell')]:
                # Need to implement
                spell_out(text[len('spell')+1:])
                return

            elif 'command' == text:
                url = "http://localhost:8080/voice"

                response = requests.post(url=url, data=text[len('command')+1:])

                if response.status_code == 200:
                    data = response.json()
                    print(data)
                    return data['command']
                else:
                    print(f'Request failed for {url} with status code {response.status_code}')
                    return "NA_COMMAND"

            else:
                print("No speech detected")
                return

        except sr.WaitTimeoutError:
            print("Timeout: No speech detected")
            return
        except sr.UnknownValueError:
            print("Could not understand audio")
            return
        except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))
            return


'''
-------------------------------------------------------------------------------------------
                                          :)
-------------------------------------------------------------------------------------------
'''

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
        # print("Left: " + str(left[0].y - left[1].y), "Right: " + str(right[0].y - right[1].y))
        if (left[0].y - left[1].y < 0.01) and (right[0].y - right[1].y < 0.01):
            print("Blink")
            pyautogui.sleep(1)
        elif (left[0].y - left[1].y < 0.009):
            pyautogui.click()
            pyautogui.sleep(1)
            print("Wink")
        elif (right[0].y - right[1].y < 0.004):
            print("New Wink, activate speech to text")
            '''text
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save("listening.mp3")
            os.system("afplay listening.mp3")'''
            # recognize_speech_from_microphone()
            # pyautogui.sleep(1)
            new_type()
            # pyautogui.press('f5')
    # print(landmark_points)
    # cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)


