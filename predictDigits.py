import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

#画像ファイルを数値リストに変換する
def imageToData(filename):
    #画像を8x8のグレースケールに変換
    grayImage=PIL.Image.open(filename).convert('L')
    
    grayImage=grayImage.resize((8,8),PIL.Image.ANTIALIAS)   #8x8のグレースケールに変換 小さくても自然な画像になるようにアンチエイリアスを指定
    
    #数値リストに変換
    numImage=numpy.asarray(grayImage,dtype = float) #8x8の数値リストに変換する
    numImage=numpy.floor(16-16*(numImage/256))  #0~16の濃淡に変換
    numImage=numImage.flatten() #1列の数値リストに変換
    return numImage

#数字を予測する
def predictDigits(data):    #何の数字か予測する関数
    #学習用データを読み込む
    digits=sklearn.datasets.load_digits() #画像を読み込む

    #機械学習する
    clf=sklearn.svm.SVC(gamma=0.001)   #学習の準備をする
    clf.fit(digits.data,digits.target)  #データを使って学習
    
    #予測結果を表示する
    n=clf.predict([data])   #何の数字か予測
    print('予測=',n)
#画像ファイルを数値リストに変換する
data=imageToData("4.png")
#数字を予測する
predictDigits(data)
