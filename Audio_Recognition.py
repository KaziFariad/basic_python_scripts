import speech_recognition as sr
audio_file = ("Recording.wav")  # audio file in wav format

reader = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio = reader.record(source)

try:
    print("Audio contains:"+reader.recognize_google(audio))
except sr.UnknownValueError:
    print("Couldn't understand")
except sr.RequestError:
    print("Couldn't get results")
