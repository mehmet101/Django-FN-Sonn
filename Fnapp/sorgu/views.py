from contextlib import _RedirectStream
from django.shortcuts import render
import os 
from .models import News
from .Predict_LR import Predict_LR
from .Predict_RFC import Predict_RFC
from .Predict_DT import Predict_DT
from .Predict_GBC import Predict_GBC
from .Predict_NB import Predict_NB
from.Helper_Predict import HelpPredict
import datetime















def home(request):
    print(request)
    

    if request.method == "POST":
         e = datetime.datetime.now()
         print ("Method Post Giriş Saati: = %s:%s:%s" % (e.hour, e.minute, e.second))
         print(request)
         news_Title=request.POST["news_Title"]
         news_Author=request.POST["news_Author"]
         news_Text=request.POST["news_Text"]
         news_Subject=request.POST["news_Subject"]
         short_Text=news_Text[0:110]
         news_List={'news_Title':news_Title,'news_Author':news_Author,'news_Text':news_Text,'news_Subject':news_Subject,'short_Text':short_Text}



         result=HelpPredict(news_List)
        
         print("HelpPredict fonksiyonundan gelen result bilgisi =")
         print(result)


     
         data= {"Haberlist":News.objects.all()[::-1]}
         e1=datetime.datetime.now()
         
         print("Method Post Çıkış Saati, Liste Sayfasına Yönlendiriliyor. ", e1)
         
         return render(request, "classifield_news.html", data)
         
         
         


    return render(request, "index.html")

    


def classifield_news(request):
    data= {"Haberlist":News.objects.all()[::-1]}

    
    
    
    
    return render(request, "classifield_news.html", data)


def classifield_news_details(request, idd):



    data={"data": News.objects.filter(id=idd)}


    
    
    return render(request, "classifield_news_detail.html", data)



def Hakkimizda(request):
    

    
    
    
    
    return render(request, "Hakkimizda.html")    

def main_page(request):
    

    
    
    
    
    return render(request, "main_page.html")  






