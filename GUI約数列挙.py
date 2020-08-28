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

##ラベル作成
label_question = tkinter.Label(root, text = "入力された数の約数を列挙します")
label_question.grid(row = 0)

##テキストボックスの作成
txt = tkinter.Entry(width = 10)
txt.place(x = 50, y = 30)

##ボタンが押された時に実行される関数
def clicked():
    input_num = txt.get()
    if input_num == '':
        res = messagebox.showwarning("エラー", "数字が入力されていません")
        print("showwarning", res)
    else:
        label_ans = tkinter.Label(root, text = divisor(int(input_num)), justify = 'left', font = "VLゴシック")
        label_ans.place(x = 10, y = 60)
    txt.delete(0, tkinter.END)

##ボタンの作成
button = tkinter.Button(root, text = "PUSH", command = clicked)
button.place(x = 150, y = 30)

##イベントループ
root.mainloop()
