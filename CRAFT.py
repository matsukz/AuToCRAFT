from re import T
from shutil import move
import tkinter, tkinter.messagebox as tk
import tkinter.font as f
import pyautogui
import sys

tki = tkinter.Tk()
tki.geometry('220x150')
tki.title("CRAFT")
tki.attributes("-topmost", True)

def time():
    tki.after(2000, craft)

def craft():
    LOOPCOUNT = 0
    XCounter = 1
    YCounter = 0
    Xjiku = 590
    while LOOPCOUNT < 9:

        if YCounter == 0: #行の位置を計算
            Yjiku = 460
            Yidou = 1

        elif 1 <= YCounter <= 3: #行の位置を計算
            Yjiku = YCounter * 60 + 460
            Yidou = 1
        
        elif YCounter == 4: #Ycounterが4

            pyautogui.moveTo(930,320) #完成したアイテムの取り出し
            pyautogui.click()

            if XCounter == 0: #次の列の位置計算
                Xjiku = 600
                Xidou = 1

            elif 1 <= XCounter <= 8:
                Xjiku = XCounter * 50 + 600
                Xidou = 1

            elif XCounter == 9: #正常終了値。LOOP外へ
                break
            else:
                tkinter.messagebox.showerror("警告", "変数「Xcounter」にエラーがある可能性があります。")
                break
            
            if Xidou == 1: #実際に列を動かすプログラム
                print(str(XCounter) + " X " + str(Xjiku))
                pyautogui.moveTo(Xjiku, 460)
                Xidou = 0
                YCounter = 0
                XCounter = XCounter + 1
                LOOPCOUNT = LOOPCOUNT + 1
                continue
            else:
                tkinter.messagebox.showerror("警告", "変数「Xidou」にエラーがある可能性があります。")
                break

        if Yidou == 1: #行を動かすプログラム
            print(str(YCounter) + " Y " + str(Yjiku))
            pyautogui.moveTo(Xjiku, Yjiku)
            with pyautogui.hold("shift"):
                pyautogui.click()
            YCounter = YCounter + 1
            Yidou = 0
    
    tkinter.messagebox.showinfo("確認", "指定回数のループが完了しました。")
 

btn = tkinter.Button(tki, text='スタート', command=time, width= 20, height = 2)
btn.place(x=40, y=40)

tki.mainloop()