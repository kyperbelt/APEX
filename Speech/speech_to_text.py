# You need these two libraries installed on your device:
# pip install SpeechRecognition
# pip install PyAudio

# This is a draft version

import speech_recognition as sr

def recognize_speech_from_microphone():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default system microphone as the audio source
    microphone = sr.Microphone()

    # Adjust for ambient noise before listening
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening... (Ctrl+C to stop)")

    # Continuously listen to the microphone
    try:
        while True:
            with microphone as source:
                audio_data = recognizer.listen(source)

            try:
                # Recognize the speech using Google Web Speech API
                text = recognizer.recognize_google(audio_data)
                print("Recognized speech:", text)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Web Speech API; {0}".format(e))

    except KeyboardInterrupt:
        print("Stopping...")

def main():
    # Call the speech recognition function
    recognize_speech_from_microphone()

if __name__ == "__main__":
    main()
