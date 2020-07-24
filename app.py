import tkinter as tk

root=tk.Tk() #画面を作成
root.geometry("200x100")#画面の大きさを決める(px)

lbl=tk.Label(text='LABEL')#ラベルを作る
btn=tk.Button(text='push')#ボタンを作る

lbl.pack()#配置する
btn.pack()#配置する
tk.mainloop()#作ったウィンドウを表示する
