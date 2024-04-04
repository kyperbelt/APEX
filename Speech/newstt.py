from PIL import Image, ImageTk
import tkinter as tk
import os
import speech_recognition as sr
import webbrowser

def open_youtube():
    # URL of YouTube
    youtube_url = "https://www.youtube.com"
    # Open YouTube in the default web browser
    webbrowser.open(youtube_url)
    return

def search_youtube(query):
    # URL of YouTube
    youtube_url = "https://www.youtube.com"
    search_url = f"{youtube_url}/results?search_query={query}"
    # Open YouTube in the default web browser with search query
    webbrowser.open(search_url)
    return

def open_netflix():
    # URL of Netflix
    netflix_url = "https://www.netflix.com"
    # Open Netflix in the default web browser
    webbrowser.open(netflix_url)
    return

def spell_out(text):
    # Dictionary mapping letters to their spell-out representations
    spell_dict = {
        'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta',
        'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel',
        'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
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
            elif 'open youtube' == text:
                open_youtube()
                return
            elif 'search youtube' == text[:14]:
                # Extract the query from the recognized speech
                query = text[len('search youtube')+1:]
                search_youtube(query)
                return
            elif 'open netflix' == text:
                open_netflix()
                return
            elif 'spell' == text:
                pass

                '''# Display the image with word to letter mappings
                # Ask user to spell out a phrase
                print("Please spell out the phrase.")
                phrase = input("Phrase: ")
                # Get the spell-out version of the phrase
                spell_out_text = spell_out(phrase)
                print("Spell-out:", spell_out_text)'''

            elif 'command' == text:
                # Need to implement
                pass

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))

def main():
    # Call the speech recognition function
    recognize_speech_from_microphone()

if __name__ == "__main__":
    main()
