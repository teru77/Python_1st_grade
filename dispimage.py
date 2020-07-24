import tkinter as tk
import tkinter.filedialog as fd #ファイルダイアログを使うモジュール
import PIL.Image #画像を扱うモジュール
import PIL.ImageTk #tkinterで作った画面上に画像を表示させるモジュール

def dispPhoto(path):    #画像ファイルを標示する関数
    newImage=PIL.Image.open(path).resize((300,300)) #画像を読み込む

    imageData=PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image= imageData)      # -> イメージをラベルに表示する
    imageLabel.image=imageData

def openFile():
    fpath= fd.askopenfilename()     #ファイルダイアログを開いて選択したファイル名を取得する
    if fpath:   #もしファイル(画像)を選択した時、fpathに入れられる
        dispPhoto(fpath)    #fpathを引数としてdispPhotoが実行される
    
root=tk.Tk()
root.geometry("400x350")

btn=tk.Button(text="ファイルを開く",command=openFile)
imageLabel=tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()
