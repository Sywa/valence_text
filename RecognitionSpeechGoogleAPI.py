# Requires PyAudio and PySpeech.

import speech_recognition as sr

def Recognition(recognition_object, audio):
    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        print(recognition_object.recognize_google(audio, language=LANGUAGE))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def GetFromStream():
    recognition = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognition.listen(source)
    Recognition(recognition, audio)

def GetFromFile(name):
    recognition = sr.Recognizer()
    with sr.WavFile(name) as source:  # use "test.wav" as the audio source
        audio = recognition.record(source)
    Recognition(recognition, audio)


LANGUAGE = "ru-RU"
# audio = GetFromStream(sr)
audio = GetFromFile("agata.wav")



