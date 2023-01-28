from django.urls import path
from . import views

urlpatterns=[
    path("home", views.home, name="question"),
    path("", views.main_page,name="main_page"),
    path("list/<int:idd>", views.classifield_news_details , name="news_detail"),
    path("list", views.classifield_news, name="listing"),
    path("Hakkimizda",views.Hakkimizda, name="Hakkimizda" ),
    
]