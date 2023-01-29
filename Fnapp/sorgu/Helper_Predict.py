from contextlib import _RedirectStream
from django.shortcuts import render
import os 
from .models import News
from .Predict_LR import Predict_LR
from .Predict_RFC import Predict_RFC
from .Predict_DT import Predict_DT
from .Predict_GBC import Predict_GBC
from .Predict_NB import Predict_NB
import datetime








def HelpPredict(news_List):
    

   e = datetime.datetime.now()
   print ("Helper_Predict'e Giriş Yaptı: = %s:%s:%s" % (e.hour, e.minute, e.second))
   news_Text=news_List["news_Text"]
   news_Title=news_List["news_Title"]
   news_Author=news_List["news_Author"]
   news_Subject=news_List["news_Subject"]
   short_Text=news_List["short_Text"]


   labels=0

   a = Predict_LR(news_Text)
   LR_Label=a["label"]
   LR_Score=a["score"]
   print("LR Label=",LR_Label)
   print("LR Score=",LR_Score)
   labels+=LR_Label



   a = Predict_DT(news_Text)
   DT_Label=a["label"]
   DT_Score=a["score"]
   print("DT Label=",DT_Label)
   print("DT Score =",DT_Score)
   labels+=DT_Label

   a = Predict_RFC(news_Text)
   RFC_Label=a["label"]
   RFC_Score=a["score"]
   print("RFC Label=",RFC_Label)
   print("RFC Score",RFC_Score)
   labels+=RFC_Label



   print("3 Algoritma Koşturuldu Sonuçlar Toplamı =",labels)



   if labels != 3 and labels != 0:

      print("sonuç toplamı 3 olmadığı için ek olarak 2 Algoritma Daha koşturulacak")

      a = Predict_GBC(news_Text)
      GBC_Label=a["label"]
      GBC_Score=a["score"]
      print("GBC Label=",GBC_Label)
      print("GBC Score",GBC_Score)
      labels+=GBC_Label

      a = Predict_NB(news_Text)
      NB_Label=a["label"]
      NB_Score=a["score"]
      print("NB Label=",NB_Label)
      print("NB Score",NB_Score)
      labels+=NB_Label
      
   else:
      print("Sonuç Toplamı 3 veya 0 olduğu için yeni Algoritmalar Koşturulmayacak")
      e1 = datetime.datetime.now()
      print ("3 algoritmalar koşturuldu Saat: = %s:%s:%s" % (e1.hour, e1.minute, e1.second))

      GBC_Label=-1
      GBC_Score=-1
      NB_Label=-1
      NB_Score=-1





   if(labels>=3):
      news_Label=1
      print("News Label=",news_Label)

   else:
      news_Label=0
      print("News Label =", news_Label)



   e1 = datetime.datetime.now()
   print("Toplam zaman =",e1-e)




   result = {
   'LR_Label': LR_Label,
   'DT_Label': DT_Label,
   'RFC_Label': RFC_Label,
   'GBC_Label': GBC_Label,
   'NB_Label':NB_Label,
   'LR_Score': LR_Score,
   'DT_Score': DT_Score,
   'RFC_Score': RFC_Score,
   'GBC_Score': GBC_Score,
   'NB_Score':NB_Score,
   'news_Label': news_Label,
   }







   news = News(
     news_Title=news_Title,
     news_Author=news_Author,
     news_Label=news_Label,
     news_Text=news_Text,
     news_Subject=news_Subject,
     short_Text=short_Text,
     LR_Label= LR_Label,
     DT_Label= DT_Label,
     RFC_Label= RFC_Label,
     GBC_Label= GBC_Label,
     NB_Label= NB_Label,
     LR_Score= LR_Score,
     DT_Score= DT_Score,
     RFC_Score= RFC_Score,
     GBC_Score= GBC_Score,
     NB_Score= NB_Score,)
   news.save()



   return result