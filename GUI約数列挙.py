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
    ans = ""
    for j in table:
        ans += str(j) + ' '
    return ans


#GUIを書いてみる

import tkinter

##フレームの作成
root = tkinter.Tk()

##フレームの名前を設定
root.title("divisor_Tkinter")

##ウィンドウの大きさを設定
root.geometry("800x150")

##ラベル作成
label_question = tkinter.Label(root, text = "入力された数の約数を列挙します")
label_question.grid(row = 0)

##テキストボックスの作成
txt = tkinter.Entry(width = 10)
txt.place(x = 50, y = 30)

##ボタンが押された時に実行される関数
def clicked():
    input_num = int(txt.get())
    label_ans = tkinter.Label(root, text = divisor(input_num))
    label_ans.place(x = 10, y = 60)
    txt.delete(0, tkinter.END)

##ボタンの作成
button = tkinter.Button(root, text = "PUSH", command = clicked)
button.place(x = 150, y = 30)

##イベントループ
root.mainloop()
