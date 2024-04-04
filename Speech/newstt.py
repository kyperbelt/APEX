from PIL import Image, ImageTk
import tkinter as tk
import pyautogui
import os
import speech_recognition as sr
import webbrowser
import openai

def gpt(text=''):
    # Initialize the OpenAI API client with your API key
    api_key = ''
    openai.api_key = api_key

    # Call the GPT-4 model to generate code
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-4 engine
        prompt=text,
        max_tokens=100,  # Maximum number of tokens to generate
        n=1,  # Number of completions to generate
        stop="\n",  # Stop generating after reaching newline
        temperature=0.7  # Controls randomness of generation
    )

    # Extract and return the generated code
    return response.choices[0].text.strip()
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
    # Dictionary mapping letters to their spell-out representations
    spell_dict = {
        'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta',
        'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel',
        'i': 'india', 'j': 'juliet', 'k': 'kilo', 'l': 'lima',
        'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa',
        'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
        'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray',
        'y': 'yankee', 'z': 'zulu'
    }

    spell_out_text = ""
    for char in text:
        # Check if the character is in the spell_dict, if not, skip it
        if char.lower() in spell_dict:
            spell_out_text += spell_dict[char.lower()] + " "

    return spell_out_text.strip()

def type_text(text):
    pyautogui.typewrite(text)

def recognize_speech_from_microphone():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default system microphone as the audio source
    microphone = sr.Microphone()

    # Adjust for ambient noise before listening
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening... (Ctrl+C to stop)")

    while True:
        with microphone as source:
            audio_data = recognizer.listen(source)

        try:
            # Recognize the speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("Recognized speech:", text)

            text = text.lower()
            if 'luminous' in text:
                return

            elif 'code' in text:
                if text[len('code')+1:]:
                    gpt(text[len('code')+1:])
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
                    scale = 'sex'
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

            elif 'spell' == text:
                # Need to implement
                pass

            elif 'command' == text:
                # Need to implement
                pass

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))


if __name__ == "__main__":
    # Call the speech recognition function
    recognize_speech_from_microphone()
