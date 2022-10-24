import audioop
from cgitb import text
from email.mime import audio
import pyttsx3
import datetime
import playsound
import speech_recognition as sr
import webbrowser as wb
import os
from lib2to3.pgen2.token import RIGHTSHIFTEQUAL
from tkinter import *
from PIL import Image,ImageTk
from threading import Thread
from gtts import gTTS

def AllFun() :
    friday=pyttsx3.init()
    voice=friday.getProperty('voices')
    friday.setProperty('voice',voice[1].id)


    def speak(audio):
        print('Bi-li: '+audio)
        tts = gTTS(text = audio, lang = "vi",slow=False)
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3",True)
        os.remove("sound.mp3")
    def time():
       Time=datetime.datetime.now().strftime("%H:%M:%p")
       speak(Time)

    def today():
        Today=datetime.datetime.now().strftime("%A - %d/%m/%Y")
        speak(Today)

    def Welcome():
        hour=datetime.datetime.now().hour
        if hour>=3 and hour<=10: 
            speak("Chào bạn, Boss")
        elif hour>=11 and hour<=18: 
            speak("Chào buổi chiều, Boss")
        elif hour>=19 and hour<=24:
            speak("chào bạn , Boss")
        speak("tôi có thể giúp gì cho bạn")

    def command():
        c=sr.Recognizer()
        with sr.Microphone() as source:
            c.pause_threshold=1
            audio=c.listen(source)
        try:
            query=c.recognize_google(audio,language='vi-VN')
            print('Boss: '+query)
        except sr.UnknownValueError:
            speak("Xin lỗi Bili không nghe rõ, boss hãy nhập yêu cầu")
            query=str(input("Yêu cầu của boss: "))
        return query
    # def open_application(query):
    #     if "google" in query:
    #         speak("Mở Google Chrome")
    #         time.sleep(2)
    #         os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe') # Trong ngoặc là đường dẫn đến ứng dụng trong máy mình, các bạn tự tìm trong máy mình sao cho đúng nha
    #     elif "word" in query:
    #         speak("Mở Microsoft Word") 
    #         time.sleep(2)
    #         os.startfile('C:\Program Files\Microsoft Office\Office15\WINWORD.EXE') # Ở đây cũng như ở trên
    #     elif "excel" in query:
    #         speak("Mở Microsoft Excel")
    #         time.sleep(2)
    #         os.startfile('C:\Program Files\Microsoft Office\Office15\EXCEL.EXE') # Ở trển cũng giống dưới này =))
    #     else:
    #         speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
    #         time.sleep(3)


    if __name__ == "__main__":
        Welcome()
        while True:
            query=command().lower()
            if "google" in query:
                speak("Bạn muốn tìm kiếm gì, boss?")
                search=command().lower()
                url=f"https://www.google.com/search?q={search}"
                wb.get().open(url)
                speak(f"Here is your {search} on Google")
            elif "youtube" in query:
                speak("Ba")
                search=command().lower()
                url=f"https://www.youtube.com/search?q={search}"
                wb.get().open(url)
                speak(f"Here is your {search} on Youtube")
            elif "open video" in query:
                file=os.path.realpath(r"D:\Album\Video lapto")
                os.startfile(file)
            elif "" in query or "hello" in query:
                speak("Hi, Boss")        
            elif "time" in query:
                time()
            elif "today" in query:
                today()
            elif "bye" in query or "goodbye" in query or "bye" in query:
                speak("Devil's Rose is quiting! Goodbye Boss")
                quit()
            # elif "ứng dụng" in query:
            #     speak("Tên ứng dụng bạn muốn mở là ")
            #     time.sleep(3)
            #     text1 = query
            #     open_application(text1)
            else: 
                speak("Nothing, Sir")
            speak("How can I help you")

    
#Lặp vô tận để hiển thị cửa sổ


def screen():
    
    window = Tk()

    canva  = Canvas(window,height= 500, width= 350,bg="#688B8A")

    canva.pack()
    #avatar cua boss
    avt = ImageTk.PhotoImage(Image.open("image/bear.jpg").resize((40,40)))
    my_label = Label(image=avt)

    my_label.place(x=300,y=0)

    myText = Label(window, text= "ahahahah",bg='#FAEFD4',font='Times 10 bold')
    myText.place(relx = 1, x =-2, y = 50, anchor = NE)


    #avatar cua Bili
    avt_Bili = ImageTk.PhotoImage(Image.open("image/Bili.jpg").resize((40,40)))
    Bili_label = Label(image=avt_Bili)

    Bili_label.place(x=10,y=120)

    BiliText = Label(window, text= 'hhhh',bg='#FAEFD4',font='Times 10 bold')

    BiliText.place( y = 170, anchor = NW)

    # phan input

    Input_Text = Entry(window, width= 18,font='Times 20 bold',bg="#FAEFD4")
    Input_Text.place(y=450, x=20 )
    Input_Btn = Button(window, text= 'SUBMIT',bg='#FFCCBB')
    Input_Btn.place(x=280, y= 455)
    #Thêm tiêu đề cho cửa sổ
    window.title('B-I-L-I')

    #Đặt kích thước của cửa sổ
    window.geometry('350x500')



    window.mainloop()


# đa luồng để chạy chương trình

bili = Thread(target= AllFun)
bili.start()

chatBox = Thread(target= screen )
chatBox.start()