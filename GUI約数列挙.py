# -*- coding: utf-8 -*-

def divisor(n): #n以下の約数列挙
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    table.sort()
    ans = ''
    #len_n = len(str(n))
    for j in range(len(table)):
        #ans += '{:<7}'.format(str(table[j]))
        ans += str(table[j]) + '\t'
        if (j + 1) % 10 == 0:
            ans += '\n'
    return ans


#GUIを書いてみる

import tkinter
from tkinter import messagebox

##フレームの作成
root = tkinter.Tk()

##フレームの名前を設定
root.title("divisor_Tkinter")

##ウィンドウの大きさを設定
root.geometry("700x300")
#root['bg'] = "#005000"

##ラベル作成
var_1 = tkinter.StringVar()
var_1.set("入力された数の約数を列挙します")
label_question = tkinter.Label(root, textvariable = var_1)#, fg = "#ffffff", bg = "#005000")
label_question.grid(row = 0)

##テキストボックスの作成
txt = tkinter.Entry(width = 10)#, bg = "#005000")
txt.place(x = 50, y = 30)

var_2 = tkinter.StringVar()
var_2.set(" ")
##ボタンが押された時に実行される関数
def clicked(self):
    input_num = txt.get()
    if input_num == '':
        res = messagebox.showwarning("エラー", "数字が入力されていません")
        print("showwarning", res)
    else:
        #label_ans.place_forget()
        #var_2 = tkinter.StringVar()
        var_2.set(divisor(int(input_num)))
    txt.delete(0, tkinter.END)
    return var_2
label_ans = tkinter.Label(root, textvariable = var_2, justify = 'left', font = "VLゴシック")
label_ans.place(x = 10, y = 60)

##ボタンの作成
#var_3 = tkinter.StringVar()
#var_3.set("PUSH")
button = tkinter.Button(root, text = "PUSH", fg = "blue", bg = "red")
button.bind("<Button-1>",clicked)
button.place(x = 150, y = 30)

##イベントループ
root.mainloop()
