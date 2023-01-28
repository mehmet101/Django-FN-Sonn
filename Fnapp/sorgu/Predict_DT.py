import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import re
import string
import pickle
import time
from scipy.sparse import hstack, csr_matrix

def Predict_DT(news_Text):



    tic = time.perf_counter()
    toc = time.perf_counter()
    print(f"DT_Predict Fonksiyona Giris Yapti: {toc - tic:0.4f} seconds")

    DT_ModelPath=r'C:\Users\Kent\Desktop\django-project-2\DT_finalized.sav'
    x_trainPath=r'C:\Users\Kent\Desktop\django-project-2\x_train'
    x_testPath=r'C:\Users\Kent\Desktop\django-project-2\x_test'
    y_testPath=r'C:\Users\Kent\Desktop\django-project-2\y_test'

    x_train=pickle.load(open(x_trainPath,'rb'))
    x_test=pickle.load(open(x_testPath,'rb'))
    y_test=pickle.load(open(y_testPath,'rb'))

    toc = time.perf_counter()
    print(f"Modelden gelen x_train, x_test dosyalar açıldı: {toc - tic:0.4f} seconds")
    
    testing_news = {"text":[news_Text]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt)
    new_x_test = new_def_test["text"]

    toc = time.perf_counter()
    print(f"tahmin edilecek metin temizlendi: {toc - tic:0.4f} seconds")
    
    vectorization =TfidfVectorizer()
    
    xv_train = vectorization.fit_transform(x_train)
    xv_test = vectorization.transform(x_test)
    new_xv_test = vectorization.transform(new_x_test)
   
    toc = time.perf_counter()
    print(f"x_train, x_test, x_predict transform edildi: {toc - tic:0.4f} seconds")

    DTModel =pickle.load(open(DT_ModelPath,'rb'))
    
    toc = time.perf_counter()
    print(f"DT Model açıldı: {toc - tic:0.4f} seconds")

    pred_DT = DTModel.predict(new_xv_test)
    score=DTModel.score(xv_test, y_test)
    label = pred_DT[0]
    print("DT_Model Label=", label)
    print("DT_Model Score=", score)

    toc = time.perf_counter()
    print(f"DT Model kullanıldı tahmin ve score oluşturuldu: {toc - tic:0.4f} seconds")

    result={"label":label,"score":score}


    return result


def output_lable(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Not A Fake News"




def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " " , text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text
