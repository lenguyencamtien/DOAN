#Thêm thư viện tkinter
from lib2to3.pgen2.token import RIGHTSHIFTEQUAL
from tkinter import *
from PIL import Image,ImageTk
#Tạo một cửa sổ mới
def screen(audio) :
    window = Tk()

    canva  = Canvas(window,height= 500, width= 350,bg="#688B8A")

    canva.pack()
#avatar cua boss
    avt = ImageTk.PhotoImage(Image.open("image/bear.jpg").resize((40,40)))
    my_label = Label(image=avt)

    my_label.place(x=300,y=0)

    myText = Label(window, text= "Helloooooooooooooooooo",bg='#FAEFD4',font='Times 10 bold')
    myText.place(relx = 1, x =-2, y = 50, anchor = NE)


#avatar cua Bili
    avt_Bili = ImageTk.PhotoImage(Image.open("image/Bili.jpg").resize((40,40)))
    Bili_label = Label(image=avt_Bili)

    Bili_label.place(x=10,y=120)

    BiliText = Label(window, text= audio,bg='#FAEFD4',font='Times 10 bold')

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

#Lặp vô tận để hiển thị cửa sổ
    window.mainloop()


screen()