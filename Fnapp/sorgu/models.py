from django.db import models

# Create your models here.




class News(models.Model) :

    news_Title= models.CharField(max_length=50)

    news_Author= models.CharField(max_length=50)

    news_Label= models.BooleanField(default=False)

    news_Text= models.CharField(max_length=5000)

    LR_Label= models.IntegerField(default=0)
    DT_Label= models.IntegerField(default=0)
    RFC_Label= models.IntegerField(default=0)
    GBC_Label= models.IntegerField(default=0)
    NB_Label= models.IntegerField(default=0)

    LR_Score= models.FloatField(default=0)
    DT_Score= models.FloatField(default=0)
    RFC_Score= models.FloatField(default=0)
    GBC_Score= models.FloatField(default=0)
    NB_Score= models.FloatField(default=0)

    short_Text= models.CharField(max_length=200,default="")

    news_Subject= models.CharField(max_length=50, default="a")

