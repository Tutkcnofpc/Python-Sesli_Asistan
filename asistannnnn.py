import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

aramacumleleritr=["arama yap","bakalım","benim için ara","araştır","bak","google'a bak"]
aramacumlelerieng=["search","looking","looking for","look something","go google"]
musiccumleleritr=["şarkı çal","şarkı aç","şarkı patlat"]
musiccumlelerieng=["Play","Play Music","play","play music","play the music"]                 
kapatmacumleleritr=["eyvallah","bitti","yeterli","çıkış","bay bay","teşekkürler"]
kapatmacumlelerieng=["Thanks","Close","Enough","Quit","Exit","See You","See you","thanks","thank you","close","quit","exit","enough","see you"]
dilsecimicumlelerieng=["Yes English","yes english","YES ENGLISH","Yes please","YES PLEASE","yes please"]
                   
r=sr.Recognizer()
def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speaktr(ask)
        audio=r.listen(source)
        data=''
        try:
            data=r.recognize_google(audio,language='tr')
           
            
        except sr.UnknownValueError:
            speaktr('anlayamadım')
        except sr.RequestError:
            speaktr('Sistem Çalışmıyor')
        return data


def response(data):
    if data in aramacumleleritr:
        search=record('ne aramak istiyorsun')
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        speaktr(search+'için bulunanlar')
        
    if data in aramacumlelerieng:
        search=record(speakeng('what are you looking for'))
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        speakeng('result for'+search)
   
    if data in musiccumleleritr:
        musc=record('istek parçanızı söyleyin')
        driver = webdriver.Chrome(ChromeDriverManager().install())
        url='https://youtube.com/results?search_query='+musc
        webbrowser.get().open(url)
        
        
        
    if data in musiccumlelerieng:
        musc=record(speakeng('tell me your song'))
        driver = webdriver.Chrome(ChromeDriverManager().install())
        url='https://youtube.com/results?search_query='+musc
        webbrowser.get().open(url)
        
        
    if data in kapatmacumleleritr:
        speaktr('hoşçakal')
        exit()
        
    if data in kapatmacumlelerieng:
        speakeng('see you')
        exit()

def speaktr(string):
    tts=gTTS(string,lang='tr')
    rand=random.randint(1,1000)
    file='audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

def speakeng(string):
    tts=gTTS(string,lang='en')
    rand=random.randint(1,1000)
    file='audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

speaktr('Nasıl yardımcı olabilirim? ')


time.sleep(1)
while 1:   
        data=record()
        if data != "":
            print("-->",data)
            response(data)
    
        
        
        
        





    
