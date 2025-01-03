import pyttsx3
def texttospeech(text):
    #text = "hello my nigga mohul podder eat lot of kfc and watermelon"
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate','rate-700')
    engine.say(text)
    engine.runAndWait()
