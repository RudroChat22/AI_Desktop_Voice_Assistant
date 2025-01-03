from requests_html import HTMLSession
import speech_to_text
def weather():
    s = HTMLSession()
    query = "hyderabad"
    url = f'https://www.google.com/search?client=opera&q=weather+hyderabad&sourceid=opera&ie=UTF-8&oe=UTF-8'
    r = s.get(url,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0'})
    temp = r.html.find('span#wob_tm',first = True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t',first = True).text
    desc = r.html.find('span#wob_dc',first = True).text
    return temp + " " + unit + " " + desc