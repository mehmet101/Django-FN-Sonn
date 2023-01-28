import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import re
import string
import pickle
import time
from scipy.sparse import hstack, csr_matrix

def Predict_LR(news_Text):


    tic = time.perf_counter()
    toc = time.perf_counter()
    print(f"LR_Predict Fonksiyona Giris Yapti: {toc - tic:0.4f} seconds")

    LR_ModelPath=r'C:\Users\Kent\Desktop\django-project-2\LR_finalized.sav'
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

    LRModel =pickle.load(open(LR_ModelPath,'rb'))

    toc = time.perf_counter()
    print(f"LR Model açıldı: {toc - tic:0.4f} seconds")
   
    pred_lr = LRModel.predict(new_xv_test)
    score=LRModel.score(xv_test, y_test)
    label = pred_lr[0]
    print("LR_Model Label=", label)
    print("LR_Model Score=", score)

    toc = time.perf_counter()
    print(f"LR Model kullanıldı tahmin ve score oluşturuldu: {toc - tic:0.4f} seconds")

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









# Fit the vectorization on x_train and x_test
    
    # xv_train_test = vectorization.fit_transform(pd.concat([x_train, x_test]))

    # Transform the train and test sets
    # xv_train = xv_train_test[:len(x_train)]
    # xv_test = xv_train_test[len(x_train):]

    
    
    #new_xv_test = vectorization.transform(new_x_test)

    # Transform the new test set
    # new_xv_test = vectorization.transform(new_x_test)
    
    # new_xv_test = vectorization.transform(new_x_test)



    # print('is X Type=',type(new_xv_test.shape))
    # print('is X Shape=',new_xv_test.shape)
    # print('is X Shape[1]=',new_xv_test.shape[1])



 # print("is Model Shape=", LRModel.coef_.shape)
    # print("is Model Shape[1]=", LRModel.coef_.shape[1])
    # print('is Model Type=',type(LRModel))


    # print('Mean', new_xv_test.mean())

    
    # z=LRModel.coef_.shape[1]-new_xv_test.shape[1]

    # print(new_xv_test)

    # # liste= list(new_xv_test)
    # # print(type(liste))
    # # print(liste)
    # new_element=new_xv_test.mean()

    # print("for a giriş")

    # tuple_to_list = list(new_xv_test)
    # tuple_to_list.extend([new_element]*z)
    # new_tuple = tuple(tuple_to_list)



    # for b in range(z-1):
        
    #     new_xv_test = new_xv_test + (new_element,)
    

    # print("for dan a giriş")
    
    # print('is X Type=',new_tuple.shape)
    # print('is X Shape=',new_tuple.shape)
    # print('is X Shape[1]=',new_tuple.shape[1])






    # print('is new_tuple Type=',type(new_tuple))
    # print('is new_tuple Shape=',new_tuple.shape)
    # print('is new_tuple Shape[1]=',new_tuple.shape[1])

    
    
    # test_tuple=tuple(liste)
    # print(type(test_tuple))
    # print(test_tuple)
    # print('is testt tupleee  Shape=',test_tuple.shape)

    # new_xv_test.resize(1,LRModel.coef_.shape[1])
    # print('is X Shape=',new_xv_test.shape[1])
    

    # new_xv_test=np.reshape(new_xv_test, 100)
    # print('is X Shape=',new_xv_test.shape[1])

    # print('is X Shape=',new_xv_test.shape[1])
    # print("is Model Shape=", LRModel.coef_.shape[1])
    # print('is X Shape Type=',type(new_xv_test.shape))
    # print("is Model Shape Type=", type(LRModel.coef_.shape))
