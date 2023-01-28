import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import MultinomialNB
import re
import string
import pickle
import time
import datetime



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




e = datetime.datetime.now()
print ("Modelleme Başlangıç Saati: = %s:%s:%s" % (e.hour, e.minute, e.second))

tic = time.perf_counter()
toc = time.perf_counter()
print(f"Modelling.py çalışmaya başladı: {toc - tic:0.4f} seconds")

data_fake = pd.read_csv(r"C:\Users\Kent\Desktop\django-project\Fnapp\sorgu\datasetss\Fake.csv")
data_true = pd.read_csv(r"C:\Users\Kent\Desktop\django-project\Fnapp\sorgu\datasetss\True.csv")
toc = time.perf_counter()
print(f"Data Setler okundu: {toc - tic:0.4f} seconds")

data_fake['class'] = 0
data_true['class'] = 1
toc = time.perf_counter()
print(f"etiket kolonu eklendi : {toc - tic:0.4f} seconds")


data_merge = pd.concat([data_fake, data_true], axis = 0)
toc = time.perf_counter()
print(f"Data setler birleştirildi : {toc - tic:0.4f} seconds")

data = data_merge.drop(['title', 'subject', 'date'], axis = 1)
toc = time.perf_counter()
print(f"Bazı kolonlar atıldı : {toc - tic:0.4f} seconds")




#data.isnull().sum()


data = data.sample(frac = 1)
toc = time.perf_counter()
print(f"Datasetin tamamı tekrar örneklendi : {toc - tic:0.4f} seconds")

data.reset_index(inplace = True)
data.drop(['index'], axis = 1, inplace = True)
toc = time.perf_counter()
print(f"İndex kolonu silindi : {toc - tic:0.4f} seconds")

data['text'] = data['text'].apply(wordopt)
toc = time.perf_counter()
print(f"wordopt fonksiyonu ile data temizlendi: {toc - tic:0.4f} seconds")

x = data['text']
y = data['class']

toc = time.perf_counter()
print(f"x ve y olarak datalar ayrıldı: {toc - tic:0.4f} seconds")

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.20)   
toc = time.perf_counter()
print(f"Veriler split edildi: {toc - tic:0.4f} seconds")






x_train_filename='x_train'
x_test_filename='x_test'
y_train_filename='y_train'
y_test_filename='y_test'
pickle.dump(x_train, open(x_train_filename,'wb'))
pickle.dump(x_test, open(x_test_filename,'wb'))
pickle.dump(y_train, open(y_train_filename,'wb'))
pickle.dump(y_test, open(y_test_filename,'wb'))

toc = time.perf_counter()
print(f"Split edilen x_train, x_test, y_train, y_test kaydedildi: {toc - tic:0.4f} seconds")


vectorization =TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)
toc = time.perf_counter()
print(f"Modellerin eğitilmesi için x_train ve x_test transorm edildi: {toc - tic:0.4f} seconds")






toc = time.perf_counter()
print(f"Veriler vectorization yapildi: {toc - tic:0.4f} seconds")
RFCFileName = 'RFC_finalized.sav'
LRFileName = 'LR_finalized.sav'
DTFileName = 'DT_finalized.sav'
GBCFileName = 'GBC_finalized.sav'
NBFileName = 'NB_finalized.sav'


RFC = RandomForestClassifier(random_state=0)
RFC.fit(xv_train, y_train)
pickle.dump(RFC, open(RFCFileName,'wb'))
toc = time.perf_counter()
print(f"RFC File Olusturuldu: {toc - tic:0.4f} seconds")

LR = LogisticRegression()
LR.fit(xv_train, y_train)
pickle.dump(LR, open(LRFileName,'wb'))
toc = time.perf_counter()
print(f"LR File Olusturuldu: {toc - tic:0.4f} seconds")

DT = DecisionTreeClassifier()
DT.fit(xv_train, y_train)
pickle.dump(LR, open(DTFileName,'wb'))
toc = time.perf_counter()
print(f"DT File Olusturuldu: {toc - tic:0.4f} seconds")

GBC =  GradientBoostingClassifier(random_state = 0)
GBC.fit(xv_train, y_train)
pickle.dump(GBC, open(GBCFileName,'wb'))
toc = time.perf_counter()
print(f"GBC File Olusturuldu: {toc - tic:0.4f} seconds")


NB = MultinomialNB()
NB.fit(xv_train,y_train)
pickle.dump(NB, open(NBFileName,'wb'))
toc = time.perf_counter()
print(f"NB File Olusturuldu: {toc - tic:0.4f} seconds")






toc = time.perf_counter()
print(f"Modelleme Bitti: {toc - tic:0.4f} seconds")



e1 = datetime.datetime.now()
print ("Modelleme Bitiş Saati: = %s:%s:%s" % (e1.hour, e1.minute, e1.second))
 






    






