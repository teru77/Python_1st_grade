import tkinter as tk

def dispLabel():
    lbl.configure(text='こんにちは')

root=tk.Tk() #画面を作成
root.geometry("200x100")#画面の大きさを決める(px)

lbl=tk.Label(text='LABEL')#ラベルを作る
btn=tk.Button(text='push',command = dispLabel)#ボタンを作る 押したらdipLabelが呼び出される,()はいらない

lbl.pack()#配置する
btn.pack()#配置する
tk.mainloop()#作ったウィンドウを表示する



