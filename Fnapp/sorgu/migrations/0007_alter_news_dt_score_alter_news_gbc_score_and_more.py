# Generated by Django 4.1.5 on 2023-01-28 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorgu', '0006_news_dt_label_news_dt_score_news_gbc_label_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='DT_Score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='GBC_Score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='NB_Score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='RFC_Score',
            field=models.FloatField(default=0),
        ),
    ]
