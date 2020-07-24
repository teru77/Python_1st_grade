import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
#機械学習
import sklearn.datasets
import sklearn.svm
import numpy

#画像を表示
def imageToData(filename):
    grayImage=PIL.Image.open(filename).convert('L')
    grayImage=grayImage.resize((8,8),PIL.Image.ANTIALIAS)

    dispImage=PIL.ImageTk.PhotoImage(grayImage.resize((300,300)))
    imageLabel.configure(image=dispImage)
    imageLabel.image=dispImage

    numImage=numpy.asarray(grayImage,dtype=float)
    numImage=numpy.floor(16-16*(numImage/256))
    numImage=numImage.flatten()
    return numImage



#ファイルダイアログを開く
def openFile():
    fpath=fd.askopenfilename()
    if fpath:
        data=imageToData(fpath)
        predictDigits(data)


def predictDigits(data):
    digits=sklearn.datasets.load_digits()

    clf=sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data,digits.target) #digitsで入手したデータをdataで数字画像,targetで何の数字かを渡す

    n=clf.predict([data])
    textLabel.configure(text='この画像は'+str(n)+'です')

#アプリのウィンドウを作る
root=tk.Tk()
root.geometry("400x400")

btn=tk.Button(root,text='ファイルを開く',command=openFile)
imageLabel=tk.Label()

btn.pack()
imageLabel.pack()

textLabel=tk.Label(text='手書きの文字を認識')
textLabel.pack()

tk.mainloop()



