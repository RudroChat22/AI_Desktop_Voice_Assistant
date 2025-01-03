import speech_to_text1
import text_to_speech
import datetime
import webbrowser
import weather
def Action(data):
    user_data = data.lower()
    if "what is your name" in user_data:
        text_to_speech.texttospeech("My name is Jarvis") 
        return "My name is Jarvis"

    elif "good evening" in user_data:
        text_to_speech.texttospeech("good evening sir")
        return "good evening sir"
        

    elif (("what time is it now" in user_data) or ("what is the time" in user_data)):
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour:", (str)(current_time) + "Minute"
        text_to_speech.texttospeech(Time)
        return Time

    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.texttospeech("hello,how may i help you")
        return "hello,how may i help you"
    
    elif "shutdown" in user_data:
        text_to_speech.texttospeech("ok sir")
        return "ok sir"

    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com")
        return 1

    elif "open google" in user_data:
        webbrowser.open("https://www.google.com")
        return 1
        

    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com")
        return 1
        

    elif "check weather" in user_data:
        ans = weather.weather()
        text_to_speech.texttospeech(ans)
        return ans

    else:
        text_to_speech.texttospeech("cannot understand")
        return "cannot understand"
