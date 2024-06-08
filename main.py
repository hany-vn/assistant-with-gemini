from threading import Thread
import speech_recognition as sr
import threading
import time
from time import sleep
from gtts import gTTS
import playsound
import os
import google.generativeai as genai
import json

def hear():
     global on_hear
     r = sr.Recognizer()
     with sr.Microphone() as source:
          on_hear_status = "1" if ( int(time.time()) - on_hear ) < 60 else "0"
          print("------------------> Hear is running ("+on_hear_status+")")
          r.adjust_for_ambient_noise(source)
          audio = r.listen(source)
          try:
               text = r.recognize_google(audio, language="vi-VN")
               print("@Owner: " + text)
               if ( int(time.time()) - on_hear ) > 60:
                    if any(word in text.lower() for word in ["lina", "luna", "lena", "lila", "vina", "mina", "linda"]):
                         on_hear = int(time.time())
                         hear_list.append("lina");
               elif on_hear:
                    on_hear = int(time.time())
                    hear_list.append(text)
          except:
               hear_list.append("error")
               print("* Can't recognize")

def brain():
     global error_hear

     if len(hear_list) > 0:
          print("------------------> Brain is running")
          text = hear_list[0]
          hear_list.pop(0)

          method = "local"
          cache = in_memory(text)
          cache_long = in_memory(text, "long")

          if text == "error":
               method = "error"
               brain_logic = "Tôi không nghe rõ, bạn có thể nói lại không?"
               error_hear += 1
          elif text == "lina":
               method = "call"
               error_hear = 0
               brain_logic = "Hữm"
          elif cache != False:
               method = "short"
               error_hear = 0
               brain_logic = cache
          elif cache_long != False:
               method = "long"
               error_hear = 0
               brain_logic = cache_long
          else:
               method = "gemini"
               error_hear = 0
               brain_logic = False
               while brain_logic == False:
                    brain_logic = gemini_brain(text)

          if error_hear <= 1:
               print("@Lina: " + brain_logic + " ("+method+")")

               speak_list.append(brain_logic)
               if error_hear == 0:
                    short_momory.append(
                         {
                              "role": "user",
                              "parts": [text]
                         }
                    )
                    short_momory.append(
                         {
                              "role": "model",
                              "parts": [brain_logic]
                         }
                    )

def in_memory(text, type="short"):
     if type == "short":
          memory = short_momory
     elif type == "long":
          memory = long_memory
     else:
          return False

     text = text.replace(" ", "")
     for i in range(len(memory)-1, -1, -1):
          if text in memory[i]["parts"][0].replace(" ", ""):
               for j in range(i+1, len(memory)):
                    if memory[j]["role"] == "model":
                         return memory[j]["parts"][0]
     return False

def gemini_brain(promt):
     try:
          memory = []
          for i in training:
               memory.append(i)
          for i in long_memory:
               memory.append(i)
          for i in short_momory:
               memory.append(i)

          genai.configure(api_key="key-here")
          generation_config = {
          "temperature": 1,
          "top_p": 0.95,
          "top_k": 64,
          "max_output_tokens": 8192,
          "response_mime_type": "text/plain",
          }

          model = genai.GenerativeModel(
          model_name="gemini-1.5-flash",
          generation_config=generation_config,
          # safety_settings = Adjust safety settings
          # See https://ai.google.dev/gemini-api/docs/safety-settings
          )

          chat_session = model.start_chat(
          history=memory
          )

          response = chat_session.send_message(promt)
          return response.text
     except:
          return False

def speak():
     if len(speak_list) > 0:
          print("------------------> Speak is running")

          text = speak_list[0]
          speak_list.pop(0)

          tts = gTTS(text, lang='vi')
          tts.save("sound.mp3")
          playsound.playsound("sound.mp3")
          os.remove("sound.mp3")

def save_memory():
     while True:
          sleep(10)
          #print("% Save memory")
          memory = []
          for i in long_memory:
               memory.append(i)
          for i in short_momory:
               memory.append(i)
          with open("./long_memory.json", "w+") as f:
               f.write(json.dumps(memory))

if __name__ == '__main__':
     error_hear = 0
     on_hear = False

     hear_list = []
     speak_list = []

     training = json.loads(open("./training.json", "r").read())
     short_momory = []
     long_memory = json.loads(open("./long_memory.json", "r").read())

     save_memory = threading.Thread(target=save_memory, args=())
     save_memory.start()

     while True:
          hear()
          brain()
          speak()
